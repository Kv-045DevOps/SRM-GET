import os
import requests

def main():
    check_services()



def check_services():
    URL = "ui-service.production.svc:5000"
    req = request.get(URL)
    if req.status_code == 200:
        print("Tests successfull pass")
        continue
    else:
        raise Exception("F... b...!!!! Opssss")
        return 1
    URL_GET = "ui-service.production.svc:5000/salaries"
    reques = request.get(URL_GET)
    if reques.status_code == 200:
        print("Get req success to UI")
        return 0
    else:
        raise Exception("F... b... again!!!! Opssss")
        return -1
        
if __name__ == '__main__':
    main()

