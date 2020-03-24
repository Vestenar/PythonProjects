import pandas as pd
import sklearn

money = pd.read_excel('RC_F01_01_2019_T13_08_2019.xlsx')
# print(money.describe())
'''
       nominal        curs
count    147.0  147.000000
mean       1.0   64.816923
std        0.0    1.120933
min        1.0   62.522900
25%        1.0   63.969800
50%        1.0   64.801200
75%        1.0   65.634950
max        1.0   67.192000
'''

future = 7  # предсказание на неделю вперед
past = 28   # данные за 28 дней до

# преобразование таблицы
# организовыввется структура данных - курс на сегодня, курсы за 28 дней до, курсы за 7 длней после

values = money.curs
# print(values)
start = past
end = len(values) - future

raw_data = []
for i in range(start, end):
    past_and_future_values = values[(i - past):(i + future)]
    raw_data.append(list(past_and_future_values))
# print(raw_data)

# делаем из raw_data таблицу

past_columns = []
future_columns = []
for i in range(past):
    past_columns.append(f'past_{i}')
for i in range(future):
    future_columns.append(f'future_{i}')

df = pd.DataFrame(raw_data, columns=(past_columns+future_columns))
# print(df.head(15))
'''
     past_0   past_1   past_2   past_3  ...  future_3  future_4  future_5  future_6
0   67.0795  66.8605  66.9167  67.1920  ...   65.5401   65.5149   65.2582   65.6182
1   66.8605  66.9167  67.1920  67.0820  ...   65.5149   65.2582   65.6182   65.7570
2   66.9167  67.1920  67.0820  66.7617  ...   65.2582   65.6182   65.7570   65.8895
3   67.1920  67.0820  66.7617  66.4438  ...   65.6182   65.7570   65.8895   65.8145
4   67.0820  66.7617  66.4438  66.3309  ...   65.7570   65.8895   65.8145   65.7956'''

# print(df.shape) - # количество значений в фрейме
# отделяем данные входа модели от колонок на выходе
# Тренировочная выборка для обучения модели
x = df[past_columns][:-1]        # только колонки past - вход использыемый для предсказания
y = df[future_columns][:-1]      # только колонки future - целевые значения (target) то, что мы хотим предсказать

# Тестовая выборка для проверки качества модели
x_test = df[past_columns][-1:]      # только последние значения для проверки модели
y_test = df[future_columns][-1:]    #

from sklearn.linear_model import LinearRegression       # линейная регрессия
LinReg = LinearRegression()
LinReg.fit(x, y)                        # обучение модели

prediction = LinReg.predict(x_test)[0]         # предсказание на основе обучения
print(prediction)
print(y_test)

# построение графика
import matplotlib.pyplot as plt
plt.plot(prediction, label='Prediction LR')
plt.plot(y_test.iloc[0], label='Real')      # iloc извлекает из объекта только сами данные
plt.legend()
plt.show()

from sklearn.metrics import mean_absolute_error     # метрика для вычисления средней абсолютной ошибки
metric_mae = mean_absolute_error(y_test, [prediction])
print(metric_mae, ' for Linear Regression')

from sklearn.neighbors import KNeighborsRegressor       # регрессия по соседним значениям
KNReg = KNeighborsRegressor(n_neighbors=1)
KNReg.fit(x, y)
prediction = KNReg.predict(x_test)[0]

plt.plot(prediction, label='Prediction KNR')
plt.plot(y_test.iloc[0], label='Real')      # iloc извлекает из объекта только сами данные
plt.legend()
plt.show()

metric_mae = mean_absolute_error(y_test, [prediction])
print(metric_mae, ' for KNeighbors Regressor')

from sklearn.neural_network import MLPRegressor
MLPReg = MLPRegressor(hidden_layer_sizes=(100, 100, 100), activation='tanh', solver='lbfgs',
                                  max_iter=1000, alpha=0.0008, random_state=10)
MLPReg.fit(x, y)
prediction = MLPReg.predict(x_test)[0]

plt.plot(prediction, label='Prediction MLP')
plt.plot(y_test.iloc[0], label='Real')      # iloc извлекает из объекта только сами данные
plt.legend()
plt.show()

metric_mae = mean_absolute_error(y_test, [prediction])
print(metric_mae, ' for MLP Regressor')

