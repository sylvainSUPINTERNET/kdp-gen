from src.services.ChatGPTService import get_book_title
from src.models.Book import Book
from ebooklib import epub



def print_book(plan:str="free"):
    theme:str = "White shark"
    
    b = Book(book=epub.EpubBook(), language="fr", theme=theme, author="J. Sylvain")
    b.add_metadata()
    title = b.book.get_metadata('DC', 'title')[0][0]
    print("Book title : ", title)
    b.add_chapter(chapter_title=title).write_epub(file_name=f"MYBOOK.epub")








    
