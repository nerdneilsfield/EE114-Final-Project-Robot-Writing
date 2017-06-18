#!/bin/env python3

from  arm import arm
import tkinter as tk
import serial.tools.list_ports
class Appication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.data = {}
        self.pack()
        self.create_widgets()
        self.data["an1"] = 45
        self.data["an2"] = 45
        self.data["an3"] = 45
        self.data["an4"] = 45
    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "FUck you\n(Come on)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        self.arm = arm()
        self.text5 = tk.Label(self,text="Port")
        self.text5.pack()
        self.port = tk.Entry(self)
        self.port.pack()
        self.listport = tk.Button(self,text="list all port",command=self.listportFun,fg="red")
        self.listport.pack()
        self.connect = tk.Button(self,text="connect",command=self.connectFun,fg="red")
        self.connect.pack()
        self.disconnect = tk.Button(self,text="disconnect",command=self.disConnetctFun,fg="red")
        self.disconnect.pack()
        self.testconnect = tk.Button(self,text="testconnect",command=self.testconnectFun,fg="red")
        self.testconnect.pack()
        self.text1 = tk.Label(self,text="Angle1")
        self.text1.pack()
        self.an1 = tk.Entry(self)
        self.an1.pack()
        self.text2 = tk.Label(self,text="Angle2")
        self.text2.pack()
        self.an2 = tk.Entry(self)
        self.an2.pack()
        self.text3 = tk.Label(self,text="Angle3")
        self.text3.pack()
        self.an3 = tk.Entry(self)
        self.an3.pack()
        self.text4 = tk.Label(self,text="Angle4")
        self.text4.pack()
        self.an4 = tk.Entry(self)
        self.an4.pack()
        self.setButton = tk.Button(self,text="Set",command=self.setFun,fg="red")
        self.setButton.pack()
        self.showinfo = tk.Text(self)
        self.showinfo.pack()
        self.quit = tk.Button(self, text="Quit",fg = "red",command=root.destroy)
        self.quit.pack(side="bottom")
    def connectFun(self):
        port = self.port.get()
        if port :
            self.data["port"] = self.port.get()
            self.showinfo.insert("end","Try to connect"+self.data["port"]+"\n")
            reading  = self.arm.connect(self.data["port"])
            self.showinfo.insert("end",reading)
        else:
            self.showinfo.insert("end","Please input the port\n")
    def disConnetctFun(self):
        reading = self.arm.close()
        self.showinfo.insert("end",reading)
    def testconnectFun(self):
        reading = self.arm.test()
        self.showinfo.insert("end",reading)
    def setFun(self):
        self.data["an1"] = int(self.an1.get()) or self.data["an1"]
        self.data["an2"] = int(self.an2.get()) or self.data["an2"]
        self.data["an3"] = int(self.an3.get()) or self.data["an3"]
        self.data["an4"] = int(self.an4.get()) or self.data["an4"]
        if self.data["an1"] >=  0 and  self.data["an1"] <= 180 and  \
            self.data["an2"] >=  15 and  self.data["an1"] <= 165 and \
            self.data["an1"] >= 0 and  self.data["an1"] <= 180 and \
            self.data["an1"] >=  0 and  self.data["an1"] <= 180:
            reading = self.arm.run(self.data["an1"], self.data["an2"], self.data["an3"], self.data["an4"])
            self.showinfo.insert("end",reading)
        else:
            self.showinfo.insert("end","Wrong input\n")
    def listportFun(self):
        reading = serial.tools.list_ports.comports()
        self.showinfo.insert("end","\n".join([str(i) for i in reading])+"\n")
        
root = tk.Tk()
app = Appication(master=root)
app.master.title("GUI Angle Config Tool")
app.mainloop()
