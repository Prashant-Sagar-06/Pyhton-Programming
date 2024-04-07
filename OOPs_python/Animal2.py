class Animal:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
class Lion(Animal):
    def display_details(self):
        print(f"""Lion : The king of jungle
            Name:- {self.name}
            Age:-{self.age}
            Species:-{self.species}""")
class Giraffe(Animal):
    def display_details(self):
        print(f"""Giraffe : The Longest animal  of jungle
            Name:- {self.name}
            Age:-{self.age}
            Species:-{self.species}""")

class Elephant(Animal):
    def display_details(self):
        print(f"""Elephant : The Heaviest animal of jungle
            Name:- {self.name}
            Age:-{self.age}
            Species:-{self.species}""")         

# main code
animal1=Lion("Sher",18,"Indian")
animal2=Giraffe("LAmbi gardan Wala",20,"African")
animal3=Elephant("Haathi",22,"Indian") 

animal1.display_details()
animal2.display_details()
animal3.display_details()

                