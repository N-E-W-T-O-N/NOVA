#pragma once
#include "../math/vec3.hpp"

namespace Constants {
constexpr double G = 6.67430e-11;
constexpr double EARTH_MASS = 5.972e24;
constexpr double EARTH_RADIUS = 6371000.0;
const Vec3 VERTICAL_EARTH_RADIUS(EARTH_RADIUS, 0.0, 0.0);
constexpr double SEA_LEVEL_PRESSURE = 101325.0;
constexpr double SEA_LEVEL_TEMPERATURE = 288.15;
constexpr double AIR_GAS_CONSTANT = 287.05;
} // namespace Constants
