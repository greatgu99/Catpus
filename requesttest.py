import  requests,pprint
#
# payload = {
#     "action":"addcat",
#     "data":{
#         "CatName":"白猫",
#         "CatLocation":"打篮球",
#         "CatColor":"黄"
#     }
# }
# response = requests.post('http://localhost:8080/test/',json=payload)
# print(response)
#
#
# pprint.pprint(response.json())
#
#
payload = {
    "action":"addcat",
    "data":{
        "CatName":"白猫",
        "CatLocation":"打篮球",
        "CatColor":"绿"
    }
}
response = requests.post('http://localhost:8080/test/',json=payload)
print(response)


pprint.pprint(response.json())

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
print(MEDIA_ROOT)