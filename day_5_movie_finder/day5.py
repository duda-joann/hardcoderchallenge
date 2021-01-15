import requests


def get_data_from_api(title):
    movies_ids = []
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q": title}
    headers = {
    'x-rapidapi-key': "0f062f447cmsha3201cd01ee5606p1bb261jsn1f348c5fe246",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        raise ConnectionAbortedError

    data = response.json()['d']
    for item in data:
        movies_ids.append(item['id'])
    return movies_ids


def get_movie_details_by(id):
    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt1375666"
    headers = {
            'x-rapidapi-key': "0f062f447cmsha3201cd01ee5606p1bb261jsn1f348c5fe246",
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
        }
    params = {'query': id}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data


def main():
    title = input('Please provide a title: ')
    ids = get_data_from_api(title)
    for id in ids:
        data = get_movie_details_by(id)
        print(data)


if __name__ == '__main__':
    main()