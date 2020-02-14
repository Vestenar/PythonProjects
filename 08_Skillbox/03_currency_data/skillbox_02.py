import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint
from sklearn.linear_model import LinearRegression, LassoLars
from sklearn.neighbors import KNeighborsRegressor
from sklearn import neural_network

money = pd.read_csv('money.csv')
# print(money.head(5))
past = 28
future = 7

df = list()
values = money['value']
for i in range(past, len(money) - future):
    part_of_values = values[(i-past):(i+future)]
    df.append(list(part_of_values))
# pprint.pprint(df, compact=True)

past_columns = [f'past_{i+1}' for i in range(past)]
future_columns = [f'future_{i+1}' for i in range(future)]

df = pd.DataFrame(df, columns=(past_columns + future_columns))
# print(df.head(5))

X = df[past_columns][:-1]  # прошлое (кроме последнего)
Y = df[future_columns][:-1]  # будущее (кроме последнего)

X_test = df[past_columns][-1:]
Y_test = df[future_columns][-1:]
reg = LinearRegression().fit(X,Y)
prediction = reg.predict(X_test)[0]
# print(prediction)
# print(Y_test)
print(np.linalg.norm(prediction - Y_test))  # суммарная ошибка предсказания
plt.plot(prediction, label='predicted')
plt.plot(df[future_columns].iloc[-1], label='real')
plt.legend()
plt.show()

reg = KNeighborsRegressor(n_neighbors=5).fit(X,Y)
prediction = reg.predict(X_test)[0]
print(np.linalg.norm(prediction - Y_test))
plt.plot(prediction, label='predicted')
plt.plot(df[future_columns].iloc[-1], label='real')
plt.legend()
plt.show()

reg = LassoLars(alpha=.1).fit(X, Y)
prediction = reg.predict(X_test)[0]
print(np.linalg.norm(prediction - Y_test))
plt.plot(prediction, label='predicted')
plt.plot(df[future_columns].iloc[-1], label='real')
plt.legend()
plt.show()

reg = neural_network.MLPRegressor(hidden_layer_sizes=1150, activation='tanh', solver='lbfgs',
                                  max_iter=296, alpha=0.0008, random_state=0).fit(X, Y)
prediction = reg.predict(X_test)[0]
print(np.linalg.norm(prediction - Y_test))
plt.plot(prediction, label='predicted')
plt.plot(df[future_columns].iloc[-1], label='real')
plt.legend()
plt.show()
exit()
