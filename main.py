from ebooklib import epub
from mako.template import Template


if __name__ == '__main__':

    book = epub.EpubBook()

    # set metadata
    book.set_identifier("id123456")
    book.set_title("Sample book")
    book.set_language("en")

    book.add_author("Author Authorowski")
    book.add_author(
        "Danko Bananko",
        file_as="Gospodin Danko Bananko",
        role="ill",
        uid="coauthor",
    )


    
    nb_page = 5
    
    for i in range(nb_page):
        print(i)
    

    with open('page_template.html', 'r') as f:
        template = Template(f.read())
        
    # render the template with your variables
    html = template.render(text="MYCONTENT", illustration_path="MY PATH")

    # create chapter
    c1 = epub.EpubHtml(title="Intro", file_name="chap_01.xhtml", lang="fr")
    c1.content = (
        html
    )
    
    
    # add chapter
    book.add_item(c1)


    # define Table Of Contents
    # book.toc = (
    #     epub.Link("chap_01.xhtml", "Introduction", "intro"),
    #     (epub.Section("Simple book"), (c1,)),
    # )

    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())


    # basic spine
    book.spine = ["nav", c1]

    # write to the file
    epub.write_epub("xd.epub", book, {})

