import numpy as np


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

            self.weights = self.weights - self.lr * (dJdw + self.l1(self.weights, m))
            self.bias = self.bias - self.lr * dJdb

            n_iter += 1

        return self

    def l1(self, weights_array, m):
        return np.array([self.l1_coef if w > 0 else -self.l1_coef for w in weights_array.flatten()]).reshape(m, 1)

    def predict(self, X):
        '''
        Метод возвращает предсказанную метку класса на объектах X
        '''
        return np.dot(X, self.weights) + self.bias

    def predict_proba(self, X):
        '''
        Метод возвращает вероятность класса 1 на объектах X
        '''
        return self.sigmoid(self.predict(X))

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


def read_input():
    n, m = map(int, input().split())
    x_train = np.array([input().split() for _ in range(n)]).astype(float)
    y_train = np.array([input().split() for _ in range(n)]).astype(float)
    return x_train, y_train


def solution():
    x_train, y_train = read_input()

    model = LogisticRegression(max_iter=5e3, lr=0.04, l1_coef=0.1)
    model.fit(x_train, y_train)

    all_weights = [model.bias] + list(model.weights.flatten())
    result = ' '.join(map(lambda x: str(float(x)), all_weights))
    print(result)


solution()
