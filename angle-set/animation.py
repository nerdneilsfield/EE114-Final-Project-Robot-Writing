#!/bin/env python3

from arm import arm
import serial.tools.list_ports
from time import sleep

newbee = arm()

def connect():
    ports = serial.tools.list_ports.comports()
    ports_str = [str(i) for i in ports]
    print("Ports are?\n")
    for i in range(len(ports_str)):
        print(str(i)+"."+ports_str[i])
    chose = int(input("chose some?"))
    if chose < len(ports):
        newbee.connect(ports_str[i].split("-")[0].replace(" ",""))
    else:
        print("wrong input")

def write(datas):
    newbee.run(datas[:4])
    sleep(datas[4]/1000)

def draw(files):
    f  = open(files,'r')
    ha = f.readlines()
    for i in ha:
        datas = [int(j) for j in i.split()]
        write(datas)


connect()

files = input("file?")
draw(files)
