from gc import get_count

class Book:
   def __init__(self, title, author):
    title = title
    self.author = author

class Ebook:
   def __init__(self, title, author):
    self.title = title
    self.author = author

def __init__(self, title, author):
    self.title = title
    self.author = author

class Printbook:
   def __init__(self, title, author):
    self.title = title
    self.author = author
      
class Librabry:
   def __init__(self):
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
