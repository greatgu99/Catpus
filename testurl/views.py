from time import time
from django.http import JsonResponse
import json
import time
def testurls(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    print(11111)
    time.sleep(5)
    print(22222)
    return JsonResponse({'data':request.params,'method':request.method})
