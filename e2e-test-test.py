import os
import requests
import time

def main():
    check_services()



def check_services():
    URL = "http://ui-service.testing.svc:5000"
    req = requests.get(URL)
    if req.status_code == 200:
        print("Test UI successfull pass")
    else:
        raise Exception("Fucking bitch!!!! Opssss")
#    URL_GET = "http://ui-service.testing.svc:5000/salaries"
#    time.sleep(5)
#    reques = requests.get(URL_GET)
#    if reques.status_code == 200:
#        print("UI success to GET")
#    else:
#        raise Exception("Fucking bitch again!!!! Opssss. You are unclever animal")
        
if __name__ == '__main__':
    main()
