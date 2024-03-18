'''Question 8:
Create a class Person with attributes name, age, and address. Implement a method 
is_adult that returns True if the person is 18 years or older, otherwise False.'''


class Person:
    def __init__(self,name,age,address) -> None:
        self.name=name
        self.age=age
        self.address=address
    def is_adult(self):
        print(f"""
                Name:-{self.name} 
                Age:-{self.age}
                Address:-{self.address}""")    
        if self.age>=18:
            return True
        else:
            return False
                    
#Main code
person1=Person("Sagar",18,"Ishpaur")
print(person1.is_adult())

        