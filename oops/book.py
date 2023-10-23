class Book:
    name:str
    author:str
    price:int
    publisher:str

    def __init__(self,name,author,price,publisher):
        self.name=name
        self.author=author
        self.price=price
        self.publisher=publisher

    def display(self):
        print(self.name,self.author,self.price,self.publisher)

bk1=Book("harry potter","jk rowley",500,"HP")
# bk1.set_book("harry potter","jk rowley",500,"HP")
bk1.display()