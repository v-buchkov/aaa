import pandas as pd

df = pd.read_csv('dataset_521000_13.txt')
print(df)
df = df.drop_duplicates(subset=['item_id'], keep='last')
