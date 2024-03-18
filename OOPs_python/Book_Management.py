class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def Book_Details(self):
        return f"""Title of Book is:- {self.title}
        Author of Book is:- {self.author}
        Publication Year of Book is :-{self.year} """
class Ebook(Book):
    def __init__(self, title, author, year,size):
        super().__init__(title, author, year)
        self.size=size
    def Book_Details(self):
        return f"""
        Title of Book is:- {self.title}
        Author of Book is:- {self.author}
        Publication Year of Book is :-{self.year}
        Size of File is := {self.size} """
        
        

#main code
obj1=Ebook("NewBharat","Modi",2025,"10MB")  
print(obj1.Book_Details())