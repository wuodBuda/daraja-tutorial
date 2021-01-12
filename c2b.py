import requests
from requests.auth import HTTPBasicAuth

from accessToken import generateAccessToken
import keys



def registerUrl():
    myAccessToken =generateAccessToken()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % myAccessToken}
    request = { "ShortCode": keys.shortCode,
                "ResponseType": "Completed",
                "ConfirmationURL": "https://fullstackdjnango.com/confirmation",
                "ValidationURL": "https://fullstackdjnango.com/validation_url"}

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

# registerUrl()

def simulateC2bTransaction():

    myAccessToken = generateAccessToken()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % myAccessToken}

    request = {"ShortCode": keys.shortCode,
               "CommandID": "CustomerPayBillOnline",
               "Amount": " ",
               "Msisdn": keys.TestMsisdn,
               "BillRefNumber": "34119905"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

simulateC2bTransaction()