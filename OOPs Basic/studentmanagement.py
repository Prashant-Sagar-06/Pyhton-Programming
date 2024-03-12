class Students:
    def __init__(self,name,student_id,address):
        self.name=name
        self.student_id=student_id
        self.address= address
    def details(self):
        return f"STUDENT NAME:-{self.name},STUDENT ID:-{self.student_id},ADDRESS:-{self.address}"
         
#main
obj1=Students("sagar",123,"ishapur")        
print(obj1.details())

