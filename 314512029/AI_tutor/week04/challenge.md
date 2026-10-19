# Part B - Survey Vehicle Hierarchy

This Week 4 challenge transfers getters, information hiding, inheritance, method overriding, and class variables from MIT 6.0001 Lecture 9. It also connects to Lab 04's C++ OOP concepts.

## Problem statement

Implement a base class `Vehicle` and a subclass `SurveyVehicle`.

### `Vehicle`

- `Vehicle(name, max_speed)` stores a string name and a positive numeric maximum speed.
- `get_name()` and `get_max_speed()` return those values.
- `travel_time(distance)` returns `distance / max_speed`.
- `str(vehicle)` returns exactly `Vehicle:<name>:<max_speed>`.

### `SurveyVehicle`

- Inherits from `Vehicle`.
- `SurveyVehicle(name, max_speed, sensor)` initializes the inherited state and stores the sensor name.
- Every new survey vehicle gets a shared sequential ID starting at 1.
- `get_id()` returns the ID as three digits, such as `001`.
- `get_sensor()` returns the sensor name.
- `can_survey(required_sensor)` returns whether its sensor exactly matches the requested name.
- Override `__str__` to return `SurveyVehicle:<id>:<name>:<sensor>:<max_speed>`.

## Constraints

- Names and sensor names are nonempty strings.
- `max_speed > 0` and `distance >= 0`.
- Use inheritance rather than duplicating the base getters and `travel_time`.
- Keep the next ID as a class variable shared by all `SurveyVehicle` instances.

## Examples

1. `str(Vehicle("cart", 5))` returns `Vehicle:cart:5`.
2. The first `SurveyVehicle("alpha", 4, "sonar")` has ID `001` and can survey `"sonar"`.
3. A second survey vehicle has ID `002`; inherited `travel_time(20)` returns `5.0` when its maximum speed is 4.

Before coding, identify which state and methods belong in the parent, which are added by the child, and which method the child overrides.
