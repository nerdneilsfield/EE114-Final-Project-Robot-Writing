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
        self.ser = Serial(port,9600,timeout=0.005)
        reading = str(self.ser.read(100),'utf-8')+"\n"
        print(reading)
        self.run([80,130,150,170])
        return reading
    def run(self,angles):
        for i in range(4):
            self.command = bytes(str(i+1)+hello(angles[i]),'utf-8');
            self.ser.write(self.command)
            print(self.command)
            sleep(0.06)
        return "hello"
    def test(self):
        #self.ser.write(bytes("p","utf-8"))
        reading = str(self.ser.read(100),'utf-8')+"\n"
        print(reading)
        return reading
    def demo(self):
        i = 9;
        while(i):
            self.run([0,15,30,30])
            sleep(1)
            self.run([40, 30, 40, 30])
            sleep(1)
            i-=1

    def close(self):
        self.ser.close()