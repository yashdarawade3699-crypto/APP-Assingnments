class Course:
    def __init__(self,Course_name,duration,fee):
        self.Course_name = Course_name
        self.duration = duration
        self.fee = fee

    def get_category(self):
        if self.duration <=6:
            return"Short Duration"
        else:
            return"Long Duration"
    def display(self):
        print("Course Name",self.Course_name)
        print("Duration",self.duration)
        print("Fee",self.fee)
        print("Category",self.get_category())
        print("-"*30)

class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self):
        Course_name = str(input("Enter Course Name:"))
        Duration = int(input("Enter Duration:"))
        fee = int(input("Enter Fee:"))
        course = Course(Course_name,Duration,fee)
        self.courses.append(course)
        print("Course added\n")
    def display(self):
        if len(self.courses) == 0:
            print("No courses added")
        else:
            print("Courses added")

institute = Institute()

n = int(input("Enter Number of Courses: "))

for i in range(n):
    print(f"\nEnter Details of Course {i + 1}")
    institute.add_course()

institute.display()