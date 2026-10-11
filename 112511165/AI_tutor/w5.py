class Employee(object):
    next_id = 1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.id = Employee.next_id
        Employee.next_id += 1

    def get_id(self):
        return self.id

    def pay(self):
        return self.salary

    def raise_salary(self, percent):
        self.salary = self.salary * (100 + percent) // 100

    def __str__(self):
        return f"Employee:{self.id}:{self.name}:{self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        Employee.__init__(self, name, salary)
        self.bonus = bonus
        self.reports = []

    def pay(self):
        return self.salary + self.bonus

    def add_report(self, emp):
        for member in self.reports:
            if member.get_id() == emp.get_id():
                return
        self.reports.append(emp)

    def team_cost(self):
        total = self.pay()
        for member in self.reports:
            total += member.pay()
        return total

    def __str__(self):
        return f"Manager:{self.id}:{self.name}:{self.salary}:{self.bonus}"
