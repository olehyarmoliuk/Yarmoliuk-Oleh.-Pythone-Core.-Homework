import pyowm

owm = pyowm.OWM('b935502bd96ee8d52e5c9dce3849d093')

while True:
    try: 
        choice = input('Do you want to check weather (yes/no)? ')
        if choice == "Yes" or choice == 'yes':
            city = input("Choose a city ")
            mgr = owm.weather_manager()
            location = mgr.weather_at_place(city)
            weather = location.weather

            print(f'Current weather in {city} is:')
            status = weather.detailed_status
            print(f'status - {status}')
            temp_1 = weather.temperature('celsius')

            for key, value in temp_1.items():
                print(f'{key} (°C) - {value}')

            wind = weather.wind()
            humidity = weather.humidity

            print(f'wind = {wind}')
            print(f'humidity (%) = {humidity}')

            forecast_1 = mgr.forecast_at_place(city, '3h', 8).forecast
            print(f'Forecast for {city} for the next 24h is:')
            for weather in forecast_1:
                print(f"{weather.reference_time('iso')}, temperature measurement - " \
                    + f"{weather.temperature('celsius')}, status - {weather.detailed_status}")


        elif choice == 'No' or choice == 'no':
            print('Good bye.')
            break
        else:
            print('Please, make a choice.')
    except:
        print('There is no such city!') 