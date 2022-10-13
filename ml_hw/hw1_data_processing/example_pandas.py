import numpy as np
import pandas as pd
import big_o

"""Task 1"""
# categories = ['Hahaha'] * 5000 + ['Haha'] * 5000 + ['Hah'] * 5000
# # categories_set = set(categories)
# categories_array = np.array(categories)
#
# data = pd.DataFrame(categories, columns=['category'], index=range(15000))
#
# # data['category'].apply(lambda x: x in categories)
# # data['category'].isin(categories)
#
# best, others = big_o.big_o(data['category'].apply(lambda x: x in categories_array),
# lambda n: categories, n_repeats=100)
# print(best)

"""Task 2"""
# df = pd.DataFrame({'seller_id': [621] * 3 + [783] * 4, 'quantity': [28, 32, 13, 17, 35, 4, 11],
#                    'date': ['2021-06-01', '2021-06-02', '2021-06-03', '2021-06-04', '2021-06-05', '2021-06-06',
#                             '2021-06-08']})

df = pd.read_csv('dataset_521000_9.txt', sep=';').sort_values(by=['seller_id', 'date'])
df['days_diff'] = df['date'].apply(lambda x: pd.to_datetime(x)).dt.date.diff()
df = df.fillna(pd.Timedelta(1))
df['days_diff'] = df['days_diff'].apply(lambda x: pd.Timedelta(0) if x.days == -1 else x)
print(df)
df['seller_diff'] = df['seller_id'].diff()
df = df.sort_values(by=['seller_id', 'date'])
df['period'] = df.apply(lambda row: 1 if (row['days_diff'].days > 1) or (row['seller_diff'] > 0) else 0, axis=1)
df['period'] = df['period'].cumsum()

mean_period_length = df.groupby('period')['days_diff'].count().mean()
mean_sales_count = df.groupby('period')['quantity'].mean().mean()
mean_periods_count = df.groupby('seller_id')['period'].nunique().mean()

print(f'mean_period_length:{round(mean_period_length, 3)} mean_sales_count:{round(mean_sales_count, 3)} '
      f'mean_periods_count:{round(mean_periods_count, 3)}')
