

from infrastructure.OpenAiConfiguration import chat_GPT_complete
import datetime
import time
from typing import List


class Story(object):
    story_paragraphs:List[str] = []
    limit_req_free_plan_per_minute:int = 3
    delay_free_plan:int = 60
    
    def __init__(self, prologue:str, plan:str="free"):
        
        self.plan = plan
        
        if plan == "free":
            print(f"Using free plan, chatgpt-3.5 turbo is limited {self.limit_req_free_plan_per_minute} requests per minute")
        
        
        self.prologue = prologue
        
    def add_paragraph_step(self, metadata:str = None, role:str="user"):
        print(f"Generating paragraph ({role}) -> {metadata}")
        
        if len(self.story_paragraphs) == 0:
            
            paragraph:str = chat_GPT_complete(self.prologue, "user")

            self.story_paragraphs.append(paragraph)
            return self
        
        if self.plan == "free":
            # TODO => ici bug une fois qu'on a dépassé la limite en fait ça va le faire tout le temps donc il faut implémenter un count annexe
            if (len(self.story_paragraphs) % self.limit_req_free_plan_per_minute) == 0:
                print("Limit of free plan reached waiting for 1 minute for next generation...")
                time.sleep(self.delay_free_plan)
                return self

        if metadata is not None:
            prologue:str = f"{metadata} {self.story_paragraphs[-1]}"
        else:
            prologue:str = f"Continue this story {self.story_paragraphs[-1]}"
            
        paragraph:str = chat_GPT_complete(prologue, role)
        self.story_paragraphs.append(paragraph)
        
        return self

    
    def get_story(self)->List[str]:
        """ Get the story

        Returns:
            list[str]: story as array of string ( contains /r /n and so on, so trim is required )
        """        
        return self.story_paragraphs
    