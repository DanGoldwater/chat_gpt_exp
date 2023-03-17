import os
import openai

openai.api_key = os.environ.get("OPEN_AI_API_KEY")

def get_summary(input_text: str):
    pre_prompt = "What follows is an academic paper. Provide a summary of the paper, around 500 words. Assume a technical audience. #####"
    response_chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pre_prompt + input_text + "#####"},
        ]
    )
    return response_chat

def get_davinci(input_string: str):
    pre_prompt = "All houses have corners"
    response_davinci = openai.ChatCompletion.create(
    model="text-davinci-003",
    prompt= pre_prompt + input_string,
    temperature=0.7,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
    )