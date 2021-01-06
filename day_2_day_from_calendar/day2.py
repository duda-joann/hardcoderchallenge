import requests
from random import randint
from bs4 import BeautifulSoup
from typing import Dict, List


def get_single_quote() -> Dict:
    """
    get a single  quote from api
    :return: dictinary with text and and author
    """
    request = requests.get("https://type.fit/api/quotes?fbclid=IwAR1hYMVMle01uUHjjHrkXxG5qnp7iRVsLAMuX9gWXgUxwKTQszM98owxooA")
    if request.status_code != 200:
        return {'message': "API not available"}

    data = request.json()
    index = randint(0, len(data)-1)
    return data[index]


def get_data(url: str, headers: Dict, params: Dict) -> Dict:
    """
    :param url: api adress
    :param headers: api key and api domain
    :param params: city, lanquage, units - metric, json as default format
    :return:  dict with choosen weather parameters to show user
    """
    result = requests.get(url, headers=headers, params= params)
    if result.status_code != 200:
        return {'message': "API not available"}

    data = result.json()
    weather = {
        'weather_main': data['weather'][0]['main'],
        'weather_description': data['weather'][0]['description'],
        'temperature[C]': data['main']['temp'],
        'pressure[C]': data['main']['pressure'],
        'humidity[C]': data['main']['humidity'],
        'country_code': data['sys']['country'],
        'timezone': data['timezone'],
    }

    return weather


def get_name_day() -> List:
    """
    return list of name days for current day/today
    """
    response = requests.get("https://imienniczek.pl/widget/js")
    soup = BeautifulSoup(response.text, "html.parser")
    names = []
    for name_day in soup.find_all("span"):
        names.append(name_day.text)

    return names


def main() -> None:
    """
      user's input and ouput
    """
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    quote = get_single_quote()
    city = input('Please provide your city: ')
    params = {"q": "London", "lang": "eng", "units": "metric"}
    headers = {
        'x-rapidapi-key': "0f062f447cmsha3201cd01ee5606p1bb261jsn1f348c5fe246",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
               }

    data = get_data(url, headers, params)
    names = get_name_day()
    print(quote)
    print(city)
    print(f'Name day today: {names}')
    print(*data.items(), sep='\n')


if __name__ == '__main__':
    main()
