
import requests
from pprint import pprint

def cliens():
    
    cred = {
        'username':'cap002@gmail.com',
        'password':'deneme123..'
    }
    token='Token 48cb29f40a021609594f2d845d50de8a6b79c073'
    headers = {
        #"Content-Type": "application/json; charset=UTF-8",
        #'Content-Type': 'multipart/form-data',
        "Authorization": 'Token 48cb29f40a021609594f2d845d50de8a6b79c073'
    }
    pprint(headers)
    url = 'http://127.0.0.1:8000/profil/'
    response = requests.get(
        url = url,
        #data=cred,
        headers=headers  
    )
    print('Response Statüs codu: ',response.status_code)
    
    pprint(response.json())
    
if __name__=='__main__':
    cliens()
    
    