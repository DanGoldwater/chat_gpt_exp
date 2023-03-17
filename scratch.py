#%%
import pandas

df = pandas.read_csv('cancer_4.csv')
df.head()

for a in df['abstract']:
    print(a)
    print('------')