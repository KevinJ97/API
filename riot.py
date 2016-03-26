import requests
import json

my_api_key = "16889499-30b8-4ea8-9917-5220f777443e"
url_append_key = "?api_key={}".format(my_api_key)

region = "na" # Locking this application to only be North America at the moment.
version = "v1.4"

base_request_URL = "https://{}.api.pvp.net/api/lol/{}/{}/".format(region,region,version)

def main():
    username = raw_input('Enter a username to search: ')
    get_endpoint = base_request_URL + "summoner/by-name/{}".format(username) + url_append_key
    get_response = requests.get(get_endpoint)
    print (get_response.text)


if __name__ == "__main__":
    main()
