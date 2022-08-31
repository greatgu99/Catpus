from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import LikeMoments, LikeCat
from cat.models import Cat
from moments.models import Moments
from user.models import User
from utils.utils import *

# Create your views here.

def getlikecat(request):
    data = request.params['data']
    print(data)
    personid = data['personid']
    catid = data['catid']
    person = User.objects.get(personid=personid)
    cat = Cat.objects.get(id=catid)
    print(personid,catid)
    try:
        ans = LikeCat.objects.get(person=person, cat=cat)
    except BaseException:
        return JsonResponse({'ret': 0, 'catlike': False})
    else:
        return JsonResponse({'ret': 0, 'catlike': True})


def likecat(request):
    data = request.params['data']
    print(data)
    personid = data['personid']
    catid = data['catid']
    person = User.objects.get(personid=personid)
    # 此处也应用try except处理
    cat = Cat.objects.get(id=catid)
    print(personid, catid)
    cat.catlike = cat.catlike +1
    cat.save()

    print("调用了没啊调用了没啊调用了没啊调用了没啊调用了没啊")
    try:
        ans = LikeCat.objects.get(person=person, cat=cat)
    except BaseException:
        likecats = LikeCat()
        likecats.person=person
        likecats.cat=cat
        # cat的like数量加加
        likecats.save()
        print("保存成功保存成功保存成功保存成功保存成功保存成功保存成功")
        return JsonResponse({'ret': 0})
    else:
        return JsonResponse({'ret': 1})

def unlikecat(request):
    data = request.params['data']
    print(data)
    personid = data['personid']
    catid = data['catid']
    person = User.objects.get(personid=personid)
    # 此处也应用try except处理
    cat = Cat.objects.get(id=catid)
    cat.catlike = cat.catlike - 1
    cat.save()
    print(personid, catid)
    try:
        ans = LikeCat.objects.get(person=person, cat=cat)
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        ans.delete()
        return JsonResponse({'ret': 1})



def getlikemoments(request):
    data = request.params['data']
    print(data)
    personid = data['personid']
    momentsid = data['momentsid']
    person = User.objects.get(personid=personid)
    moments = Moments.objects.get(id=momentsid)
    print(personid,moments)
    try:
        ans = LikeMoments.objects.get(person=person, moments=moments)
    except BaseException:
        return JsonResponse({'ret': 0, 'momentslike': False})
    else:
        return JsonResponse({'ret': 0, 'momentslike': True})

def likemoments(request):
    data = request.params['data']
    print(data)
    personid = data['personid']
    momentsid = data['momentsid']
    person = User.objects.get(personid=personid)
    # 此处也应用try except处理
    moments = Moments.objects.get(id=momentsid)
    print(personid, momentsid)
    moments.like = moments.like + 1
    moments.save()
    try:
        ans = LikeMoments.objects.get(person=person, moments=moments)
    except BaseException:
        likemoments = LikeMoments()
        likemoments.person = person
        likemoments.moments = moments
        likemoments.save()
        return JsonResponse({'ret': 0})
    else:
        return JsonResponse({'ret': 1})

def unlikemoments(request):
    data = request.params['data']
    print(data)
    personid = data['personid']
    momentsid = data['momentsid']
    person = User.objects.get(personid=personid)
    # 此处也应用try except处理
    moments = Moments.objects.get(id=momentsid)
    print(personid, momentsid)
    moments.like = moments.like - 1
    moments.save()
    try:
        ans = LikeMoments.objects.get(person=person, moments=moments)
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        ans.delete()
        return JsonResponse({'ret': 1})



def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']
    print(action)
    if (not test_request(request)):
        return JsonResponse({'ret': 1, 'msg': '数据不合格'})

    if action == 'getlikecat':
        return getlikecat(request)
    elif action == 'getlikemoments':
        return getlikemoments(request)
    elif action == 'likecat':
        return likecat(request)
    elif action == 'likemoments':
        return likemoments(request)
    elif action == 'unlikecat':
        return unlikecat(request)
    elif action == 'unlikemoments':
        return unlikemoments(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
