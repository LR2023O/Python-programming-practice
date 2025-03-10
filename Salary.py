class Employee:
    def __init__(self, emp_ID, name, salary):
        self.emp_ID = emp_ID
        self.name = name
        self.salary = salary
        
    def calculate_salary(self):
        return self.salary
    
class HourlyEmployee(Employee):
    def __init__(self, emp_ID, name, rate, hours_worked):
        super().__init__(emp_ID, name, 0)
        self.rate = rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.salary = self.rate*self.hours_worked
        return self.salary
    
class SalariedEmployee(Employee):
     def __init__(self, emp_ID, name, monthly_salary):
        super().__init__(emp_ID, name, monthly_salary)
     def calculate_salary(self):
        return self.salary

hourly_emp = HourlyEmployee(25, "Larry", 20, 160)
salaried_emp = SalariedEmployee(43, "Alex", 5000)
print(f"{hourly_emp.name} :${hourly_emp.calculate_salary()}")
print(f"{salaried_emp.name} :${salaried_emp.calculate_salary()}")
