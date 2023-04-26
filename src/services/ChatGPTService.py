import openai

from src.constants.constants import PROMPT_BOOK_TITLE, PROMPT_BOOK_TITLE_CHAPTER,PROMPT_BOOK_CONTENT_CHAPTER


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
