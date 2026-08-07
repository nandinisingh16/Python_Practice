#magic methods

class Book:
    def __init__(self,title,author,year,page):
        self.author=author
        self.title=title
        self.year=year
        self.page=page
    def __str__(self):
        return f" name : {self.author}, title : {self.title}, year : {self.year}, number of page : {self.page}"
    def __eq__(self, other):
        return self.author==other.author
    def __gt__(self, other):
        return self.page>other.page
    def __lt__(self, other):
        return self.page<other.page
    def __add__(self, other):
        return f" added pages {self.page+other.page} pages"

book1=Book("jk rowling", "harry Potter", 2002, 1054)
book2=Book("The Hobbit", "J.R.R", 1998, 1350)
book3=Book("The Lion", "C. S. Lewis", 2008, 1002)

print(book1)

print(book1 == book2)

print(book1 > book2)

print(book1 < book2)

print(book1 + book2)