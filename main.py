from dotenv import load_dotenv
load_dotenv()

import uuid
from ebooklib import epub
from mako.template import Template
import openai
import os
import requests
from PIL import Image
from io import BytesIO

# constants
PROMPT_BOOK_TITLE="Donne un titre de livre pour le thème : "
PROMPT_BOOK_TITLE_CHAPTER="Un titre de chapitre pour thème : "
PROMPT_BOOK_CONTENT_CHAPTER="Ecris une histoire pour le titre : "

PROMPT_STORY="Continue l'histoire : "
PROMPT_STORY="Conclue l'histoire : "


def get_book_title(theme:str, role:str="user")->str:
    # Call chatGPT with theme to get title
    prompt:str=f"{PROMPT_BOOK_TITLE} {theme}"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": f"{role}", "content": f"{prompt}"}])
    return completion.choices[0].message.content

def get_chapter_title(theme:str, role:str="user") -> str:
    # Call chatGPT with theme to get title
    prompt:str=f"{PROMPT_BOOK_TITLE_CHAPTER} {theme}"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": f"{role}", "content": f"{prompt}"}])
    return completion.choices[0].message.content

def get_chapter_content(chapter_title:str, role:str="user") -> str:
    # Call chatGPT with theme to get title
    prompt:str=f"{PROMPT_BOOK_CONTENT_CHAPTER} {chapter_title}"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": f"{role}", "content": f"{prompt}"}])
    return completion.choices[0].message.content


def get_illustration_path(paragraph:str, idx:int):
    try:
        url_dalle = "https://api.openai.com/v1/images/generations"
        num_result = 1
        size = "512x512" # '256x256', '512x512', '1024x1024'
        
        body = {
            "prompt": f"{paragraph}",
            "n": num_result,
            "size": size
        }
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
        }
        resp = requests.post(url=url_dalle, json=body, headers=headers)
        
        if resp.status_code == requests.codes.ok:
            resp_data = resp.json()
            b_img_resp = requests.get(resp_data["data"][0]["url"])
            img = Image.open(BytesIO(b_img_resp.content))
            
            img.save(f"./img_generation/img-{idx}.jpeg")

            img = epub.EpubImage(
                uid=f"img-illustration-{idx}",
                file_name=f"./img_generation/img-{idx}.jpeg",
                media_type="image/jpeg",
                content=open(f"./img_generation/img-{idx}.jpeg", "rb").read()
            )
            
            
            # epub_image_bg = epub.EpubItem(uid=f'img-illustration-{idx}', file_name=f'./img_generation/img-{idx}.jpeg', media_type='image/jpeg', content=open(f"./img_generation/img-{idx}.jpeg", 'rb').read())
            # self.book.add_item(epub_image_bg)
            
            return (img, f"./img_generation/img-{idx}.jpeg")
        else:
            print("error")
            print(resp.json())
            
    except Exception as e:
        print(e)


if __name__ == '__main__':

    # Global Parameters
    theme="Les requins blancs de la méditerranée"
    plan = "free"
    nb_page = 1

    book = epub.EpubBook()
    book_title:str = get_book_title(theme=theme)
    # set metadata
    book.set_identifier(str(uuid.uuid4()))
    book.set_title(book_title)
    book.set_language("fr")
    book.add_author("Joly Sylvain")
    # book.add_author(
    #     "Danko Bananko",
    #     file_as="Gospodin Danko Bananko",
    #     role="ill",
    #     uid="coauthor",
    # )

    template = None
    with open('page_template.html', 'r') as f:
        template = Template(f.read())

    spine = ["nav"]
    for i in range(nb_page):

        chapter_title:str = get_chapter_title(theme=theme)
        chapter_content:str = get_chapter_content(chapter_title=chapter_title).replace("\n", "<br/>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")


        img, img_file_path = get_illustration_path(paragraph="chapter_content", idx=i)
        # render the template with your variablesx
        html = template.render(text=chapter_content, illustration_path=img_file_path)
    
        # create chapter
        c1 = epub.EpubHtml(title=chapter_title, file_name=f"chap_{i}.xhtml", lang="fr")
        c1.content = (
            html
        )

        # add item item
        book.add_item(img)

        # add chapter
        book.add_item(c1)

        # add chapter to spine
        spine.append(c1)


    # define Table Of Contents
    # book.toc = (
    #     epub.Link("chap_01.xhtml", "Introduction", "intro"),
    #     (epub.Section("Simple book"), (c1,)),
    # )

    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())


    # basic spine
    book.spine = spine

    # write to the file
    epub.write_epub("MyBook.epub", book, {})

