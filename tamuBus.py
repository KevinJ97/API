import requests
import json

base_url = "http://transport.tamu.edu:80/BusRoutesFeed/api/"

def testBus(): #Function to get the current free to play rotation.
    endpoint_url = base_url + "route/12/buses/mentor"
    get_response = requests.get(endpoint_url)
    print(get_response.text)

def main():
    testBus()



if __name__ == "__main__":
    main()
