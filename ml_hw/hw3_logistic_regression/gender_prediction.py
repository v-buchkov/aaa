import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('binary_clf_data.csv')

data = data.dropna(subset=['gender'])
data = data.dropna(axis=0)

train, val = train_test_split(data)

print(data.columns)

# print(data['param3'])

# val = pd.read_csv('dataset_527992_9.txt', sep=',')


class LogisticRegression:

    def __init__(self, max_iter=5e3, lr=0.04, tol=0.001, l1_coef=0.1):
        '''
        max_iter – максимальное количеств
        '''

        self.max_iter = max_iter
        self.lr = lr
        self.tol = tol
        self.l1_coef = l1_coef

        self.weights = None
        self.bias = None

    def fit(self, X_train, y_train):
        '''
        Обучение модели.

        X_train – матрица объектов для обучения
        y_train – ответы на объектах для обучения

        '''
        n, m = X_train.shape

        self.weights = np.zeros((m, 1))
        self.bias = np.mean(y_train)

        n_iter = 0
        gradient_norm = np.inf

        while n_iter < self.max_iter and gradient_norm > self.tol:

            dJdw, dJdb = self.grads(X_train, y_train)

            gradient_norm = np.linalg.norm(np.hstack([dJdw.flatten(), [dJdb]]))

            # self.weights = self.weights - self.lr * (dJdw + self.l1(self.weights, m))
            self.weights = self.weights - self.lr * dJdw
            self.bias = self.bias - self.lr * dJdb

            n_iter += 1

        return self

    def l1(self, weights_array, m):
        return np.array([self.l1_coef if w > 0 else -self.l1_coef for w in weights_array.flatten()]).reshape(m, 1)

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def predict_proba(self, X):
        '''
        Метод возвращает вероятность класса 1 на объектах X
        '''
        return self.sigmoid(self.predict(X))

    def predict_class(self, X):
        ans = self.predict_proba(X) >= 0.5
        return ans.astype(int)

    def grads(self, X, y):
        '''
        Расчёт градиентов
        '''
        y_hat = self.predict_proba(X)

        dJdw = np.mean(X * (y_hat - y), axis=0, keepdims=True).T
        dJdb = np.mean(y_hat - y)

        return dJdw, dJdb

    @staticmethod
    def sigmoid(x):
        '''
        Сигмоида от x
        '''
        return 1 / (1 + np.exp(-x))


"""Category"""
ohe_category_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')

train_ohe_category = ohe_category_transformer.fit_transform(train[['category_name']])
val_ohe_category = ohe_category_transformer.transform(val[['category_name']])

train_ohe_category = [np.array(x) for x in train_ohe_category]
val_ohe_category = [np.array(x) for x in val_ohe_category]

"""Subcategory"""
ohe_subcategory_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')

train_ohe_subcategory = ohe_subcategory_transformer.fit_transform(train[['subcategory_name']])
val_ohe_subcategory = ohe_subcategory_transformer.transform(val[['subcategory_name']])

train_ohe_subcategory = [np.array(x) for x in train_ohe_subcategory]
val_ohe_subcategory = [np.array(x) for x in val_ohe_subcategory]

"""Param1"""
ohe_param_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')

train_ohe_param = ohe_param_transformer.fit_transform(train[['param1']])
train_ohe_param = [np.array(x) for x in train_ohe_param]

val_ohe_param = ohe_param_transformer.transform(val[['param1']])
val_ohe_param = [np.array(x) for x in val_ohe_param]

"""Param2"""
ohe_param2_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')

train_ohe_param2 = ohe_param2_transformer.fit_transform(train[['param2']])
train_ohe_param2 = [np.array(x) for x in train_ohe_param2]

val_ohe_param2 = ohe_param2_transformer.transform(val[['param2']])
val_ohe_param2 = [np.array(x) for x in val_ohe_param2]

"""Param3"""
ohe_param3_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')

train_ohe_param3 = ohe_param3_transformer.fit_transform(train[['param3']])
train_ohe_param3 = [np.array(x) for x in train_ohe_param3]

val_ohe_param3 = ohe_param3_transformer.transform(val[['param3']])
val_ohe_param3 = [np.array(x) for x in val_ohe_param3]

"""Finalizing"""
train['ohe'] = train_ohe_category
# to_train = train.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_train = train.groupby('user_id')['ohe'].apply(np.sum)
train['ohe_vector'] = train.apply(lambda row: to_train[row['user_id']], axis=1)

train['ohe_sub'] = train_ohe_subcategory
# to_train = train.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_train = train.groupby('user_id')['ohe_sub'].apply(np.sum)
train['ohe_vector_sub'] = train.apply(lambda row: to_train[row['user_id']], axis=1)

train['ohe_param'] = train_ohe_param
# to_train = train.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_train = train.groupby('user_id')['ohe_param'].apply(np.sum)
train['ohe_vector_param'] = train.apply(lambda row: to_train[row['user_id']], axis=1)

train['ohe_param2'] = train_ohe_param2
# to_train = train.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_train = train.groupby('user_id')['ohe_param2'].apply(np.sum)
train['ohe_vector_param2'] = train.apply(lambda row: to_train[row['user_id']], axis=1)

train['ohe_param3'] = train_ohe_param3
# to_train = train.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_train = train.groupby('user_id')['ohe_param3'].apply(np.sum)
train['ohe_vector_param3'] = train.apply(lambda row: to_train[row['user_id']], axis=1)

"""Drop"""
train = train.drop_duplicates(subset=['user_id'], keep='last')

"""Finalizing"""
val['ohe'] = val_ohe_category
# to_val = val.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_val = val.groupby('user_id')['ohe'].apply(np.sum)
val['ohe_vector'] = val.apply(lambda row: to_val[row['user_id']], axis=1)

val['ohe_sub'] = val_ohe_subcategory
# to_val = val.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_val = val.groupby('user_id')['ohe_sub'].apply(np.sum)
val['ohe_vector_sub'] = val.apply(lambda row: to_val[row['user_id']], axis=1)

val['ohe_param'] = val_ohe_param
# to_val = val.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_val = val.groupby('user_id')['ohe_param'].apply(np.sum)
val['ohe_vector_param'] = val.apply(lambda row: to_val[row['user_id']], axis=1)

val['ohe_param2'] = val_ohe_param2
# to_val = val.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_val = val.groupby('user_id')['ohe_param2'].apply(np.sum)
val['ohe_vector_param2'] = val.apply(lambda row: to_val[row['user_id']], axis=1)

val['ohe_param3'] = val_ohe_param3
# to_val = val.groupby('user_id').apply(lambda row: [sum(x) for x in zip(row['ohe']) if isinstance(x, list)])
to_val = val.groupby('user_id')['ohe_param3'].apply(np.sum)
val['ohe_vector_param3'] = val.apply(lambda row: to_val[row['user_id']], axis=1)

"""Drop"""
val = val.drop_duplicates(subset=['user_id'], keep='last')

# print(train['user_id'].nunique())
# print(train.shape)
#
# print(val[val['user_id'] == 154236473][['user_id', 'ohe_vector']])

# print(train)

# print(train_ohe_category)
#
# train = train.groupby('user_id').apply(lambda row)
# print(train.head())

X_train_category = np.array([x.tolist() for x in train['ohe_vector']])
X_train_subcategory = np.array([x.tolist() for x in train['ohe_vector_sub']])
X_train_param = np.array([x.tolist() for x in train['ohe_vector_param']])
X_train_param2 = np.array([x.tolist() for x in train['ohe_vector_param2']])
X_train_param3 = np.array([x.tolist() for x in train['ohe_vector_param3']])
y_train = train['gender'].apply(lambda x: 1 if x == 'male' else 0).values.reshape(-1, 1)

X_val_category = np.array([x.tolist() for x in val['ohe_vector']])
X_val_subcategory = np.array([x.tolist() for x in val['ohe_vector_sub']])
X_val_param = np.array([x.tolist() for x in val['ohe_vector_param']])
X_val_param2 = np.array([x.tolist() for x in val['ohe_vector_param2']])
X_val_param3 = np.array([x.tolist() for x in val['ohe_vector_param3']])
y_val = val['gender'].apply(lambda x: 1 if x == 'male' else 0).values.reshape(-1, 1)

X_train_extended = np.hstack([X_train_subcategory, X_train_param])
X_val_extended = np.hstack([X_val_subcategory, X_val_param])

model = LogisticRegression()
model.fit(X_train_extended, y_train)

val_predictions = model.predict_class(X_val_extended)

print(accuracy_score(y_val, val_predictions))

'---'

# X_train = count_vectorizer.fit_transform(train_titles.values)
# X_val = count_vectorizer.transform(val_titles.values)

# df = pd.read_csv('real_estate_novosibirsk.csv')
# # df = pd.read_csv('dataset_521000_13.txt', sep=';')
# df = df.drop_duplicates(subset=['item_id'], keep='last')
# df = df.dropna(subset=['area'])
# df = df.dropna(subset=['district'])
# df = df.dropna(subset=['type_of_house'])
# df['price_per_area'] = (df['price'] / df['area']).round()
# df = df[df['price_per_area'] < 10 ** 6]
# df = df[df['price_per_area'] > 10 ** 4]
# df = df[df['area'] > 0]
# df = df[10 ** 5 < df['price']]
# df['price'] = df['price'].round()
#
# # by_district = df.groupby('district').agg({'price': [np.median, np.min, np.max], 'area': [np.median]}).round()
# # unique_rooms = df.rooms_number.unique()
#
# train, test = train_test_split(df, test_size=0.2)
# # print(df[['rooms_number', 'price']].corr(method='spearman'))
#
# """Baseline"""
# # mean_sq_meter_price = (train.price / train.area).mean()
# # prediction = (test.area * mean_sq_meter_price)
# """End Baseline"""
#
# """Approach 1"""
# mean_by_type = train.groupby('type_of_house').apply(lambda row: (row['price'] / row['area']).mean())
# median_by_district = train.groupby('district').apply(lambda row: (row['price'] / row['area']).median())
#
# test['mean_by_type'] = test['type_of_house'].apply(lambda row: mean_by_type[row])
# test['median_by_district'] = test['district'].apply(lambda row: median_by_district[row])
# prediction = test.area * (test.mean_by_type + test.median_by_district) / 2
# """End Approach 1"""
#
# df['MAPE'] = ((test.price.round() - prediction.round()) / test.price.round()).abs()
# MAPE = ((test.price.round() - prediction.round()) / test.price.round()).abs().mean()
# print(MAPE)
#
# prediction.to_csv('solution.csv', header=False, index=False)

# test = pd.read_csv('dataset_527992_9.txt', sep=',')
