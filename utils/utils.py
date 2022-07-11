from socket import socket
from urllib import response
import  requests
import http.client
import urllib
import json

def send_request(host, path, method, port=443, params={}):
    try:
        client = http.client.HTTPSConnection(host, port,timeout=1)
        if method == 'GET':
            client.request(method, path)
        else :
            client.request(method, path, params)
        res = client.getresponse()
    except Exception:
        return [False,]
    else:
        if not res.status == 200:
            return False, res.status
        return True, json.loads(res.read())

def get_access_token():
    params = {
        'grant_type': 'client_credential',
        'appid': 'wx6686a216a78b3702',
        'secret': '6590de016b1a1b18a830edb5b6d57d45'
    }
    host = 'api.weixin.qq.com'
    path = '/cgi-bin/token'
    path = '?'.join([path, urllib.parse.urlencode(params)])
    method = 'GET'
    res = send_request(host, path, method)
    if not res[0]:
        return False
    if res[1].get('errcode'):
        return False
    return res[1]

# def msg_sec_check(content):
#     print(1)
#     access_token = get_access_token()
#     print(access_token)
#     if not access_token:
#         return False
#     access_token = access_token['access_token']

#     params = {'content': content.encode("utf-8").decode("latin-1")}
#     host = 'api.weixin.qq.com'
#     path = '/wxa/msg_sec_check?access_token='+access_token
#     method = 'POST'
#     res = send_request(host, path, method, params=json.dumps(params,ensure_ascii=False))
#     print(res)
#     return res

def msg_sec_check(msg):
    access_token = get_access_token()
    print(access_token)
    if not access_token:
        return False
    access_token = access_token['access_token']
    url = "https://api.weixin.qq.com/wxa/msg_sec_check?access_token=" + access_token
    data = {'content': msg.encode("utf-8").decode("latin-1")}
    return_value = requests.post(url=url, data=json.dumps(data,ensure_ascii=False))
    return_value_json = return_value.json()
    print(return_value_json)
    errcode = return_value_json['errcode']
    # errmsg = return_value_json['errmsg']
    if errcode == 0:
        return True
    if errcode == 87014:
        return False

def img_sec_check(img):
    print(1)
    access_token = get_access_token()
    print(access_token)
    if not access_token:
        return False
    access_token = access_token['access_token']
    url = "https://api.weixin.qq.com/wxa/img_sec_check?access_token=" + access_token
    headers = {"Content-Type":"multipart/form-data"}
    post_files = {"media": img}
    response = requests.post(url=url,
                             files=post_files,
                             headers=headers)
    response.encoding = 'utf-8' # 設置可接收的編碼為 utf-8
    responseDict = eval(response.text)
    print(responseDict)
    errcode = responseDict['errcode']
    # errmsg = return_value_json['errmsg']
    if errcode == 0:
        return True
    if errcode == 87014:
        return False

def get_openid(code):
    params = {
        'appid': 'wx6686a216a78b3702',
        'secret': '6590de016b1a1b18a830edb5b6d57d45',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    host = 'api.weixin.qq.com'
    path = '/sns/jscode2session'
    path = '?'.join([path, urllib.parse.urlencode(params)])
    method = 'GET'
    res = send_request(host, path, method)
    print(res)
    if not res[0]:
        return False
    if res[1].get('errorcode') and res[1].get('errorcode') != 0:
        return False
    if res[1].get('openid'):
        return res[1].get('openid')
    return False

if __name__ == '__main__':
    print(get_openid('073kMZZv3QH2QY2qNp1w3YcPIf2kMZZp'))
    # msg_sec_check('xidada')

    # msgSecCheck('特3456书yuuo莞6543李zxcz蒜7782法fgnv级 完2347全dfji试3726测asad感3847知qwez到')