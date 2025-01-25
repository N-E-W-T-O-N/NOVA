import subprocess
import os
import re
import sys

# Regex for extracting version numbers
version_pattern = re.compile(r'\d+\.\d+(\.\d+)?')

def generate_flight_data():
    """
    Main function to check Python and G++ versions then create flight dataset.
    """
    check_python_version()
    check_gpp_version()
    build_and_execute_dependency()

def build_and_execute_dependency():
    """
    Build the C++ program and execute the binary.
    """
    try:
        print("Building the project...")
        subprocess.run(["g++", "-std=c++17", os.path.join("src","main.cpp"), "-o", "nova"], check=True)
        print("Build successful. Running the executable...")
        process = 'nova.exe' if os.name == 'nt' else './nova'
        subprocess.run([process], check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred during the build or execution process.")
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as ex:
        print("An unexpected error occurred.")
        print(f"Error: {ex}")
        sys.exit(1)

def check_python_version():
    """
    Check the installed Python version.
    """
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True, check=True)
        version = extract_version(result.stdout.strip())
        print(f"Python Version: {version}")
        validate_version(version, min_major=3, min_minor=6, software="Python")
    except subprocess.CalledProcessError:
        print("Error: Python is not installed or not found in PATH.")
        sys.exit(1)
    except Exception as e:
        print("An error occurred while checking Python version.")
        print(f"Error: {e}")
        sys.exit(1)

def check_gpp_version():
    """
    Check the installed G++ version.
    """
    try:
        result = subprocess.run(['g++', '--version'], capture_output=True, text=True, check=True)
        version = extract_version(result.stdout.split('\n')[0])
        print(f"G++ Version: {version}")
        validate_version(version, min_major=7, software="G++")
    except subprocess.CalledProcessError:
        print("Error: G++ is not installed or not found in PATH.")
        sys.exit(1)
    except Exception as e:
        print("An error occurred while checking G++ version.")
        print(f"Error: {e}")
        sys.exit(1)

def extract_version(input: str) -> str:
    """
    Extract the version number from a given input string using regex.
    """
    match = version_pattern.search(input)
    if not match:
        raise ValueError(f"Version information not found in input: {input}")
    return match.group()

def validate_version(version: str, min_major: int, min_minor: int = 0, software: str = "Software"):
    """
    Validate the version against minimum required major and minor versions.
    """
    major, minor, *_ = map(int, version.split('.'))
    if major < min_major or (major == min_major and minor < min_minor):
        print(f"{software} version must be at least {min_major}.{min_minor}. Found: {version}")
        sys.exit(1)
