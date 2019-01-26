import os
import sys

with open(sys.argv[1], 'r') as file:
    arr_s = sys.argv[2].split(',')
    print(arr_s)
    str_tmp = "ghostgoose"
    arr_f = ["100.71.71.71:5000/get-service", "100.71.71.71:5000/post-service", "100.71.71.71:5000/ui-service", "100.71.71.71:5000/db-service", "100.71.71.71:5000/init-container"]
    arr = ["100.71.71.71:5000/get-service:v2", "100.71.71.71:5000/post-service:2.1", "100.71.71.71:5000/ui-service:latest", "100.71.71.71:5000/db-service:latest", "100.71.71.71:5000/init-container:latest"]
    data = file.read()
    print(len(arr_f))
    for i in range(len(arr_f)):
        tmp = arr_f[i] + ":" + arr_s[i]
        data = data.replace(arr[i], tmp)
    
    print(data)
         

with open(sys.argv[1], 'w') as file:
    file.write( data )
