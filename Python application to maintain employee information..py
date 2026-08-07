class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def get_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"
    def display(self):
        print("Employee Id:",self.emp_id)
        print ("Name:",self.name)
        print ("Salary:",self.salary)
        print("Category:",self.get_category())
        print ("-"*30)

class Company:
    def __init__(self):
       self.employees= []
    def add_employee(self):
        emp_id=int(input("Enter Employee Id:"))
        name=str(input("Enter Employee Name:"))
        salary=int(input("Enter Employee Salary:"))
        emp=Employee(emp_id,name,salary)
        self.employees.append(emp)
        print ("Employee added successfullyy \n")
    def display(self):
         if len(self.employees) == 0:
            print("No Employee Records Found.")
         else:
            print("\nEmployee Details")
            print("=" * 30)
            for emp in self.employees:
                emp.display()
company=Company()

n=int(input("Enter  NO OF Employees :"))
for i in range(n):
    print(f"\nEnter details of Employee {i + 1}")
    company.add_employee()

company.display()


