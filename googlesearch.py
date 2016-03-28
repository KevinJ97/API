import requests
import json

my_api_key = "rKxaoEeEqWGh5CLFvMBmK5pEv9WeYA2aZEswJFnX"
auth_API = '?auth={}'.format(my_api_key)
url_base = 'https://iofood.firebaseio.com'

def main():
    #  Example code to test GET response
    # get_endpoint = 'https://www.googleapis.com/customsearch/v1'
    # data = {'key': 'AIzaSyAl-5kUI1ir5CF90nW-6cjPijs1kxsb-Fw','cx':'008457250590413522654:dl2_s2ixyas', 'q': 'candy'}
    # get_response = requests.get(get_endpoint, params=data)
    # print (get_response.text)
    #
    # #  Example code to test PUT response
    # put_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name.json'
    # payload = json.dumps({ "first": "Jack", "last": "Sparrow" })
    # put_response = requests.put(put_endpoint, data=payload)
    # print (put_response.text)
    #
    # #  Example code to test POST response
    # post_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name.json'
    # payload = json.dumps({"user_id" : "jack", "text" : "Ahoy!"})
    # post_response = requests.post(post_endpoint, data=payload)
    # print (put_response.text)
    #
    # #  Example code to test PATCH response
    # patch_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name/.json'
    # payload = json.dumps({'last':'Jones'})
    # patch_response = requests.patch(put_endpoint, data=payload)
    # print (patch_response.text)
    #
    # #  Example code to test DELETE response
    # delete_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name/last.json'
    # delete_response = requests.delete(delete_endpoint)
    # print delete_response.text

    #-----------------------------------------------------------------------------------

    #  Sample Put request to add to/update FireBase Database

    # username = raw_input('Username: ')
    # name = raw_input('Name: ')
    # age = raw_input('Age: ')
    # put_endpoint = 'https://spoti.firebaseio.com/{}.json?auth={}'.format(username, my_api_key)
    # put_data = { "Name": name, "Age": age}
    # payload = json.dumps(put_data)
    # put_response = requests.put(put_endpoint, data=payload)
    # print (put_response.text)

    #  Sample GET request from a FireBase Database
    # username = 'Cloud'
    # get_endpoint = 'https://spoti.firebaseio.com/{}}.json?auth={}'.format(username, my_api_key)
    # get_response = requests.get(get_endpoint)
    # print (get_response.text)

    # message = "I love pie"
    # put_endpoint = 'https://material-fire.firebaseio.com/messages/-KCwhuRu6mppXjM8FIk3.json?auth={}'.format(my_api_key)
    # put_data = { "senderId": "2230f54c-5528-432b-8476-b82264eebf3a", "text": message}
    # payload = json.dumps(put_data)
    # put_response = requests.put(put_endpoint, data=payload)
    # print (put_response.text)

    UPC = raw_input('ENTER UPC: ')
    input_name = raw_input('ENTER NAME:')
    image_url = raw_input('IMAGE URL: ')


    put_endpoint = 'https://iofood.firebaseio.com/Items/{}/.json?auth={}'.format(UPC, my_api_key)
    put_data = { 'Name': input_name, 'Quanity': 10, 'image': image_url}
    payload = json.dumps(put_data)
    put_response = requests.put(put_endpoint, data=payload)

    # username = 'Cloud'
    # put_endpoint = 'https://iofood.firebaseio.com/.json?auth={}'.format(my_api_key)
    # get_response = requests.get(get_endpoint)
    # print (get_response.text)



if __name__ == "__main__":
    main()
