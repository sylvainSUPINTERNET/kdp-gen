import uuid
import base64
from ebooklib import epub
from src.services.ChatGPTService import get_book_title, get_chapter_content, get_chapter_title
from src.services.UtilsService import copy_template_to_chapter_page, write_to_page

class Book(object):

    def __init__(self, book:epub.EpubBook, language:str, theme:str, author:str):
        self.book = book
        self.language = language
        self.theme = theme
        self.author = author


        self.book.spine = ['nav']

    def add_metadata(self):
        self.book.set_identifier(str(uuid.uuid4()))
        self.book.set_title(get_book_title(self.theme))
        self.book.set_language(self.language)
        self.book.add_author(self.author)
        return self

    def add_chapter(self, chapter_title:str):
        
        ch_title = get_chapter_title(chapter_title)
        file_name_page = base64.b64encode(ch_title.encode("utf-8")).decode("utf-8")

        print(f"Add Chapter : {ch_title}")

        print(f"Add XHTML page : {file_name_page}")
        
        # Create the XHTML page
        page_file_path = copy_template_to_chapter_page(file_name_page)

        print("write story ...")
        corpus = get_chapter_content(ch_title)
        corpus = corpus.replace("\n", "<br/>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")

        # Generate page xhtml and populate content
        html_output = write_to_page(page_file_path, corpus)


        print(file_name_page)
        print(page_file_path)

        ch = epub.EpubHtml(title=ch_title, file_name=f"{page_file_path}", lang=self.language)
        ch.content=f"{html_output}"

        self.book.add_item(ch)
        self.book.spine.append(ch)

        # add default NCX and Nav file
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())
        
        return self

    def write_epub(self, file_name:str):
        epub.write_epub(file_name, self.book, {})
        print("Book generated with success !")