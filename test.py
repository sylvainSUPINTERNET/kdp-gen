from io import BytesIO
from dotenv import load_dotenv
import os
import requests
from PIL import Image

load_dotenv()



def generate_illustration(paragraph:str) -> Image:
    
    try:
        url_dalle = "https://api.openai.com/v1/images/generations"
        num_result = 1
        body = {
            "prompt": f"{paragraph}",
            "n": num_result,
            "size": "512x512"  
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
            return img
        else:
            print("error")
            print(resp.json())
            
    except Exception as e:
        print(e)
    





    

# url_img = None
# for d in resp.json()["data"].keys():
#     if d in "url":
#         url_img = resp.json()["data"][d]
#         break

# print(url_img)


    # def fetch_image(paragraph:str):
    #     url_dalle = "https://api.openai.com/v1/images/generations"
    #     body = {
    #         "prompt": f"{paragraph}",
    #         "n": 1,
    #         "size": "512x512"  
    #     }
    #     headers = {
    #         "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    #     }
    #     resp = requests.post(body=body, headers=headers)
    #     img = Image.open(BytesIO(resp.content))