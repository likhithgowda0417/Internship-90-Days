class Student:
    college_name = "ABC college"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def update_college(cls, new_name):
        cls.college_name = new_name

    def display_details(self):
        print("name:", self.name)
        print("roll no:", self.roll_no)
        print("college:", Student.college_name)


s1 = Student("arjun", 101)
s2 = Student("rahul", 102)

s1.display_details()
s2.display_details()

Student.update_college("XYZ engineering college")

s1.display_details()
s2.display_details()
