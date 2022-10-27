import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def process_rooms_number(x):
    if pd.isna(x):
        return 1
       
    if isinstance(x, int):
        return x
       
    if x.isdigit():
        return int(x)
       
    if x == 'Студия':
        return 1
       
    if x == 'Своб. планировка':
        return 1
       
    if x == '> 9':
        return 10
   
    return 1


df = pd.read_csv('real_estate_novosibirsk.csv')
# df = pd.read_csv('dataset_521000_13.txt', sep=';')
df = df.drop_duplicates(subset=['item_id'], keep='last')
df = df.dropna(subset=['area'])
df = df.dropna(subset=['district'])
df = df.dropna(subset=['type_of_house'])
df['price_per_area'] = (df['price'] / df['area']).round()
df = df[df['price_per_area'] < 10 ** 6]
df = df[df['price_per_area'] > 10 ** 4]
df = df[df['area'] > 0]
df = df[10 ** 5 < df['price']]
df['price'] = df['price'].round()

by_district = df.groupby('district').agg({'price': [np.median, np.min, np.max], 'area': [np.median]}).round()
unique_rooms = df.rooms_number.unique()

df['rooms_number'] = df['rooms_number'].apply(process_rooms_number).copy()

train, test = train_test_split(df, test_size=0.2)
# print(df[['rooms_number', 'price']].corr(method='spearman'))

"""Baseline"""
# mean_sq_meter_price = (train.price / train.area).mean()
# prediction = (test.area * mean_sq_meter_price)
"""End Baseline"""

"""Approach 1"""
mean_by_type = train.groupby('type_of_house').apply(lambda row: (row['price'] / row['area']).mean())
median_by_district = train.groupby('district').apply(lambda row: (row['price'] / row['area']).median())

test['mean_by_type'] = test['type_of_house'].apply(lambda row: mean_by_type[row])
test['median_by_district'] = test['district'].apply(lambda row: median_by_district[row])
prediction = test.area * (test.mean_by_type + test.median_by_district) / 2
"""End Approach 1"""

df['MAPE'] = ((test.price.round() - prediction.round()) / test.price.round()).abs()
MAPE = ((test.price.round() - prediction.round()) / test.price.round()).abs().mean()
print(MAPE)

prediction.to_csv('solution.csv', header=False, index=False)
