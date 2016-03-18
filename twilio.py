import requests
import json

my_api_key = "vVCmw4lkUImau6OODWJCCDqtJYUmzAEMwW0ELLGD"
auth_API = '?auth={}'.format(my_api_key)
url_base = 'https://api.twilio.com/2010-04-01'

def main():
    #  Example code to test GET response
    get_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name.json'
    get_response = requests.get(get_endpoint)
    print (get_response.text)

    #  Example code to test PUT response
    put_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name.json'
    payload = json.dumps({ "first": "Jack", "last": "Sparrow" })
    put_response = requests.put(put_endpoint, data=payload)
    print (put_response.text)

    #  Example code to test POST response
    post_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name.json'
    payload = json.dumps({"user_id" : "jack", "text" : "Ahoy!"})
    post_response = requests.post(post_endpoint, data=payload)
    print (put_response.text)

    #  Example code to test PATCH response
    patch_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name/.json'
    payload = json.dumps({'last':'Jones'})
    patch_response = requests.patch(put_endpoint, data=payload)
    print (patch_response.text)

    #  Example code to test DELETE response
    delete_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name/last.json'
    delete_response = requests.delete(delete_endpoint)
    print delete_response.text

    #-----------------------------------------------------------------------------------

    #  Sample Put request to add to/update FireBase Database
    username = "TEST" #change this to where ever you want the newly created item.
    put_endpoint = 'https://spoti.firebaseio.com/{}.json?auth={}'.format(username, my_api_key)
    put_data = { "first": "Fire", "last": "Base" }
    payload = json.dumps(put_data)
    put_response = requests.put(put_endpoint, data=payload)
    print (put_response.text)

    #  Sample GET request from a FireBase Database
    username = 'TEST'
    get_endpoint = 'https://spoti.firebaseio.com/{}.json?auth={}'.format(username, my_api_key)
    get_response = requests.get(get_endpoint)
    print (get_response.text)


if __name__ == "__main__":
    main()
