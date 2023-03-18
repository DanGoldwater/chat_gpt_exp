#%%
import openai_access
import pypdf
# from Web-Scraping-PubMed import Scrape_Pubmed
from scrape import Scrape_PubMed
import pathlib


def get_pdf_text(path_to_file: str):
    pdf_file = open(pathlib.Path(path_to_file), "rb")
    pdf_reader = pypdf.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# text_bat = get_pdf_text("pdfs/nagel_bat.pdf")
keyword = 'eczema'
Scrape_PubMed.get_medical_paper_data(
    keyword=keyword,
    number_of_papers=100
)

abstracts = Scrape_PubMed.get_abstracts_as_list(Scrape_PubMed.get_filepath(keyword=keyword))

[print(i) for i in abstracts]


# print(bat_summary)


# print(text_dennet)

# print(response_davinci['choices'])
# print(response_chat['choices'])