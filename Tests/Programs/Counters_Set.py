
DurationSet=["10 minutes","15 minutes","30 minutes","45 minutes","1 hour","1 hour 15 minutes","1 hour 30 minutes","1 hour 45 minutes","2 hours","2 hours 15 minutes",
        "2 hours 30minutes","2 hours 45 minutes","3 hours","3 hours 15 minutes","3 hours 30 minutes","3 hours 45 minutes","4 hours","4 hours 15 minutes"]
Exam_Time = ["07 : 30 AM ","07 : 45 AM ","08 : 00 AM ","08 : 15 AM ","08 : 30 AM ","08 : 45 AM ","09 : 00 AM ","09 : 15 AM ","09 : 30 AM ","09 : 45 AM ","10 : 00 AM ","10 : 15 AM ","10 : 30 AM ", "10 : 45 AM ","11 : 00 AM ","11 : 15 AM ","11 : 30 AM ","11 : 45 AM ","12 : 00 PM ","12 : 15 PM ","12 : 30 PM ","12 : 45 PM ","01 : 00 PM ","01 : 15 PM ","01 : 30 PM ","01 : 45 PM ","02 : 00 PM ","02 : 15 PM ","02 : 30 PM ","02 : 45 PM ","03 : 00 PM ","03 : 15 PM ","03 : 30 PM ","03 : 45 PM ","04 : 00 PM ","04 : 15 PM ","04 : 30 PM ","04 : 45 PM ","05 : 00 PM ","05 : 15 PM","05 : 30 PM"]

def seconds_Set():
    for i in range(1,len(DurationSet)):
        print(DurationSet[i],'= ',i*15*60,'Seconds')

def seconds():
    for i in range(1,len(DurationSet)):
        print(f"\"{i*15*60}\",",end='')

# seconds_Set()
# seconds()

# def zero(i):
    # if i<10:
        # return "0"+str(i)

# def exam_time():
    # for i in range(9,15):
        # print(f"\"{zero(i)}\",")