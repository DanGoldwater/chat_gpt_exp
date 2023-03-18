#%%
import pandas
import openai_access
from scrape import Scrape_PubMed, scraper


df = scraper.load_pubmed_data_from_query('eczema')

abstracts = [a for a in df['AB'][0:10]]
abstracts = [ a for a in abstracts if a]

for ab in abstracts:
    is_clinical = openai_access.get_clinical_info_2(abstract=ab)
    is_clinical = openai_access.get_message_from_response(is_clinical)
    print(is_clinical)
