import requests
from requests.auth import HTTPBasicAuth

import keys

def generateAccessToken():

    consumer_key = keys.consumerKey
    consumer_secret = keys.consumerSecret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # print(r.json())
    jsonResponse = r.json() #'access_token': 'GuL2t98eKJOGjPNeolscxVUjNMNK', 'expires_in': '3599'

    myAccessToken = jsonResponse['access_token']

    return myAccessToken