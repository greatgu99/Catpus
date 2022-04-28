from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from .models import Moments
from cat.models import Cat,CatColor
from user.models import User
# Create your views here.

def getmoments(request):
    if 'data' in request.params:
        if 'personid' in request.params['data']:
            personid=request.params['data']['personid']
            person = User.objects.get(personid=personid)
            moments_list = Moments.objects.filter(person=person)
        elif 'catid' in request.params['data']:
            catid = request.params['data']['catid']
            cat = Cat.objects.get(id=catid)
            moments_list = Moments.objects.filter(cat=cat)
            print('*-/*-*/*-/*-/*/-*/*--/-*/*-/-*/')
            print(moments_list)
    else:
        moments_list = Moments.objects.all()

    res = []
    for i in moments_list:
        res.append(model_to_dict(i))

    for i in res:
        i['cat'] = model_to_dict(Cat.objects.get(id=i['cat']))
        i['person'] = model_to_dict(User.objects.get(id=i['person']))
        i['pic'] = 'https://catpus.top/media/img/' + i['pic']
        i['cat']['catpic'] = 'https://catpus.top/media/img/' + i['cat']['catpic']
        i['cat']['catcolor']=CatColor.objects.get(id=i['cat']['catcolor']).colorname
        # i['cat'] = model_to_dict(i['cat'])
        # i['person'] = model_to_dict(i['person'])

    return JsonResponse({'ret': 0, 'moments_list': res})


def addmoments(request):
    data=request.params['data']
    moments=Moments()
    moments.person= User.objects.get(personid=data['personid'])
    moments.cat = Cat.objects.get(id=data['catid'])
    moments.content = data['content']
    moments.pic = data['pic']
    moments.like = 0
    moments.save()
    print(moments.person)
    print(moments.cat)
    print(moments.content)
    print(moments.pic)
    return JsonResponse({'ret': 0})


def delmoments(request):
    data = request.params['data']
    try:
        moments = Moments.objects.get(id=data['momentsid'])
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        moments.delete()
        return JsonResponse({'ret': 0})

def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']

    print((request.params))


    if action=='addmoments':
        return addmoments(request)
    elif action=='getmoments':
        return getmoments(request)
    elif action=='delmoments':
        return delmoments(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})