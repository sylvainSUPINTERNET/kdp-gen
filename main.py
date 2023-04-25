from dotenv import load_dotenv

from domain.models.Book import Book
load_dotenv()

from ebooklib import epub
from domain.models.Story import Story
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    
    # story = Story(prologue="Ecris une histoire pour les enfants sur les 4 cavaliers de l'apocalypse", plan="free").add_paragraph_step("Give suspens").add_paragraph_step("Prepare to the end").add_paragraph_step("Give conclusion").get_story()
    story = Story(prologue="Ecris une histoire pour les enfants sur les 4 cavaliers de l'apocalypse", plan="free").add_paragraph_step("Give suspens").get_story()

    print(story)
    
    # b_gen = Book(epub.EpubBook(), "Jean", "My title", generated_content=["story"], language="fr").add_metadata().add_chapter(with_toc=False).add_page_cover(with_toc=False).write_book()
    b_gen = Book(epub.EpubBook(), "Jean", "My title", generated_content=story, language="fr").add_metadata().add_chapter(with_toc=False).write_book()

    

    uvicorn.run(app, host="127.0.0.1", port=8000) # specify port as 8000