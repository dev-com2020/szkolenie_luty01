import pandas as pd

# imiona = pd.read_excel('imiona.xlsx', sheet_name='Wynik', header=1)
# imiona2 = pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None, names=['Imię', 'Nazwisko', 'Wynik'])

# imiona.to_json('imiona_wer2.json')

# json = pd.read_json('imiona_wer2.json')
# print(json)

# miasta = pd.read_csv('worldcities.csv')
# print(miasta.head())
# print(miasta.tail())

# print(miasta[['city', "id"]])
# print(miasta.city)
# print(miasta.info())
# print(miasta.isnull().sum())

kostium = pd.read_csv('Halloween.csv', header=2)
# print(kostium)
# print(kostium[:10][['region', '1']])
# print(kostium.region.is_unique)
# kostium.set_index('region', inplace=True)
# kostium.loc['Florida', '4'] = 'Batman'
# print(kostium.loc['Florida'])

# for i, z in kostium.iterrows():
#     if z['1'] == 'Rabbit':
#         print(z['region'])

# print(kostium[(kostium['1'] == 'Rabbit') | (kostium['1'] == 'Dinosaur') ] )
print(kostium[(kostium['1'] == 'Rabbit') & (kostium['2'] == 'Pirate')])


import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

# lista = [[1, 3, 7, 9], [11, 33, 77, 99]]
# zbior = pd.DataFrame(lista)
# zbior.columns = ['Pierwsza', 'Druga', 'Trzecia', 'Czwarta']
# print(zbior)

# slownik = {'Imie': ['Ania', 'Tomek', 'Adam'], 'Wiek': [18, 25, 32]}
# print(pd.DataFrame(slownik))
