import os
import requests

def main():
    check_services()



def check_services():
    URL = "http://ui-service.production.svc:5000/"
    req = requests.get(URL)
    if req.status_code == 200:
        print("Tests UI successfull pass")
    else:
        raise Exception("Fucking bitch!!!! Opssss")
    URL_GET = "http://ui-service.production.svc:5000/salaries"
    reques = requests.get(URL_GET)
    if reques.status_code == 200:
        print("Test success to UI-GET/salaries")
    else:
        print(reques.status_code)
        raise Exception("Fucking bitch again!!!! Opssss. You are ....")
        
if __name__ == '__main__':
    main()
