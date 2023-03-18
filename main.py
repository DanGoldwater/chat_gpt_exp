#%%
import openai_access
import pypdf
# from Web-Scraping-PubMed import Scrape_Pubmed
from scrape import Scrape_PubMed
import pathlib


def get_abstracts(df):
    

# print(response_davinci['choices'])
# print(response_chat['choices'])