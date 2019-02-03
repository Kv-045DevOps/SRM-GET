import os
import time
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
        
if __name__ == '__main__':
    main()
