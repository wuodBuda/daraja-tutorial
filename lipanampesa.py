import requests
from requests.auth import HTTPBasicAuth


from accessToken import generateAccessToken
from encode import generatePassword
from utils import getTimestamp
import keys


def lipaNaMpesa():

    formattedTime = getTimestamp()

    decodedPassword = generatePassword(formattedTime)

    access_token = generateAccessToken()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": keys.businessShortcode,
        "Password": decodedPassword,
        "Timestamp": formattedTime,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phoneNumber,
        "PartyB": keys.businessShortcode,
        "PhoneNumber": keys.phoneNumber,
        "CallBackURL": "https://fullstackdjnango.com/lipanampesa",
        "AccountReference": "Barry osewe",
        "TransactionDesc": "Pay School Fees"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

lipaNaMpesa()
