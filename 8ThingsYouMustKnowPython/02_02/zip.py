from itertools import zip_longest

'''
Expected output:
The capital city of Netherlands is Amsterdam
The capital city of Nigeria is Abuja
The capital city of Jordan is Amman
The capital city of Nepal is Kathmandu
The capital city of Niger is Niamey
The capital city of Japan is Tokyo
'''

countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo']

for country, capital in zip(countries, capitals):
    print(f'The capital city of {country} is {capital}')

countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu']
print('===============================================')
for country, capital in zip(countries, capitals):
    print(f'The capital city of {country} is {capital}')

for country, capital in zip_longest(countries, capitals, fillvalue='Unknown'):
    print(f'The capital city of {country} is {capital}')


countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo']
pairs = list(zip(countries, capitals))
print(pairs)
country, capital = zip(*pairs)
print(country)
print(capital)
