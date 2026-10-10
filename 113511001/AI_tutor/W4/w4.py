class TimeDuration(object):

    def __init__(self, hours, minutes):
        # TODO: store hours and minutes
        self.hours = hours
        self.minutes = minutes
        
    def __str__(self):
        # TODO: return something like "2h 30m"
        return str(self.hours) + "h " + str(self.minutes) + "m"

    def __add__(self, other):
        # TODO:
        # 1. add hours
        # 2. add minutes
        # 3. handle minutes >= 60
        # 4. return a NEW TimeDuration object
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes = total_minutes % 60
        return TimeDuration(total_hours, total_minutes)