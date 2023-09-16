# import socket   
# hostname=socket.gethostname()   
# IPAddr=socket.gethostbyname(hostname)   
# print("Your Computer Name is:"+hostname)   
# print("Your Computer IP Address is:"+IPAddr) 

from pythonping import ping
# ping('127.0.0.1', verbose=True)
# ping('www.google.com', verbose=True)
p1 = ping('8.8.8.8',verbose=True)
# p2 = ping('8.8.4.4',verbose=True)
m = str(p1).split("/")
# n = str(p2).split("/")
# print("p1 = ",p1)
print("p1 => ","Avg = ",m[len(m)-2],"Max = ",m[len(m)-1])
# print("p2 = ",p2)
# print("p2 = ",n[len(n)-2],n[len(n)-1])
import time
print(time.perf_counter())