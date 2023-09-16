import time
# print(time.time())
# print(int(time.time()))

# from WorldTimeAPI import  services as serv

# myclient = serv.client('timezone')
# requests = {"area":"America","location":"New_York"}

# # Returns a DateTimeJSON object
# response = myclient.get(**requests)

# print(response.datetime)

# regions = myclient.regions()
# print(regions.data)

# timeZone_info = {
    # "Location":""
# }
import requests
global curl
# curl =  "http://worldtimeapi.org/api/timezone/Asia/Kolkata"
# curl =  "http://worldtimeapi.org/api/timezone/Asia/Kolkata.txt"
# import socket
# IPaddress=socket.gethostbyname(socket.gethostname())
# if IPaddress=="127.0.0.1":
#     print("No internet, your localhost is "+ IPaddress)
# else:
#     # curl =  "http://worldtimeapi.org/api/ip"
#     # r = requests.get(curl)
#     # received_Data = r.json()
#     # print(received_Data)
#     # print("Unix Time = ", received_Data['unixtime'])    
#     print("Connected, with the IP address: "+ IPaddress )

import urllib.request

def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False

print( 'connected' if connect() else 'no internet!' )

if connect():
    curl =  "http://worldtimeapi.org/api/ip"
    r = requests.get(curl)
    received_Data = r.json()
    unixTime = received_Data['unixtime']


# try : 
#     # global curl

# finally:
#     print('Not Connected !')