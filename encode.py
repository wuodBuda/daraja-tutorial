import base64

import keys

def generatePassword(formattedTime):

    dataToEncode = keys.businessShortcode + keys.lipaNaMpesaPasskey + formattedTime

    encodedString = base64.b64encode(dataToEncode.encode())
    #print(encodedString) b'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwMTExMTUxNTEw'

    decodedPassword = encodedString.decode('utf-8')

    return decodedPassword