"""Instance method, class method, and static method."""


class Employee:
    company_name = "ABC Software"  # Class variable, shared by all objects.

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        # Instance method can use object data through self.
        return f"{self.name} earns {self.salary}"

    @classmethod
    def change_company(cls, new_name):
        # Class method can update class-level data through cls.
        cls.company_name = new_name

    @staticmethod
    def is_workday(day):
        # Static method does not need self or cls.
        return day.lower() not in ["friday", "saturday"]


employee = Employee("Nadia", 45000)

print(employee.show_salary())
print(Employee.company_name)

Employee.change_company("XYZ Tech")
print(Employee.company_name)

print(Employee.is_workday("Sunday"))
