class Employee:
    def __init__(self, name: str, base_salary: float = 0.0):
        if base_salary < 0:
            raise ValueError("Salary must be positive")

        self.name = name
        self.base_salary = base_salary

    def __repr__(self):
        return f"<Employee name={self.name!r} salary={self.calculate_pay()!r}>"

    def calculate_pay(self) -> float:
        return self.base_salary


class HourlyEmployee(Employee):
    def __init__(self, name: str, hourly_rate: float, hours: float):
        if hourly_rate < 0 or hours < 0:
            raise ValueError("Hourly rate and hours worked must be positive")

        super().__init__(name, 0.0)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_pay(self) -> float:
        return self.hourly_rate * self.hours


class Manager(Employee):
    def __init__(self, name: str, base_salary: float, bonus: float = 0.0):
        if bonus < 0:
            raise ValueError("Bonus must be positive")

        super().__init__(name, base_salary)
        self.bonus = bonus

        self.reports: list[Employee] = []

    def calculate_pay(self) -> float:
        return self.base_salary + self.bonus

    def add_report(self, employee: Employee):
        self.reports.append(employee)

    def team_payroll(self) -> float:
        return sum(report.calculate_pay() for report in self.reports) + self.calculate_pay()
