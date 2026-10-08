class Manager:
    def work(self):
        print("Manger manages the team")

class Developer:
    def work(self):
        print("Developer develops the software")

class Tester:
    def work(self):
        print("Tester tests the software")

class EmployeeFactory:
    def get_employee(self,emp_type):
        if emp_type == "Manager":
            return Manager()
        elif emp_type == "Developer":
            return Developer()
        elif emp_type == "Tester":
            return Tester()
        else:
            return None


factory = EmployeeFactory()

emp = input("Enter Employee Type (Manager/Developer/Tester): ")

employee = factory.get_employee(emp)

if employee:
    employee.work()
else:
    print("Invalid Employee Type")


