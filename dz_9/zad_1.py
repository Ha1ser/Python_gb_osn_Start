# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

import pandas as pd

df = pd.read_csv('dz_9\california_housing_train.csv')

avg = df[(df['population'] <= 500) & (df['population'] >= 0)]['median_house_value'].mean()

print(avg)