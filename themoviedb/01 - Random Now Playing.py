import requests
import json
import random

def main():
    my_api_key = "" #replace with key from themoviedb API 
    append_api_key = '?api_key={}'.format(my_api_key)
    url_base = 'https://api.themoviedb.org'
    api_version = '3'
    specify_endpoint = 'movie/now_playing'
    headers = {
      'Accept': 'application/json',
    }
    get_endpoint = '{}/{}/{}{}'.format(url_base, api_version, specify_endpoint, append_api_key)
    get_response = requests.get(get_endpoint, headers=headers)
    get_data = json.loads(get_response.text)

    randomNumber = random.sample(range(0, int(len(get_data['results'])-1)),1)
    print (get_data['results'][randomNumber[0]]['title'])

if __name__ == "__main__":
    main()
