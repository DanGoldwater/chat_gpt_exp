#%%
import openai
import pandas
import openai_access
import pathlib
from scrape import Scrape_PubMed, scraper, web_scrape

import os
openai.api_key = os.environ.get("OPEN_AI_API_KEY")

# df = scraper.load_pubmed_data_from_query('gallstone')
filename = 'test.txt'
url = 'https://plato.stanford.edu/entries/hegel-dialectics/'

# web_scrape.save_main_text_to_file(url=url,filename=filename)
with open('data/text_scraped/hegel.txt', 'r') as file:
    text = file.read()


def iteratively_summarise(text):
    summary = text
    for i in range(5):
      chunks = openai_access.break_into_equal_chunks(text, max_tokens=3000)
      summaries = [openai_access.summarise(c) for c in chunks]
      summary = ' '.join(summaries)



# [print(s) for s in summaries]

