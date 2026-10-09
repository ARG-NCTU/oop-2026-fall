class CourseManager:
    def __init__(self):
        self.courses = []

    def register(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def is_registered(self, course):
        return course in self.courses

    def drop(self, course):
        if course not in self.courses:
            raise ValueError(str(course) + " not found")
        self.courses.remove(course)

    def __str__(self):
        self.courses.sort()
        return "{" + ",".join(self.courses) + "}"


manager = CourseManager()

manager.register("Physics")
manager.register("Math")
manager.register("Physics")
print(manager)

print(manager.is_registered("Math"))
print(manager.is_registered("History"))

manager.drop("Physics")
print(manager)
