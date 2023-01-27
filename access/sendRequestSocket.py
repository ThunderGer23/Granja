# * Importing the json module and renaming it to ujson.
import json as ujson

def sendRequest(req, requests):
    """
    It takes a request object, and sends it to the url specified in the request object
    
    :param req: The request object
    :param requests: a list of requests to send
    :return: The response from the server.
    """
    token = req["token"]
    message = req['message']
    url = req['url']
    request = {'token': token,'message': message}
    post_data = ujson.dumps(request).encode('utf8')
    print("\n\n",str(post_data),"\n\n")
    res = requests.post(url,headers = {'content-type': 'application/json'},data=post_data)
    return res.text