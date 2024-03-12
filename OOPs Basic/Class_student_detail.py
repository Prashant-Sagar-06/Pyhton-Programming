class Student:
    def __init__(self):
        self.name="NA"
        self.age="NA"
        self.grade="NA"
    def Calculate_Grade(self,percentage):
        if percentage>90 and percentage<=100 :
             return "A++" 
        elif percentage>80 and percentage<=90:
             return "A+"
        elif percentage >70 and percentage<=80:
             return "A"
        elif percentage >=60 and percentage<=70:
            return  "B+"
        elif percentage >=50 and percentage<= 60:
            return "B"
        elif percentage >=40 and percentage<= 50:
            return "c"
        elif percentage >=30 and percentage<=40:
             return "D"
        else:      
             print("Fail")    
                       
    def setDetails(self,name,age,grade):
        self.name=name
        self.age=age  
        self.grade=grade

    def getDetails(self):
        return f'Name:{self.name}\nAge:{self.age}\nGradae{self.grade}'
    #MainCode
student1 = Student()
grade = student1.Calculate_Grade(90)
student_Details=student1.getDetails()
print("calculated grade",grade)
print(student_Details)

