class publisher:
    def __init__(self,name):
      self.name=name

    def display(self):
        print("publisher name:",self.name)
class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print("book title:",self.title)
        print("author:",self.author)
class Python(book):
    def __init__(self,name,title,author,price,no_of_pages):
        super().__init__(name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        super().display()
        print("price:",self.price)
        print("no_of_pages:",self.no_of_pages)
    #create an object of python class
p=Python("ABC publication","python programming",
         "john smith",450,300)
    #display book information
p.display()