
import requests
from pprint import pprint

def cliens():
    
    cred = {
        'username':'yenikayit22gmail.com',
        'password':'deneme123..',
        'profil': { 
        "foto": "http://127.0.0.1:8000/media/profil_fotolar%C4%B1/2022/09/hcetin_QweewBo.jpg",
        "token": "290197c9bf687062933bde406da65ae05a4b13e8",
        "phone": "0(532) 602 34 50",
        "birth_date": "1969-11-10",
        "tc": "20794617376",
        "iban": "TR",
        "bank": "Banka",
        "coin": "Bitcoin",
        "coin_adresi": "btc...",
        "info": {},}
        }
    
    
    token='3f3f5e672c6a2a19415ab681f0221eeec73ba169'
    headers = {
        "Content-Type":"application/json; charset=UTF-8",
        "Authorization":"Token " + token 
    }
    pprint(headers)
    url = 'http://127.0.0.1:8000/api/users/'
    response = requests.post(
        url,
        json=cred,
        headers=headers  
    )
    print('Response Statüs codu: ',response.status_code)
    
    print(response.json())
    
if __name__=='__main__':
    cliens()
    
    