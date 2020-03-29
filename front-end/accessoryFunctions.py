import requests
from flask import jsonify
#import loggingFile
# TODO: add log Decorators use functools etc
# TODO: find the end points
# TODO: init a dataCache instance. Cache data,
def sendData2Svr(payload, URLEndPoint,method):
    ## need a wrapper to handle this
    ## without a wrapper cannot run async
    if method == "POST":
        response = requests.post(url=URLEndPoint,data=payload)
    if method == "GET":
        response = requests.get(URLEndPoint,params=payload)
    return response

class dataCache:
    """"supposedly hold the data,
    need this class to empty response data if client switches screens or searches
    """

    #will probably have json data
    cache=[]
    def __init__(self,):
        ## set up class
        return
    def deleteCache(self):
        self.cache=[]
        return



def getBackendResponse(payload, URLEndPoint):
    response = requests.get(url=URLEndPoint, params=payload)
    return response
