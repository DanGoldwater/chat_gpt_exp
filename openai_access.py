import os
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


def get_whether_or_not_paper_is_clinical_study(abstract:str):
    query_primer = "What follows is an abstract drawn from a paper published on PubMed. Determine whether the paper describes a clinical study or not. Return '1' if it does, or '0' for all other kinds of paper. "
    return query_gpt_3_5_turbo(main_text=abstract, query_primer=query_primer)

def get_clinical_info(abstract:str):
    query_primer = "What follows is an abstract drawn from a paper published on PubMed. Determine whether the paper describes clinical intervention being used to treat the condition. If it does, return the name of the treatment, and how effective it was. If the abstract does not describe the effectiveness of a treatment, return '0'. "
    return query_gpt_3_5_turbo(main_text=abstract, query_primer=query_primer)

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
    return response_davinci

def get_message_from_response(response):
    return response['choices'][0]['message']['content']