# from django.shortcuts import render
#
# # Create your views here.\
# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# import json
# from django.http import HttpResponse
# import requests
# from Catpus import settings
# from . models import  Cat,CatColor
# import os
# from pathlib import Path
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
#
# def addcat(request):
#     print(request)
#     print(request.params['data'])
#     info = request.params['data']
#     catcolor=request.params['data']['CatColor']
#     # catcolor= CatColor.objects.get(ColorName=request.params['data']['CatColor'])
#     CatColorlist = CatColor.objects.values()
#     print(CatColorlist)
#     for i in range(len(CatColorlist)):
#         if (CatColorlist[i]['ColorName']==catcolor):
#             print('!!!!!!!!!!!')
#             print(i)
#             break
#     print(i)
#     i=i+1
#
#     Cat.objects.create(CatName=info['CatName'],
#                        CatLocation=info['CatLocation'],
#                        CatColor_id=i)
#     return JsonResponse({'ret': 0})
#
# def catlist(request):
#     print("!!!!!!!!!!!!!!!")
#     Catlist = Cat.objects.values()
#     CatColorlist = CatColor.objects.values()
#     retlist=[]
#     for i in range(len(Catlist)):
#         t=dict()
#         t['id']=Catlist[i]['id']
#         t['CatName'] = Catlist[i]['CatName']
#         t['CatColor_id'] = Catlist[i]['CatColor_id']
#         t['CatLocation'] = Catlist[i]['CatLocation']
#         t['CatColor'] = CatColorlist[t['CatColor_id']-1]['ColorName']
#         retlist.append(t)
#
#     print(retlist)
#
#
#     return JsonResponse({'ret': 0, 'retlist': retlist})
#
# def testpic(request):
#     img=request.FILES.get('file')
#     if not img:
#         return JsonResponse({'ret':0})
#     else:
#         print(img.name)
#         print(img.size)
#         BASE_DIR = Path(__file__).resolve().parent.parent
#         fileroot = os.path.join(BASE_DIR, 'media/img/').replace('\\', '/')
#         path=default_storage.save('img/'+img.name,ContentFile(img.read()))
#         tmp_file = os.path.join(settings.MEDIA_ROOT, path)
#         print(tmp_file)
#         return JsonResponse({'ret':1})
#
# def dispatcher(request):
#     # if request.method == 'GET':
#     #     request.params = request.GET
#     #
#     #     # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
#     # elif request.method in ['POST', 'PUT', 'DELETE']:
#     #     # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
#     #     request.params = json.loads(request.body)
#     # return addcat(request)
#
#     return testpic(request)
#
#
#
#
#     # request.params = json.loget_response(request)ads(request.body)
#     # print(request.params)
#     #
#     # action = request.params['action']
#     #
#     # if action == 'add_cat':
#     #     return addcat(request)
#     # elif action == 'add_customer':
#     #     return addcustomer(request)
#     # elif action == 'modify_customer':
#     #     return modifycustomer(request)
#     # elif action == 'del_customer':
#     #     return deletecustomer(request)
#
#     # else:
#         # return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
#         # return HttpResponse("下面是系统中所有的订单信息。。。")
#
# # def testurl(request):
# #     response = requests.get("https://n.sinaimg.cn/blog/175/w105h70/20210615/74b6-krpikqf1152851.jpg")
# #     print("!!!!!!!!!!!@@@@@@@@@@@@@@@@@")
# #     print(response)
# #     fileurl = request.GET.__getitem__('filepath')
# #     print(fileurl)
# #     response = requests.get(fileurl)
# #     print(response)
# #     return JsonResponse({'ret': 1, 'msg0': '啦啦啦', 'data': request.GET})
#     # return JsonResponse({'ret':1,'msg0':'啦啦啦','data':request.GET,'response':response})
#
#
