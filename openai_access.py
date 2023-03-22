import os
import json
import pathlib
import openai

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
    response_davinci = openai.ChatCompletion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0.7,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
    )
    return response_davinci

def get_message_from_response(response):
    return response['choices'][0]['text']

def get_model_from_config():
    with open(pathlib.Path('config.json'), 'r') as file:
        config = json.load(file)
    return config