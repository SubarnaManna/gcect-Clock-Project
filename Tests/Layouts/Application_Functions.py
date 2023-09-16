from datetime import datetime, date, timedelta
# from pythonping import ping
# import urllib.request
import time, json, requests, os

# **************** Important Functions ***************** 

path = 'Exam_Time_Info.json'

file_Path = image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Img")

# **************** Custom Time Managementing Function ****************

def zero(n):
    n = int(n)
    if n<10 and n>-1 :
        return '0'+str(n)
    else:
        return str(n)
    
def hour12(n):
    n = int(n)
    n = n%12
    if n == 0 :
        n = 12
    return str(n)

def ampm(n):
    n = int(n)
    hr=n//12
    if hr==0:
        return "AM"
    else:
        return "PM"

def weekday(n):
    n = int(n)
    Days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return Days[n]

Months = ['January','February','March','April','May','June','July','August','September','October','November','December']

def Month(n):
    n = int(n)
    return Months[n-1]
    
def set_Exam_Dates():
    T = time.localtime()
    DateArray = []
    for i in range(1,4):
        today = date.today()
        Enddate = today + timedelta(days=i)
        day = Enddate.strftime("%d")
        month = Enddate.strftime("%B")
        year=Enddate.strftime("%Y")
        datec = day+'-'+month+'-'+year
        DateArray.append(datec)
    return DateArray


# **************** OPENing Exam Records ****************

def get_Exam_Records():
    with open(path,"r") as f:
        Exam_Records = json.load(f)
        f.close()
        return Exam_Records

# **************** Managing Network Connections ****************

def getConnectionValue():
    with open("conn_data.json",'r') as f :
        Dataset = json.load(f)
    f.close()
    conn=Dataset['conn_Status']
    return int(conn)

# **************** Network Connection Method 02 ****************
def connect_via_url():
    try:
        # urllib.request.urlopen('http://google.com') #Python 3.x
        requests.head(url='https://google.com',timeout=4)
        # requests.get(url='https://google.com',timeout=2)
        # print("Fine")
        return True
    except:
        # print("Not Fine")
        return False

def Set_Network_Time():
    pass

# **************** Network Connection Method 03 ****************
def return_Online():
    try : 
        requests.get(url='https://google.com',timeout=2)
        return True
    except:
        # print("No Connection")
        time.sleep(3)
        return_Online()

# **************** Fetching Network Time ****************

def Fetch_Time():
    try : 
        req = requests.get(url='http://worldtimeapi.org/api/ip',timeout=3)
        if req.status_code == 200 :
            data = json.loads(req.text)
            d = {"DateTime":data['datetime'],"UnixTime":data['unixtime']}
            print(d)
            return d
    except:
        print("No Connection")
        time.sleep(3)
        Fetch_Time()

# Fetch_Time()

def NewConnect():
#   The Execution Time for this Function is Maximum 4 sec Approx   

# **************** Method 01 ****************
    # p1 = ping('8.8.8.8')
    # m = str(p1).split("/")
    # n1 = int(float(m[len(m)-2]))
    # n2 = int(float(m[len(m)-1].split(" ")[0]))
    # print(" n1 = ",n1 ," | ","n2 = ",n2)
    # # if n1==n2 :
# **************** Method 02 ****************
    if connect_via_url()==False:
        data = {"conn_Status":"0"}
    else:
        data = {"conn_Status":"1"}
    with open("conn_data.json",'w')as f:
        json.dump(data,f)
        f.close()
    time.sleep(4)
    NewConnect()


#  **************** Returns Main UNIX Time for UPLOADING in Arduino **************** 
def get_Epoch(year,month,date,hour24,Minutes):

    # input datetime
    dt = datetime(year, month, date, hour24, Minutes)
    # epoch time
    epoch_time = datetime(1970, 1, 1)

    # subtract Datetime from epoch datetime
    delta = (dt - epoch_time)
    # print('Datetime to Seconds since epoch:', delta.total_seconds())
    return int(delta.total_seconds())

# print(get_Epoch(2023,4,6,0,24))