#!/bin/python3 
from serial import Serial
from time import sleep 

def hello(s):
    if s >= 100: return str(s)
    if s < 100 and s >=10: return "0"+str(s)
    if s<10: return "00"+str(s)

class arm(object):
    def __init__(self):
        pass
    def connect(self,port):
        self.ser = Serial(port,9600,timeout=1)
        reading = str(self.ser.read(100),'utf-8')+"\n"
        print(reading)
        return reading
    def run(self,a,b,c,d):
        self.command = bytes(
            "1"+hello(a) +
            "2"+hello(b) + 
            "3"+hello(c) +
            "4"+hello(d), "utf-8"
        )
        self.ser.write(self.command)
        reading = str(self.ser.read(100),'utf-8')+"\n"
        print(reading)
        return reading
        sleep(0.1)
    def test(self):
        self.ser.write(bytes("p","utf-8"))
        reading = str(self.ser.read(100),'utf-8')+"\n"
        print(reading)
        return reading
    def demo(self):
        i = 9;
        while(i):
            self.run(0,15,180,170)
            sleep(1)
            self.run(180, 165, 0, 0)
            sleep(1)
            i-=1

    def close(self):
        self.ser.close()