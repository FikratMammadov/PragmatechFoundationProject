# kitablarin siyahisi tertib edilsin
# mueyyen filterler tetbiq edilsin
from models import Books,Book

def getDataFromUser():
    bookName = input("Book Name: ")
    bookPrice = int(input("Book Price: "))
    bookAuthor = input("Book Author: ")
    bookPage = int(input("Book Page: "))
    book = Book(bookName,bookPrice,bookAuthor,bookPage)

''' 
    Book App
    --Welcome To Book App
    --Menu
    1. Add New Book
    2. Show All Books
    3. Return To Main Menu

'''

def appMenu():
    menu="""
--Welcome To Book App
--Menu
1. Add New Book
2. Show All Books
3. Return To Main Menu
4. Total Book Pages
5. Total Book Price
6. Exit
    """
    print(menu)

    order = input('Type your order : ')

    if order=='1':
        addNewBook()
    elif order=='2':
        showAllBooks()
    elif order=='3':
        returnToMain()
    elif order=='4':
        totalPages()
    elif order=='5':
        totalPrice()
    elif order=='6':
        pass
    else:
        print('Unknown order. Type 3 to return main menu')

def addNewBook():
    getDataFromUser()
    appMenu()

def showAllBooks():
    for book in Books:
        print(book.showBook())
    appMenu()

def returnToMain():
    print('Return to main menu')
    appMenu()

def totalPages():
    totalPage = 0
    for book in Books:
        totalPage+=book.Page
    print(f"totalPage: {totalPage}$")
    appMenu()

def totalPrice():
    totalPrice=0
    for book in Books:
        totalPrice+=book.Price
    print(f"totalPrice: {totalPrice}")
    appMenu()



 
appMenu()


 
