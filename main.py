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
    
    # story = Story(prologue="Une histoire pour enfant qui se passe dans un chateau", plan="free").add_paragraph_step("Give suspens").add_paragraph_step("Give suspens").add_paragraph_step("Give suspens").add_paragraph_step("Prepare to the end").add_paragraph_step("Give conclusion").get_story()
    b_gen = Book(epub.EpubBook(), "Jean", "World of Wacraft", generated_content=["story"], language="fr").add_metadata().add_chapter().add_page_cover().write_book()

    uvicorn.run(app, host="127.0.0.1", port=8000) # specify port as 8000