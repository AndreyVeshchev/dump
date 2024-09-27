import pandas as pd

data = pd.read_csv('football.csv')
print(data)

data = data[(data['Nationality'] == 'Brazil')]
print(data)

penalties_to_list = data['Penalties'].tolist()
print(penalties_to_list)
print(sum(penalties_to_list))

total_penalties = data['Penalties'].sum()
print(total_penalties)
