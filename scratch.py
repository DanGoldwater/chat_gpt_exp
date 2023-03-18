#%%
import pandas
from scrape import Scrape_PubMed

df = pandas.read_csv(Scrape_PubMed.get_filepath('eczema'))

df.head()
print(df['abstract'].isna().sum())

# df = pandas.read_csv('cancer_4.csv')
# df.head()

# for a in df['abstract']:
#     print(a)
#     print('------')
#%%
from Bio import Entrez

# Set your email (required by NCBI Entrez API)
Entrez.email = "your.email@example.com"

# Define your search term
search_term = "eczema"

# Search for articles on PubMed
handle = Entrez.esearch(db="pubmed", term=search_term, retmax=4)
record = Entrez.read(handle)
handle.close()

# Get the list of PubMed IDs
pubmed_ids = record["IdList"]

print(pubmed_ids)
# Fetch the details of the articles by PubMed ID
handle = Entrez.efetch(db="pubmed", id=pubmed_ids[0], rettype="medline", retmode="text")
records = Entrez.parse(handle)
print(records)

# print(records)
# for i in records:
#     print(i.decode('utf-8'))
# # Iterate through the articles and print the abstracts
# # for record in records.decode('utf-8'):
# #     print(f"Title: {record.get('TI', 'N/A')}")
# #     print(f"Abstract: {record.get('AB', 'N/A')}")
# #     print("=" * 80)

# handle.close()


#%%
from Bio import Entrez

Entrez.email = "dangoldwater@gmail.com"
search_results = Entrez.read(
    Entrez.esearch(
        db="pubmed", term=search_term, retmax=4,
        #   reldate=365, datetype="pdat", usehistory="y"
    )
)
count = int(search_results["Count"])
print("Found %i results" % count)
#%%
batch_size = 10
out_handle = open("recent_orchid_papers.txt", "w")
for start in range(0, count, batch_size):
    end = min(count, start + batch_size)
    print("Going to download record %i to %i" % (start + 1, end))
    fetch_handle = Entrez.efetch(
        db="pubmed",
        rettype="medline",
        retmode="text",
        retstart=start,
        retmax=batch_size,
        webenv=search_results["WebEnv"],
        query_key=search_results["QueryKey"],
    )
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()

#%%
handle = Entrez.efetch(db="pubmed",
                       id=search_results['IdList'][0:2], 
                       rettype="medline", 
                    #    retmode="medline",
                       )
a = handle.read()

print(a)

# with open('tst.xml', 'wb') as file:
#     file.write(handle.read())

# import pandas
# df = pandas.read_xml('tst.xml')
# df.head()

# for id in search_results['IdList']:
#     handle = Entrez.efetch(db="pubmed", id=id, rettype="gb", 
#                         #    retmode="text"
#                            )
#     print(handle.read())


# %%
