def listToString(s):
    str1 = "" 
    return (str1.join(s)) 


countries = {'Spain': ["Barcelona",  "Madrid", "Valencia", "Seville"],
      'England': ["London", "Manchester", "Liverpool", "Oxford"], 
      'Germany' : ["Berlin", "Bayern", "Dresden", "Hamburg"],
      'Italy': ["Rome", "Milan", "Naples", 'Florence'],
      'Ukraine' : ["Kyiv", "Lviv", "Odesa", "Kharkiv", 'Rivne']}


city_1 = input('Choose a city ')

result_1 = []
for country, city in countries.items():
    if city_1 in city:
        country = listToString(country)
        result_1.append(country)
        print(f'{city_1} is located in {listToString(result_1)}')