import subprocess 
import csv 
import pandas as pd 
devices = subprocess.check_output("arp -a",shell=True)
extract_devices = devices.decode('utf-8')
#print(extract_devices.split("wlo1"))
devices_list = extract_devices.split("wlo1")
for i in range(0,len(devices_list)-1):
            print(devices_list[i].split(" "))
            origin_list = devices_list[i].split(" ")[0]
            getdata = devices_list[i].split(" ")[1]
            print(origin_list,getdata.split("(")[1].split(")")[0])
            

            #for r in range(0,len(getdata)):
            #       print(getdata[r])
                         
            

#devices_name = open("devicesname.csv",'w')
#devices_name.write(extract_devices) #Getting the extracted devices 
#read_devices = open("devicesname.csv",'r')
#read_devices.readlines()
#df = pd.read_csv('devicesname.csv')
#print(df)


