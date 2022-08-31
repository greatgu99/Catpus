from re import I
from time import time
from django.http import JsonResponse
import json
import time
import hmac
import base64
import hashlib
import json


def testurls(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    if 'data' in request.params:
        data=request.params['data']
        print(type(data))
        data = eval(data)
        print(data)
        S=''
        for i in data:
            print(i)
            if (i == 'hashCode'):
                continue
            S = S + i
            S = S + str(data[i])
        print(S)
        SecretKey = 'rOWh1msXOsxLYu5xY0NtFVmcKVGntqLPTFNZ2gDy'
        bytesToSign = S
        bytesToSign = bytes(bytesToSign.encode('utf-8'))
        SecretKey = bytes(SecretKey.encode('utf-8'))
        dig = hmac.new(SecretKey, bytesToSign, digestmod=hashlib.sha256).digest()
        sign = base64.b64encode(dig)
        
        # sign = sign[2:len(sign)-1]
        sign = str(sign)
        print(type(sign))
        sign = sign[2:-1]
        print(sign)
        print(sign == data['hashCode'])
        # return (sign == data['hashCode'])
        return JsonResponse({'data':data,'method':request.method})
    else:
        return True
