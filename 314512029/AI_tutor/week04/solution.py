class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def get_name(self):
        return self.name

    def get_max_speed(self):
        return self.max_speed

    def travel_time(self, distance):
        return distance / self.max_speed

    def __str__(self):
        return "Vehicle:" + self.name + ":" + str(self.max_speed)


class SurveyVehicle(Vehicle):
    next_id = 1

    def __init__(self, name, max_speed, sensor):
        Vehicle.__init__(self, name, max_speed)
        self.sensor = sensor
        self.vehicle_id = SurveyVehicle.next_id
        SurveyVehicle.next_id += 1

    def get_id(self):
        return str(self.vehicle_id).zfill(3)

    def get_sensor(self):
        return self.sensor

    def can_survey(self, required_sensor):
        return self.sensor == required_sensor

    def __str__(self):
        return ("SurveyVehicle:" + self.get_id() + ":" + self.get_name()
                + ":" + self.sensor + ":" + str(self.get_max_speed()))
