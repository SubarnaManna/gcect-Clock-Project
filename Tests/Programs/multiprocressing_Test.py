
# *************************** Without Multiprocessing ***************************
"""import time

def secs():
    print(time.time())
    time.sleep(1)
    secs()

def kity():
    print("My Kitt's Name is Lora.")

secs()
print("secs Activity is done.")
kity()"""

# *************************** After Multiprocessing ***************************
import multiprocessing as mp

import time

def secs():
    print(time.time())
    time.sleep(1)
    secs()

def kity():
    print("My Kitt's Name is Lora.")
    time.sleep(2)
    kity()


class student:
    def __init__(self,name):
        super().__init__()
        self.name = name

        pass

rohan = student("Rohan")


def Rn():
    print(rohan.name)
    rohan.name = "Subham"
    time.sleep(2)
    print(rohan.name)
    time.sleep(2)
    rohan.name = "Amit"
    print(rohan.name)
    time.sleep(1)
    Rn()

if __name__ == '__main__':


    p1 = mp.Process(target=secs)
    # secs()
    p1.start()
    p2 = mp.Process(target=kity)
    p2.start()

    time.sleep(4)
    print("secs Activity is done.")
    # kity()

    p3 = mp.Process(target=Rn)
    p3.start()