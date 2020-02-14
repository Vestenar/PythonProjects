import pandas as pd
import numpy as np

df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                   'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                   'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf', 'Muhtar'],
                   'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                   'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
                    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


new_index = "k"
new_data = [5.5, "dog", "Belka", "no", 2]
del_index = "f"

df = df.drop(del_index)
df.loc[new_index] = new_data
print(df)