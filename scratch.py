#%%
import pandas
import openai_access
from scrape import Scrape_PubMed, scraper

# with open('natural_language.txt', 'r') as file:
#     textt = file.read()

# # print(textt)
# summ = openai_access.get_summary(textt)
# print(summ['choices'][0]['content'])

df = scraper.load_pubmed_data_from_query('eczema')

# for ab in df['AB']:
#     print(ab)

abstracts = [a for a in df['AB'][0:10]]
abstracts = [ a for a in abstracts if a]

for ab in abstracts:
    is_clinical = openai_access.get_clinical_info(abstract=ab)
    is_clinical = openai_access.get_message_from_response(is_clinical)
    print(is_clinical)
