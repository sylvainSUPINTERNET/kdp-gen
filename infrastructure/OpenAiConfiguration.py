import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_GPT_complete( msg:str, role:str) -> str:
    
    """
    This function is used to complete a message using the GPT-3 model.

    :param msg: The message to complete
    :type msg: str
    :param role: The role of the message (user or bot)
    :type role: str
    :return: The completed message
    :rtype: str
    """
    # Max token for prompt DALLE-2
    token_max_prompt = 242
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": f"{role}", "content": f"{msg}"}], max_tokens=token_max_prompt)
    return completion.choices[0].message.content


