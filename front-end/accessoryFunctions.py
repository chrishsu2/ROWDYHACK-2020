import requests
import os
import shutil
#import loggingFile
# TODO: add log Decorators use functools etc
# TODO: find the end points
# TODO: init a dataCache instance. Cache data, 
def postData2Svr(data, URLEndPoint,method):
    ## need a wrapper to handle this
    ## without a wrapper cannot run async
    if method == "POST":
        response = requests.post(url=URLEndPoint,data=data)
    if method == "GET":
        response = requests.get(URLEndPoint,params=data)
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
