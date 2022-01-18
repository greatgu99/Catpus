from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
import requests
from Catpus import settings
from .models import Cat,CatLocation,CatColor
import os
from pathlib import Path
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.forms.models import model_to_dict
from django.core import serializers
from likes.models import LikeCat
from user.models import User


def addcat(request):
    data=request.params['data']
    cat=Cat()
    cat.catname = data['catname']
    cat.catpic = data['catpic']
    cat.catlike = 0

    # img = request.FILES.get('file')
    # if not img:
    #     return JsonResponse({'ret':0})
    # else:
    #     print(img.name)
    #     print(img.size)
    #     BASE_DIR = Path(__file__).resolve().parent.parent
    #     fileroot = os.path.join(BASE_DIR, 'media/img/').replace('\\', '/')
    #     path=default_storage.save('img/'+img.name,ContentFile(img.read()))
    #     tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    #     print(tmp_file)

    try:
        cat.catcolor = CatColor.objects.get(colorname=data['catcolor'])
        cat.catlocation = CatLocation.objects.get(locationname=data['catlocation'])
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        cat.save()
        print(cat.catcolor)
        print(cat.catlocation)
        print(cat.catname)
        print(cat.catpic)

        return JsonResponse({'ret': 0})

    # cat.catcolor = data['catcolor']
    # cat.catlocation =  data['catLocation']


def addpic(request):
    print("!!!!!!!!!!!!!!!!!!!")
    img = request.FILES.get('file')
    if not img:
        return JsonResponse({'ret': 1, 'msg': '请上传图片'})
    else:
        print(img.name)
        print(img.size)
        BASE_DIR = Path(__file__).resolve().parent.parent
        path=default_storage.save('img/'+img.name,ContentFile(img.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return JsonResponse({'ret':0,'tmp_file':img.name})

def getcat(request):
    cat_list=Cat.objects.all()
    # print(cat_list)
    res=[]
    for i in cat_list:
        res.append(model_to_dict(i))

    if 'page' in request.params:
        page=int(request.params['page'])
        res=res[(page-1)*10:page*10]
    # if 'personid' in request.params:
    #     print(request.params['personid'])
        # cat_list=Cat.objects.filter()


    # print(res)
    for i in res:
        i['catcolor']=CatColor.objects.get(id=i['catcolor']).colorname
        i['catlocation']=CatLocation.objects.get(id=i['catlocation']).locationname
        i['catpic']='http://127.0.0.1:8080/img/'+i['catpic']


    # print(res)
    # return JsonResponse({'ret':0,'cat_list':cat_list})
    return JsonResponse({'ret':0,'cat_list':res})

def getonecat(request):
    catid=request.params['catid']
    print(catid)
    res =  model_to_dict(Cat.objects.get(id=catid))


    res['catcolor'] = CatColor.objects.get(id=res['catcolor']).colorname
    res['catlocation'] = CatLocation.objects.get(id=res['catlocation']).locationname
    res['catpic'] = 'http://127.0.0.1:8080/img/' + res['catpic']
    print(res)
    return JsonResponse({'ret':0,'cat':res})
    # return JsonResponse({'ret': 0})

def getmylikecat(request):
    personid = request.params['personid']
    print(personid)
    person = User.objects.get(personid=personid)
    res =  LikeCat.objects.filter(person=person)
    cat_list = []
    for i in res:
        cat_list.append(model_to_dict(i.cat))

    for i in cat_list:
        i['catcolor']=CatColor.objects.get(id=i['catcolor']).colorname
        i['catlocation']=CatLocation.objects.get(id=i['catlocation']).locationname
        i['catpic']='http://127.0.0.1:8080/img/'+i['catpic']

    return JsonResponse({'ret': 0, 'cat_list': cat_list})


def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']

    print("!!!!!!!!!!")
    print((request.params))


    if action=='addcat':
        return addcat(request)
    elif action=='getcat':
        return getcat(request)
    elif action=='getonecat':
        return getonecat(request)
    elif action=='getmylikecat':
        return getmylikecat(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
    # return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})