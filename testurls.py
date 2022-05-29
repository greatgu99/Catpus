from socket import socket
import  requests
import http.client
import urllib
import json
def send_request(host, path, method, port=443, params={}):
    client = http.client.HTTPSConnection(host, port,timeout=1)
    path = '?'.join([path, urllib.parse.urlencode(params)])
    try:

        client.request(method, path)
        res = client.getresponse()
    except Exception:
        return [False,]
    else:
        


        if not res.status == 200:
            return False, res.status

        return True, json.loads(res.read())

if __name__=="__main__":
    print(1)
    params = {
        'grant_type': 'client_credential',
        'appid': 'wx6686a216a78b3702',
        'secret': '6590de016b1a1b18a830edb5b6d57d45'
    }
    host = 'api.weixin.qq.com'
    path = '/cgi-bin/token'
    method = 'GET'
    res = send_request(host, path, method, params=params)
    if not res[0]:
        pass
        # return False
    if res[1].get('errcode'):
        pass
        # return False
    # return res[1]
    print(res)
    print(2)