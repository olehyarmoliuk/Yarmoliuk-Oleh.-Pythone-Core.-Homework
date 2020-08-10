countries = {'Spain': ["Barcelona",  "Madrid", "Valencia", "Seville"],
      'England': ["London", "Manchester", "Liverpool", "Oxford"], 
      'Germany' : ["Berlin", "Bayern", "Dresden", "Hamburg"],
      'Italy': ["Rome", "Milan", "Naples", 'Florence'],
      'Ukraine' : ["Kyiv", "Lviv", "Odesa", "Kharkiv", 'Rivne']}

city_1 = input('Choose a city ')

for country, city in countries.items():
    if city_1 in city:
        print(f'{city_1} is located in {country}') 
        break
else: 
    for character in city_1:
        if any(map(str.isdigit, city_1)):
            print('Incorrect value!')
            break
        else:
            print('There is no such city in the list!')
            break