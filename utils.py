from datetime import datetime

def getTimestamp():

    unformattedTime = datetime.now()
    formattedTime = unformattedTime.strftime("%Y%m%d%H%M%S")

    return formattedTime

