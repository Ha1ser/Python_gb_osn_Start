# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

one_hot_dict = {'robot': [1, 0], 'human': [0, 1]}
data['robot'] = data['whoAmI'].map(lambda x: one_hot_dict[x][0])
data['human'] = data['whoAmI'].map(lambda x: one_hot_dict[x][1])
data.drop('whoAmI', axis=1, inplace=True)

data.head() 