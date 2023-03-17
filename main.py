import openai_access
import pypdf
import pathlib


def get_pdf_text(path_to_file: str):
    pdf_file = open(pathlib.Path(path_to_file), "rb")
    pdf_reader = pypdf.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

text_bat = get_pdf_text("pdfs/nagel_bat.pdf")

bat_summary = openai_access.get_summary(input_text=text_bat)

print(bat_summary)


# print(text_dennet)

# print(response_davinci['choices'])
# print(response_chat['choices'])