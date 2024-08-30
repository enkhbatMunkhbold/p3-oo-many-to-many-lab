from datetime import datetime

class Author:
    all = []

    def __init__(self, name):
        self.name = name  
        

class Book:
    all = []

    def __init__(self, title):
        self.title = title


class Contract:
    all = []

    def __init__(self, author, book, date, royalties) -> None:
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

    @property
    def author(self):
        return self.author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Instance must be Author class.")
        
    # @property
    # def book(self):
    #     return self.book
    
    # @book.setter
    # def book(self, book):
    #     if isinstance(book, Book):
    #         self.book = book
    #     else:
    #         raise Exception("Instance must be Book class.")