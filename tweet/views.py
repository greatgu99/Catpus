import imp
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from .models import Tweet
# Create your views here.

def gettweet(request):
    tweet_list = Tweet.objects.all()

    res = []
    for i in tweet_list:
        res.append(model_to_dict(i))

    for i in res:
        # i['photo'] = 'https://catpus.top/media/tweet/' + i['photo']
        i['photo'] = 'http://127.0.0.1:8080/media/tweet/' + i['photo']

    return JsonResponse({'ret': 0, 'tweet_list': res})

def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']

    print((request.params))

    if action=='gettweet':
        return gettweet(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})