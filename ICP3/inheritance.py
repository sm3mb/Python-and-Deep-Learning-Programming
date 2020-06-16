class Employee: # declaring Employee Class
    count = 0
    sum = 0
    def __init__(self, name, family, salary, department): # Construtor
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.sum += self.salary # Adding the salary of each employee
        Employee.count += 1 # Counting the total number of employees

    def avgsalary(self): # Average Salary Method/Function
        return Employee.sum/Employee.count

class FullTimeEmployee(Employee): # Declaring Full Time Employee Class and Inheriting the Employee class
    pass

# Creating Instances to FullTimeEmployee class
fullTimeEmp1 = FullTimeEmployee("Sarath", "Manikonda", 7000, "Developer")
fullTimeEmp2 = FullTimeEmployee("Employee 1", "Employee1", 3000, "Manager")
fullTimeEmp3 = FullTimeEmployee("Employee 2", "Employee2", 3500, "Testing")
fullTimeEmp4 = FullTimeEmployee("Employee 3", "Employee3", 5000, "Developer")
fullTimeEmp5 = FullTimeEmployee("Employee 4", "Employee4", 2800, "Testing")

print('Average Salary of Employees:',fullTimeEmp1.avgsalary()) # Calling the Average Salary Method using the instance