from dotenv import load_dotenv
load_dotenv()

from domain.models.Story import Story

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    
    story = Story(prologue="Une histoire pour enfant qui se passe dans un chateau", plan="free").add_paragraph_step("Give suspens").add_paragraph_step("Give suspens").add_paragraph_step("Give suspens").add_paragraph_step("Prepare to the end").add_paragraph_step("Give conclusion").get_story()

    print(story)
    
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) # specify port as 8000