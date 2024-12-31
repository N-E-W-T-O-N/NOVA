#pragma once
#include "../math/vec3.hpp"
#include "constants.hpp"

class Gravity {
public:
  static Vec3 getAcceleration(const Vec3 &position) {
    double altitude = State(position).getAltitude(); 
    if (altitude < 0)
      altitude = 0.0;
    double r = position.magnitude();
    double g = Constants::G * Constants::EARTH_MASS / (r * r);
    return position.normalize() * (-g);
  }
};
