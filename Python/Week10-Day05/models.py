Books=[]
class Book():
    def __init__(self,_name,_price,_author,_page):
        self.Name=_name
        self.Price=_price
        self.Author=_author
        self.Page=_page
        Books.append(self)

    def showBook(self):
        return f"{self.Name} | {self.Price} | {self.Author} | {self.Page}"