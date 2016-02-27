import requests
import json

my_api_key = "8776cd8658f49f0ec71d7b77c9a7bace" #replace with key from themoviedb API
append_api_key = '?api_key={}'.format(my_api_key)
url_base = 'https://api.themoviedb.org'
api_version = '3'

def generateRandomMovie():
    #  Function that will generate a random movie that is currently airing. Modify for use.
    import random
    specify_endpoint = 'movie/now_playing'
    headers = {'Accept': 'application/json'}
    get_endpoint = '{}/{}/{}{}'.format(url_base, api_version, specify_endpoint, append_api_key)
    get_response = requests.get(get_endpoint, headers=headers)
    get_data = json.loads(get_response.text)

    randomNumber = random.sample(range(0, int(len(get_data['results'])-1)),1)
    print (get_data['results'][randomNumber[0]]['title'])

def searchForMovie(usersearch):
    #  Function that searches for a specific movie, no error checking. Modify for use.
    specify_endpoint = 'search/movie'
    headers = { 'Accept': 'application/json'}
    payload = { 'query' : usersearch}
    get_endpoint = '{}/{}/{}{}'.format(url_base, api_version, specify_endpoint, append_api_key)
    get_response = requests.get(get_endpoint, headers=headers, params=payload)
    get_data = json.loads(get_response.text)
    print ('\nTitle: %s' % get_data['results'][0]['title'])
    print ('Description: %s' % get_data['results'][0]['overview'])
    print ('Language: %s' % get_data['results'][0]['original_language'])
    print ('ID: %s' % get_data['results'][0]['id'])
    # print (get_response.text)

def main():
    try:
        print('Select an option: \n')
        print('1 - Generate a random movie currently airing\n')
        print('2 - Search\n')
        mode=int(raw_input('Option:'))
        if mode == 1:
            generateRandomMovie()
        elif mode == 2:
            searched=raw_input('Query: ')
            searchForMovie(searched)
        else:
            print('Not an option')
    except ValueError:
        print "Not a number"

if __name__ == "__main__":
    main()
