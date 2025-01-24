class Book:
   def __init__(self, title, author): #Book: Pride and Prejudice by Jane Austen
    title = title
    self.author = author

class EBook(Book):
   def __init__(self, title, author): #EBook: Snow Crash by Neal Stephenson, File Size: 500KB
    self.title = title
    self.author = author

class PrintBook(Book):
   def __init__(self, title, author): #PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
    self.title = title
    self.author = author
     
class Librabry: 
   def __init__(self): #PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
    self.Book [""]
    self.page_count = get_count
    print(f"Title: {Book.title}")
    print(f"Author: {Book.author}")
      
def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"  
def __del__(self):
        print("Deleting", self.title)
   
if isinstance(Book, Ebook):
                print(f"File Size: {Book.file_size} MB")
elif isinstance(Book, Printbook, ):
                print(f"Page Count: {Book.get_count} pages")        
print("------------------------")
self.books = [], ("append", "list_books" )
super().__init__, ("self.file_size")
if __name__=="__main__":
   main()
