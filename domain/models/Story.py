

from infrastructure.OpenAiConfiguration import chat_GPT_complete


class Story():
    story_paragraphs = []
    backtrace_generation = ""
    continue_text = "Continue with story"
    
    def __init__(self, theme:str , itteration:int = 5):
        self.theme = theme
        self.itteration = itteration
        
    def add_paragraph(self, paragraph:str):
        chat_GPT_complete()
        self.story_paragraphs.append(paragraph)
        