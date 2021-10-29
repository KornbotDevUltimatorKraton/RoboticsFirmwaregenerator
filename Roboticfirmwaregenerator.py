#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Chanapai Chuadchum
#Project:Auracore color controller GUI 
#release date:25/2/2020
from paramiko import SSHClient, AutoAddPolicy # SSH remote command to activate the host machine control
from PyQt5 import QtCore, QtWidgets, uic,Qt,QtGui 
from PyQt5.QtWidgets import QApplication,QTreeView,QDirModel,QFileSystemModel,QVBoxLayout, QTreeWidget,QStyledItemDelegate, QTreeWidgetItem,QLabel,QGridLayout,QLineEdit,QDial,QComboBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QIcon,QImage,QPalette,QBrush
from pyqtgraph.Qt import QtCore, QtGui   #PyQt graph to control the model grphic loaded  
import pyqtgraph.opengl as gl
import subprocess # Getting the subprocess 
import pandas as pd 
import csv 
import os 
import sys 
import json #Reading the json file from the input nodes 
import getpass
import pywifi 
memwrite = [] #Getting the status of the writing process 
OS_name = [] #Getting the operating system choosing for uploadinto the robot
network_name = []
dict_cc = {} #Getting the dictionary 
username = getpass.getuser()
print(username)
PATH_SD_CARD = "/media/"+str(username)   #Path of the SD card 
name = "name"
code = "code"
ssidmem = [] #Getting the array ssid mem for the data of the wifi host name 
country = [{name: 'Afghanistan', code: 'AF'}, 
  {name: 'Åland Islands', code: 'AX'}, 
  {name: 'Albania', code: 'AL'}, 
  {name: 'Algeria', code: 'DZ'}, 
  {name: 'American Samoa', code: 'AS'}, 
  {name: 'AndorrA', code: 'AD'}, 
  {name: 'Angola', code: 'AO'}, 
  {name: 'Anguilla', code: 'AI'}, 
  {name: 'Antarctica', code: 'AQ'}, 
  {name: 'Antigua and Barbuda', code: 'AG'}, 
  {name: 'Argentina', code: 'AR'}, 
  {name: 'Armenia', code: 'AM'}, 
  {name: 'Aruba', code: 'AW'}, 
  {name: 'Australia', code: 'AU'}, 
  {name: 'Austria', code: 'AT'}, 
  {name: 'Azerbaijan', code: 'AZ'}, 
  {name: 'Bahamas', code: 'BS'}, 
  {name: 'Bahrain', code: 'BH'}, 
  {name: 'Bangladesh', code: 'BD'}, 
  {name: 'Barbados', code: 'BB'}, 
  {name: 'Belarus', code: 'BY'}, 
  {name: 'Belgium', code: 'BE'}, 
  {name: 'Belize', code: 'BZ'}, 
  {name: 'Benin', code: 'BJ'}, 
  {name: 'Bermuda', code: 'BM'}, 
  {name: 'Bhutan', code: 'BT'}, 
  {name: 'Bolivia', code: 'BO'}, 
  {name: 'Bosnia and Herzegovina', code: 'BA'}, 
  {name: 'Botswana', code: 'BW'}, 
  {name: 'Bouvet Island', code: 'BV'}, 
  {name: 'Brazil', code: 'BR'}, 
  {name: 'British Indian Ocean Territory', code: 'IO'}, 
  {name: 'Brunei Darussalam', code: 'BN'}, 
  {name: 'Bulgaria', code: 'BG'}, 
  {name: 'Burkina Faso', code: 'BF'}, 
  {name: 'Burundi', code: 'BI'}, 
  {name: 'Cambodia', code: 'KH'}, 
  {name: 'Cameroon', code: 'CM'}, 
  {name: 'Canada', code: 'CA'}, 
  {name: 'Cape Verde', code: 'CV'}, 
  {name: 'Cayman Islands', code: 'KY'}, 
  {name: 'Central African Republic', code: 'CF'}, 
  {name: 'Chad', code: 'TD'}, 
  {name: 'Chile', code: 'CL'}, 
  {name: 'China', code: 'CN'}, 
  {name: 'Christmas Island', code: 'CX'}, 
  {name: 'Cocos (Keeling) Islands', code: 'CC'}, 
  {name: 'Colombia', code: 'CO'}, 
  {name: 'Comoros', code: 'KM'}, 
  {name: 'Congo', code: 'CG'}, 
  {name: 'Congo, The Democratic Republic of the', code: 'CD'}, 
  {name: 'Cook Islands', code: 'CK'}, 
  {name: 'Costa Rica', code: 'CR'}, 
  {name: 'Cote D\'Ivoire', code: 'CI'}, 
  {name: 'Croatia', code: 'HR'}, 
  {name: 'Cuba', code: 'CU'}, 
  {name: 'Cyprus', code: 'CY'}, 
  {name: 'Czech Republic', code: 'CZ'}, 
  {name: 'Denmark', code: 'DK'}, 
  {name: 'Djibouti', code: 'DJ'}, 
  {name: 'Dominica', code: 'DM'}, 
  {name: 'Dominican Republic', code: 'DO'}, 
  {name: 'Ecuador', code: 'EC'}, 
  {name: 'Egypt', code: 'EG'}, 
  {name: 'El Salvador', code: 'SV'}, 
  {name: 'Equatorial Guinea', code: 'GQ'}, 
  {name: 'Eritrea', code: 'ER'}, 
  {name: 'Estonia', code: 'EE'}, 
  {name: 'Ethiopia', code: 'ET'}, 
  {name: 'Falkland Islands (Malvinas)', code: 'FK'}, 
  {name: 'Faroe Islands', code: 'FO'}, 
  {name: 'Fiji', code: 'FJ'}, 
  {name: 'Finland', code: 'FI'}, 
  {name: 'France', code: 'FR'}, 
  {name: 'French Guiana', code: 'GF'}, 
  {name: 'French Polynesia', code: 'PF'}, 
  {name: 'French Southern Territories', code: 'TF'}, 
  {name: 'Gabon', code: 'GA'}, 
  {name: 'Gambia', code: 'GM'}, 
  {name: 'Georgia', code: 'GE'}, 
  {name: 'Germany', code: 'DE'}, 
  {name: 'Ghana', code: 'GH'}, 
  {name: 'Gibraltar', code: 'GI'}, 
  {name: 'Greece', code: 'GR'}, 
  {name: 'Greenland', code: 'GL'}, 
  {name: 'Grenada', code: 'GD'}, 
  {name: 'Guadeloupe', code: 'GP'}, 
  {name: 'Guam', code: 'GU'}, 
  {name: 'Guatemala', code: 'GT'}, 
  {name: 'Guernsey', code: 'GG'}, 
  {name: 'Guinea', code: 'GN'}, 
  {name: 'Guinea-Bissau', code: 'GW'}, 
  {name: 'Guyana', code: 'GY'}, 
  {name: 'Haiti', code: 'HT'}, 
  {name: 'Heard Island and Mcdonald Islands', code: 'HM'}, 
  {name: 'Holy See (Vatican City State)', code: 'VA'}, 
  {name: 'Honduras', code: 'HN'}, 
  {name: 'Hong Kong', code: 'HK'}, 
  {name: 'Hungary', code: 'HU'}, 
  {name: 'Iceland', code: 'IS'}, 
  {name: 'India', code: 'IN'}, 
  {name: 'Indonesia', code: 'ID'}, 
  {name: 'Iran, Islamic Republic Of', code: 'IR'}, 
  {name: 'Iraq', code: 'IQ'}, 
  {name: 'Ireland', code: 'IE'}, 
  {name: 'Isle of Man', code: 'IM'}, 
  {name: 'Israel', code: 'IL'}, 
  {name: 'Italy', code: 'IT'}, 
  {name: 'Jamaica', code: 'JM'}, 
  {name: 'Japan', code: 'JP'}, 
  {name: 'Jersey', code: 'JE'}, 
  {name: 'Jordan', code: 'JO'}, 
  {name: 'Kazakhstan', code: 'KZ'}, 
  {name: 'Kenya', code: 'KE'}, 
  {name: 'Kiribati', code: 'KI'}, 
  {name: 'Korea, Democratic People\'S Republic of', code: 'KP'}, 
  {name: 'Korea, Republic of', code: 'KR'}, 
  {name: 'Kuwait', code: 'KW'}, 
  {name: 'Kyrgyzstan', code: 'KG'}, 
  {name: 'Lao People\'S Democratic Republic', code: 'LA'}, 
  {name: 'Latvia', code: 'LV'}, 
  {name: 'Lebanon', code: 'LB'}, 
  {name: 'Lesotho', code: 'LS'}, 
  {name: 'Liberia', code: 'LR'}, 
  {name: 'Libyan Arab Jamahiriya', code: 'LY'}, 
  {name: 'Liechtenstein', code: 'LI'}, 
  {name: 'Lithuania', code: 'LT'}, 
  {name: 'Luxembourg', code: 'LU'}, 
  {name: 'Macao', code: 'MO'}, 
  {name: 'Macedonia, The Former Yugoslav Republic of', code: 'MK'}, 
  {name: 'Madagascar', code: 'MG'}, 
  {name: 'Malawi', code: 'MW'}, 
  {name: 'Malaysia', code: 'MY'}, 
  {name: 'Maldives', code: 'MV'}, 
  {name: 'Mali', code: 'ML'}, 
  {name: 'Malta', code: 'MT'}, 
  {name: 'Marshall Islands', code: 'MH'}, 
  {name: 'Martinique', code: 'MQ'}, 
  {name: 'Mauritania', code: 'MR'}, 
  {name: 'Mauritius', code: 'MU'}, 
  {name: 'Mayotte', code: 'YT'}, 
  {name: 'Mexico', code: 'MX'}, 
  {name: 'Micronesia, Federated States of', code: 'FM'}, 
  {name: 'Moldova, Republic of', code: 'MD'}, 
  {name: 'Monaco', code: 'MC'}, 
  {name: 'Mongolia', code: 'MN'}, 
  {name: 'Montserrat', code: 'MS'}, 
  {name: 'Morocco', code: 'MA'}, 
  {name: 'Mozambique', code: 'MZ'}, 
  {name: 'Myanmar', code: 'MM'}, 
  {name: 'Namibia', code: 'NA'}, 
  {name: 'Nauru', code: 'NR'}, 
  {name: 'Nepal', code: 'NP'}, 
  {name: 'Netherlands', code: 'NL'}, 
  {name: 'Netherlands Antilles', code: 'AN'}, 
  {name: 'New Caledonia', code: 'NC'}, 
  {name: 'New Zealand', code: 'NZ'}, 
  {name: 'Nicaragua', code: 'NI'}, 
  {name: 'Niger', code: 'NE'}, 
  {name: 'Nigeria', code: 'NG'}, 
  {name: 'Niue', code: 'NU'}, 
  {name: 'Norfolk Island', code: 'NF'}, 
  {name: 'Northern Mariana Islands', code: 'MP'}, 
  {name: 'Norway', code: 'NO'}, 
  {name: 'Oman', code: 'OM'}, 
  {name: 'Pakistan', code: 'PK'}, 
  {name: 'Palau', code: 'PW'}, 
  {name: 'Palestinian Territory, Occupied', code: 'PS'}, 
  {name: 'Panama', code: 'PA'}, 
  {name: 'Papua New Guinea', code: 'PG'}, 
  {name: 'Paraguay', code: 'PY'}, 
  {name: 'Peru', code: 'PE'}, 
  {name: 'Philippines', code: 'PH'}, 
  {name: 'Pitcairn', code: 'PN'}, 
  {name: 'Poland', code: 'PL'}, 
  {name: 'Portugal', code: 'PT'}, 
  {name: 'Puerto Rico', code: 'PR'}, 
  {name: 'Qatar', code: 'QA'}, 
  {name: 'Reunion', code: 'RE'}, 
  {name: 'Romania', code: 'RO'}, 
  {name: 'Russian Federation', code: 'RU'}, 
  {name: 'RWANDA', code: 'RW'}, 
  {name: 'Saint Helena', code: 'SH'}, 
  {name: 'Saint Kitts and Nevis', code: 'KN'}, 
  {name: 'Saint Lucia', code: 'LC'}, 
  {name: 'Saint Pierre and Miquelon', code: 'PM'}, 
  {name: 'Saint Vincent and the Grenadines', code: 'VC'}, 
  {name: 'Samoa', code: 'WS'}, 
  {name: 'San Marino', code: 'SM'}, 
  {name: 'Sao Tome and Principe', code: 'ST'}, 
  {name: 'Saudi Arabia', code: 'SA'}, 
  {name: 'Senegal', code: 'SN'}, 
  {name: 'Serbia and Montenegro', code: 'CS'}, 
  {name: 'Seychelles', code: 'SC'}, 
  {name: 'Sierra Leone', code: 'SL'}, 
  {name: 'Singapore', code: 'SG'}, 
  {name: 'Slovakia', code: 'SK'}, 
  {name: 'Slovenia', code: 'SI'}, 
  {name: 'Solomon Islands', code: 'SB'}, 
  {name: 'Somalia', code: 'SO'}, 
  {name: 'South Africa', code: 'ZA'}, 
  {name: 'South Georgia and the South Sandwich Islands', code: 'GS'}, 
  {name: 'Spain', code: 'ES'}, 
  {name: 'Sri Lanka', code: 'LK'}, 
  {name: 'Sudan', code: 'SD'}, 
  {name: 'Suriname', code: 'SR'}, 
  {name: 'Svalbard and Jan Mayen', code: 'SJ'}, 
  {name: 'Swaziland', code: 'SZ'}, 
  {name: 'Sweden', code: 'SE'}, 
  {name: 'Switzerland', code: 'CH'}, 
  {name: 'Syrian Arab Republic', code: 'SY'}, 
  {name: 'Taiwan, Province of China', code: 'TW'}, 
  {name: 'Tajikistan', code: 'TJ'}, 
  {name: 'Tanzania, United Republic of', code: 'TZ'}, 
  {name: 'Thailand', code: 'TH'}, 
  {name: 'Timor-Leste', code: 'TL'}, 
  {name: 'Togo', code: 'TG'}, 
  {name: 'Tokelau', code: 'TK'}, 
  {name: 'Tonga', code: 'TO'}, 
  {name: 'Trinidad and Tobago', code: 'TT'}, 
  {name: 'Tunisia', code: 'TN'}, 
  {name: 'Turkey', code: 'TR'}, 
  {name: 'Turkmenistan', code: 'TM'}, 
  {name: 'Turks and Caicos Islands', code: 'TC'}, 
  {name: 'Tuvalu', code: 'TV'}, 
  {name: 'Uganda', code: 'UG'}, 
  {name: 'Ukraine', code: 'UA'}, 
  {name: 'United Arab Emirates', code: 'AE'}, 
  {name: 'United Kingdom', code: 'GB'}, 
  {name: 'United States', code: 'US'}, 
  {name: 'United States Minor Outlying Islands', code: 'UM'}, 
  {name: 'Uruguay', code: 'UY'}, 
  {name: 'Uzbekistan', code: 'UZ'}, 
  {name: 'Vanuatu', code: 'VU'}, 
  {name: 'Venezuela', code: 'VE'}, 
  {name: 'Viet Nam', code: 'VN'}, 
  {name: 'Virgin Islands, British', code: 'VG'}, 
  {name: 'Virgin Islands, U.S.', code: 'VI'}, 
  {name: 'Wallis and Futuna', code: 'WF'}, 
  {name: 'Western Sahara', code: 'EH'}, 
  {name: 'Yemen', code: 'YE'}, 
  {name: 'Zambia', code: 'ZM'}, 
  {name: 'Zimbabwe', code: 'ZW'} 
]
selectedcountry = [] #Getting the selected country 
os_list = ['Linux Ubuntu x64 x86','Linux Debian x64 x86','Linux Ubuntu arm 32','Linux Debian arm 32','Linux Ubuntu arm 64','Linux Debian arm 64'] #The list of the operaring system on the system 
osmem = []
#Password = "Rkj3548123" #Find the way to popup and get the password using this part as login into the system 
os.system("echo Hello"+"\t"+str(username)) #Getting the host name 
parent_dir = "/home/"+username+"/"
directory = ["Wifi_devices_connects","Robotics_nodes_json"]
# running the loop of make directory 
for dric in range(0,len(directory)):
   try:
      print("Now creating.....",str(directory[dric])) #Getting the directory created for the wifi config and robotics nodes json  
      path = os.path.join(parent_dir, directory[dric]) 
      os.mkdir(path) #Make the path file for the wifi device connection data for choosing on the firmware devices generator
   except:
       print(directory[dric]+" directory  was created")
nodelist = os.listdir(os.path.join(parent_dir,directory[1]))  #getting the list of the robotics node json 
nodelist.append(" ")
storage_path = "/media/"+username  
generic_storage = os.listdir(storage_path) #Getting the list of the storate path 
generic_mem = []
generic_mem.append(" ")
generic_mem.append("Generic storage"+str(generic_storage))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Getting the device name of the host 
devices = subprocess.check_output("arp -a",shell=True)
extract_devices = devices.decode('utf-8')
#print(extract_devices.split("wlo1"))
devices_list = extract_devices.split("wlo1")
hostname_mem = [] #Getting the list of the devices host name 
hostip_mem = [] #Getting the list of the devices host ip 
automateip_add = {}
hoste_selected =[]
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #Getting the wifi of the host 
wifi_mem = []


class MainWindow(QtWidgets.QMainWindow):
   
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('Roboticfirmwaregenerator.ui', self)
        self.setWindowTitle('Robotics firmware generator  User:'+"\t"+username)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(p)
        self.pushButton.clicked.connect(self.Writeimage)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
              #Set of commbobox selection function 
        self.combo1 = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox,"comboBox_2")
        self.combo3 = self.findChild(QComboBox,"comboBox_3")
        self.combo4 = self.findChild(QComboBox, "comboBox_4")
        self.combo5 = self.findChild(QComboBox,"comboBox_5")
        self.combo7 = self.findChild(QComboBox,"comboBox_7")
        self.combo1.activated.connect(self.Operatingsystem)
        self.combo1.addItems(os_list)
        self.combo2.activated.connect(self.Storage_generic)
        self.combo2.addItems(generic_mem)
        self.combo3.activated.connect(self.robotnodes)
        self.combo3.addItems(nodelist) #Getting the robotics node json file 
        self.combo5.activated.connect(self.countrychoose)  #Getting the data from the list dictionary countr to display on the combobox 
        for countries in range(0,len(country)):
                       print(country[countries])
                       dict_cc[country[countries].get('name')] = country[countries].get('code')
        print(dict_cc)
        self.combo5.addItems(list(dict_cc))  #Adding the country into the list item of the combobox
        self.combo4.activated.connect(self.hostname_data)
        for ri in range(0,len(devices_list)-1):
            print(devices_list[ri].split(" "))
            origin_list = devices_list[ri].split(" ")[0]
            getdatahost = devices_list[ri].split(" ")[1]
            gethostip = getdatahost.split("(")[1].split(")")[0]
            print(origin_list,getdatahost.split("(")[1].split(")")[0])
            hostname_mem.append(origin_list) #Get the hostname of the devices 
            #hostip_mem.append(gethostip) #Get the host ip of the devices 
            automateip_add[origin_list] = gethostip #Getting the autolist of the ip address 
        self.combo4.addItems(hostname_mem)#Getting the host mem data into the combo box  
        #self.combo6.addItems(hostip_mem) #Getting the ip address of the host target selected
        print(automateip_add)
        self.combo7.activated.connect(self.wifissid)
        for wifi_R in range(0,1):
                     getwifi = subprocess.check_output("nmcli dev wifi",shell=True) 
                     dataframe = getwifi.decode('utf-8')
                     #print(type(dataframe))
                     #print(dataframe)
                     file = open("currentwifi.csv",'w')
                     file.write(dataframe)
                     file.close()
                     #df = pandas.DataFrame(dataframe, columns=['SSID', 'SIGNAL'])
                     df = pd.read_csv('currentwifi.csv')
                     #print("Reading the saving current available wifi")
                     print(df)
                     index = df.index
                     print(index)
                     listdata = list(df.columns.values)
                     print(listdata)
                     print(listdata[0].split(" ")) #recreate the columns separate from one big column
                     print(df[listdata[0]].values[0])
                     print(len(index))
                     for wifi in range(0,len(index)-1):
                             getting_str =  df[listdata[0]].values[wifi].split(" ") #split the wifi data to get the wifi name and signal strength to choosing the best connection 
                             print(getting_str[10])
                             if len(wifi_mem) < len(index):
                                           wifi_mem.append(getting_str[10]) #getting the mem wifi name 
                             if len(wifi_mem) > len(index):
                                   terminal = len(wifi_mem)-len(index)
                                   for wifilist in range(len(index),terminal):
                                             wifi_mem.remove(wifi_mem[wifilist]) #remove the len of the index if the length is over 
                     self.combo7.addItems([" "]) #Getting the blank list on the top to be able to choosing the data in the combobox later 
                     self.combo7.addItems(wifi_mem) #getting the list of wifi memory
                     print(wifi_mem)
    def wifissid(self,wifi_index):
             print(wifi_mem[wifi_index])
             if len(network_name) < len(wifi_mem):
                   network_name.append(wifi_mem[wifi_index-1])  #Getting the wifi mem on the list of the network name to generate the wifi configuretion on sd card 
             #if len(network_name) >1:
             #      network_name.remove(network_name[0]) #remove the network name from the list if out of range 
             print(network_name)      
    def hostip_data(self,hostip_index):
             print(hostip_mem[hostip_index-1])    
    def hostname_data(self,host_index):
             print(hostname_mem[host_index]) #Getting the host index
             print(automateip_add.get(hostname_mem[host_index]))
             if str(automateip_add.get(hostname_mem[host_index])) not in hostip_mem:
                       hostip_mem.append(automateip_add.get(hostname_mem[host_index]))
             if len(hostip_mem) > 1:
                       hostip_mem.remove(hostip_mem[0])

    def Storage_generic(self,index_storage):
                print(generic_mem[index_storage])
    def robotnodes(self,nodes_list):
                print(nodelist[nodes_list])
    def Operatingsystem(self,osp):
             print(os_list[osp])
             if osmem !=[]:
                   osmem.append(os_list[osp])
             if len(osmem) > 1:
                  osmem.remove(osmem[len(osmem)-1]) 
             print(osmem)    
    def countrychoose(self,countries_cc):
                 #Getting the breviation from key
              try:
                 print(list(dict_cc)[countries_cc])
                 get_extracted = list(dict_cc)[countries_cc]
                 selected_cc = dict_cc.get(get_extracted)
                 print(selected_cc)
                 selectedcountry.append(selected_cc) #Getting the country breviation for the memory function              
                 print("Store country breviation successfully....")
              except: 
                   print("Store country breviation error")
    #def ssidscan(self,index_ssid):
    #             print("index number",index_ssid)
    #             print("SSID_name",ssidmem[index_ssid]) #Turn index ssid into the ssid list 
    def Writeimage(self):
            if memwrite ==[]:
                    memwrite.append("Write") #Getting the status write 
            if len(memwrite) >1:
                   memwrite.remove(memwrite[len(memwrite)]) #remove the memwrite with over lenght status writing on the array 
            print("Start writing the firmware on boot........") #Display the status on the logo 
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                 #Start writing the firmware
                 #Selecte case of the operating system to upload the firmware into the 
            #This will be using the list combobox to select the SBC type tp choosing the image writer selection capability 
            #Accessing the boot directory of the raspberrypi_boot directory   
            target_rpi = ["boot","rootfs","pi"]   #Getting the into the directory of the inner file 
            #Checking there is boot  
            list_seek_boot = os.listdir(PATH_SD_CARD) #Seeking the target file 
            print("Seek dir",list_seek_boot) #Getting the list seek boot 
            for re in range(0,len(list_seek_boot)):
                        
                                      if list_seek_boot[re] == str(target_rpi[1]):
                                                  print("Found "+str(list_seek_boot[re])+" Now operating firmware injection.......")
                                                  
                                                  
                                      if list_seek_boot[re] == str(target_rpi[0]):
                                                  print("Found "+str(list_seek_boot[re])+" Now operating setting SSH and WiFi.......")
                                                  #Writing the file into the path
                                                  filessh = open(PATH_SD_CARD+"/"+list_seek_boot[re]+"/"+"ssh","w")  #Write the ssh file into the boot directory
                                                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                  filessh.write(" ")
                                                  filessh.close() #Close the file writer after finish writing the file ssh for enable ssh command 

                                                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                  filewpa_supplicant = open(PATH_SD_CARD+"/"+list_seek_boot[re]+"/"+"wpa_supplicant.conf",'w')
                                                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
                                                  print(selectedcountry)
                                                  filewpa_supplicant.write("country="+selectedcountry[0]) #Getting the country
                                                  filewpa_supplicant.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev")
                                                  filewpa_supplicant.write("update_config=1")
                                                  filewpa_supplicant.write("network={")
                                                  filewpa_supplicant.write("ssid="+network_name)  #Getting the name of the network from the combobox list SSID password
                                                  #filewpa_supplicant.write("psk="+network_password) #Getting the password from the text input 
                                                  filewpa_supplicant.write("}")  
                                                  print(namenetwork)

                                                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                  
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__':         
    main()
