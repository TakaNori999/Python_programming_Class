class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, subject, grade):
        self.grades.append((subject, grade)) 
    def average_grade(self):
        if not self.grades:
            return 0
        else:
            s = 0
            for subject, grade in self.grades:
                s += grade
            #s = sum(grade for subject, grade in self.grades) #ジェンレータ式
            return s / len(self.grades)
    def get_grade(self):
        if not self.grades:
            print("No grade")
        else:
            for box1, box2 in self.grades:
                print(f"subject={box1}, grade={box2}")
    def get_evaluation(self):
        ave = self.average_grade()
        if ave >= 90:
            return "A"
        elif ave >= 80:
            return "B"
        elif ave >= 70:
            return "C"
        elif ave >= 60:
            return "D"
        else:
            return "Fail"
class ScienceStudent(Student):
    def special_project(self):
        print("Science project")
class ArtsStudent(Student):
    def art_exhibition(self):
        print("Exhibition")

science_student1 = ScienceStudent("Taro")
science_student1.add_grade("math", 89)
science_student1.add_grade("science", 77)
science_student1.add_grade("physics", 71)
science_student1.get_grade()

#arts_student1 = ArtsStudent("Jiro")
#arts_student1.add_grade("Art", 29)
#arts_student1.add_grade("literature", 80)

print(f"{science_student1.name} AVERAGE={science_student1.average_grade()}")
print(f"{science_student1.name} GRADE={science_student1.get_evaluation()}")

#print(f"{arts_student1.name} AVERAGE={arts_student1.average_grade()}")
#print(f"{arts_student1.name} GRADE={arts_student1.get_evaluation()}")