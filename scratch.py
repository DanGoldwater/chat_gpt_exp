#%%
import pandas
import openai_access
import pathlib
from scrape import Scrape_PubMed, scraper


df = scraper.load_pubmed_data_from_query('gallstone')

def get_prompt(prompt_name: str):
    prompt_name += '.txt'
    path = pathlib.Path('prompts') / prompt_name
    print(f'Path is {path}')
    with open(path, 'rb') as file:
        prompt = file.read()
    return str(prompt)
    

print(get_prompt('medical_abstract_summary'))

print(openai_access.get_davinci(pre_prompt= get_prompt('medical_abstract_summary'), input_string=df['AB'][0]))
# print(df['AB'][0])

# abstracts = [a for a in df['AB'][0:10]]
# abstracts = [ a for a in abstracts if a]

# for ab in abstracts:
#     is_clinical = openai_access.get_clinical_info_2(abstract=ab)
#     is_clinical = openai_access.get_message_from_response(is_clinical)
#     print(is_clinical)
