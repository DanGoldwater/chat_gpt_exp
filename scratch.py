#%%
import openai
import pandas
import openai_access
import pathlib
from scrape import Scrape_PubMed, scraper

import os
openai.api_key = os.environ.get("OPEN_AI_API_KEY")

df = scraper.load_pubmed_data_from_query('gallstone')

def get_prompt(prompt_name: str):
    prompt_name += '.txt'
    path = pathlib.Path('prompts') / prompt_name
    print(f'Path is {path}')
    with open(path, 'rb') as file:
        prompt = file.read()
    return str(prompt)
    

print(get_prompt('medical_abstract_summary'))

response = openai_access.get_davinci(pre_prompt= get_prompt('medical_abstract_summary'), input_string=df['AB'][0])
print(openai_access.get_message_from_response(response))
# print(df['AB'][0])


# abstracts = [a for a in df['AB'][0:10]]
# abstracts = [ a for a in abstracts if a]

# for ab in abstracts:
#     is_clinical = openai_access.get_clinical_info_2(abstract=ab)
#     is_clinical = openai_access.get_message_from_response(is_clinical)
#     print(is_clinical)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Convert this text to a programmatic command:\n\nExample: Ask Constance if we need some bread\nOutput: send-msg `find constance` Do we need some bread?\n\nReach out to the ski store and figure out if I can get my skis fixed before I leave on Thursday",
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"]
)
#%%
print( os.environ.get("OPEN_AI_API_KEY"))