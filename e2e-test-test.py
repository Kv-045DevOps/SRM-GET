import os
import requests

def main():
    check_services()



def check_services():
    URL = "ui-service.testing.svc:5000"
    req = requests.get(URL)
    if req.status_code == 200:
        print("Tests successfull pass")
        continue
    else:
        raise Exception("Fucking bitch!!!! Opssss")
        return 1
    URL_GET = "ui-service.testing.svc:5000/salaries"
    reques = requests.get(URL_GET)
    if reques.status_code == 200:
        print("Get req success to UI")
        return 0
    else:
        raise Exception("Fucking bitch again!!!! Opssss. You are unclever animal")
        return -1
        
if __name__ == '__main__':
    main()
