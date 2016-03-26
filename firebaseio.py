import requests
import json
import urllib2
import simplejson
my_api_key = "rKxaoEeEqWGh5CLFvMBmK5pEv9WeYA2aZEswJFnX"
auth_API = '?auth={}'.format(my_api_key)
url_base = 'https://iofood.firebaseio.com'

def main():
    #  Example code to test GET response
    # get_endpoint = 'https://samplechat.firebaseio-demo.com/users/jack/name.json'
    # get_response = requests.get(get_endpoint)
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
    UPC.replace(" ","+")
    objectSearch = "http://www.searchupc.com/handlers/upcsearch.ashx?request_type=3&access_token=B477A55B-D092-4627-9820-5C80A25FCDF1&upc={}".format(UPC)
    search_ = requests.get(objectSearch)
    myJSON = json.loads(search_.text)
    productName_ = (myJSON['0']['productname'])
    imageURL_ = (myJSON['0']['imageurl'])
    #print(search_.text)

# Process the JSON string.
#results = simplejson.load(response)
# now have some fun with the results...
#    put_endpoint = 'https://iofood.firebaseio.com/Items/{}/.json?auth={}'.format(UPC, my_api_key)
#    put_data = { "Name": productName_, "Image URL": imageURL_}
#    payload = json.dumps(put_data)
#    put_response = requests.put(put_endpoint, data=payload)

#3     username = 'Cloud'
#     put_endpoint = 'https://iofood.firebaseio.com/.json?auth={}'.format(my_api_key)
#     get_response = requests.get(get_endpoint)
#     print (get_response.text)



if __name__ == "__main__":
    main()
