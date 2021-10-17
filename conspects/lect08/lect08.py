from datetime import date
from collections import dataclasses


Weather = get_weather ("city", "temp, humidity, wind, chance_of_rain")

def get_user(user_id: int):
    username = 'john'
    email = 'jonhsmith@example.com'
    return user_id, username, email

def get_weather (city: str):
    temp = 21
    humidity = 40
    wind = 2
    chance_of_rain = 25
    # return city, temp, humidity, wind, chance_of_rain
    return {
        "city" : city,
        "temp" : temp,
        "humidity" :humidity,
        "wind" : wind,
        "chance_of_rain" : chance_of_rain,
    }

def main():
    user = get_user(1)
    _, username, email, birth_date = user
    print(user)
    print(username)
    print(email)
    print(birth_date)

if __name__ == '__main__':
