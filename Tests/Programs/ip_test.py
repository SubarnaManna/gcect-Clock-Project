import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+IPAddr) 

import json ,time , requests




def Set_Network_Time():
    pass

def Fetch_Time():
    try : 
        req = requests.get(url='http://worldtimeapi.org/api/ip',timeout=3)
        if req.status_code == 200 :
            data = json.loads(req.text)
            print(data['datetime'])
    except:
        print("No Connection")
        time.sleep(3)
        Fetch_Time()

Fetch_Time()