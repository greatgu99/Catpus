from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
import requests
from Catpus import settings
from .models import User

def login(request):
    print(request)
    data=request.params['data']
    user = User()
    try:
        user1 = User.objects.get(personid=data['personid'])
    except User.DoesNotExist:
        pass
    else:
        user=user1
    user.personid = data['personid']
    user.avatarurl = data['avatarUrl']
    user.city = data['city']
    user.country = data['country']
    user.gender = data['gender']
    user.nickname = data['nickName']
    user.province = data['province']

    print(user)
    print(user.personid)
    print(user.nickname)
    user.save()
    return JsonResponse({'ret': 0})

def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    action = request.params['action']
    if action == 'login':
        return login(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})





    # request.params = json.loget_response(request)ads(request.body)
    # print(request.params)
    #
    # action = request.params['action']
    #
    # if action == 'add_cat':
    #     return addcat(request)
    # elif action == 'add_customer':
    #     return addcustomer(request)
    # elif action == 'modify_customer':
    #     return modifycustomer(request)
    # elif action == 'del_customer':
    #     return deletecustomer(request)

    # else:
        # return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
        # return HttpResponse("下面是系统中所有的订单信息。。。")

def testurl(request):
    pass