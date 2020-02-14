import pandas as pd
import matplotlib.pyplot as plt

file = 'RC_F01_01_2019_T13_08_2019.xlsx'
data = pd.read_excel(file)
# print(data.head(20))
# print(data.curs.head(20))
values = data['curs']
plt.plot(values)
plt.show()