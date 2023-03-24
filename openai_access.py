import os
import tiktoken
import json
import pathlib
import openai
from scrape import web_scrape

openai.api_key = os.environ.get("OPEN_AI_API_KEY")

def get_academic_summary(input_text: str):
    query_primer = "What follows is an academic text. Please summarise it in 300 words. You can use technical language."
    return query_gpt_3_5_turbo(main_text=input_text, query_primer=query_primer)



def query_gpt_3_5_turbo(main_text: str, query_primer: str):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query_primer + "###" + main_text + "#####"},
        ]
    )
    return response

# def query_davinci(preprompt: str, main_prompt: str):
#     return

def get_whether_or_not_paper_is_clinical_study(abstract:str):
    query_primer = "What follows is an abstract drawn from a paper published on PubMed. Determine whether the paper describes a clinical study or not. Return '1' if it does, or '0' for all other kinds of paper. "
    return query_gpt_3_5_turbo(main_text=abstract, query_primer=query_primer)

def get_clinical_info(abstract:str):
    query_primer = "What follows is an abstract drawn from a paper published on PubMed. Determine whether the paper describes clinical intervention being used to treat the condition. If it does, return the name of the treatment, and how effective it was. If the abstract does not describe the effectiveness of a treatment, return '0'. Do not pad your answer with context; be concise."
    return query_gpt_3_5_turbo(main_text=abstract, query_primer=query_primer)

def get_clinical_info_2(abstract:str):
    query_primer = "What follows is an abstract drawn from a paper published on PubMed. Based on the abstract, fill out the following table. If the abstract describes a study investigating the effectiveness of a treatment, return fill in and return the following table: \n  TREATMENT_NAME: $$$$ \n EFFECTIVENESS: $$$$ \n \n If the abstract does not describe a study investigating the effectiveness of a treatment, return '0', and nothing else. "
    return query_model(query_primer + abstract)
    # return query_gpt_3_5_turbo(main_text=abstract, query_primer=query_primer)

def query_model(query):
    query_args = get_model_from_config()
    query_args.update({"prompt": query})
    return openai.Completion.create(**query_args)

def get_davinci(pre_prompt: str, input_string: str):
    prompt = pre_prompt + input_string
    response_davinci = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0.7,
    max_tokens=900,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
    )
    return response_davinci

def get_prompt(prompt_name: str):
    prompt_name += '.txt'
    path = pathlib.Path('prompts') / prompt_name
    with open(path, 'rb') as file:
        prompt = file.read()
    return str(prompt)
    

def summarise(input):
    pre_prompt = get_prompt('summarizer')
    response = get_davinci(pre_prompt=pre_prompt, input_string=input)
    return get_message_from_response(response)

def get_message_from_response(response):
    return response['choices'][0]['text']

def get_model_from_config():
    with open(pathlib.Path('config.json'), 'r') as file:
        config = json.load(file)
    return config


def get_and_summarise_text_file(filename:str):
   filename = pathlib.Path('data/text_scraped') / filename
   with open(filename, 'r') as file:
      text = file.read()
   text = web_scrape.remove_blank_lines(text)
   text = text.strip()
   return summarise(text)




def break_into_equal_chunks(text, max_tokens=3000):
    text = text.replace('\n', ' ')
    encoder = tiktoken.get_encoding('cl100k_base')
    tokens = encoder.encode(text)
    if len(tokens) < max_tokens:
        return [text]

    num_chunks = (len(tokens) // max_tokens) + 1
    tokens_per_chunk = len(tokens) // num_chunks
    
    chunks = []
    current_chunk = []

    for i, token in enumerate(tokens):
        current_chunk.append(token)
        if (i + 1) % tokens_per_chunk == 0 or i == len(tokens) - 1:
            chunks.append(encoder.decode(current_chunk))
            current_chunk = []

    return chunks