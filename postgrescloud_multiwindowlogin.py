#using the input data from the pyqt5 to login into the system with the client login app to checking with the database 
import os 
import sys 
import csv
import json 
import requests
import socket
import getpass 
import psycopg2 # Login for the client side on the app machine 
import pandas as pd 
import subprocess # Getting the subprocess 
from PyQt5 import QtCore, QtWidgets, uic,Qt,QtGui 
from PyQt5.QtWidgets import QApplication,QTreeView,QDirModel,QFileSystemModel,QVBoxLayout, QTreeWidget,QStyledItemDelegate, QTreeWidgetItem,QLabel,QGridLayout,QLineEdit,QDial,QComboBox,QTextEdit,QTabWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QIcon,QImage,QPalette,QBrush
from pyqtgraph.Qt import QtCore, QtGui   #PyQt graph to control the model grphic loaded  
import pyqtgraph.opengl as gl
#Now using this postgresql-opaque-57490 #heroku cloud postgresql roboreactoruser https://roboreactoruser.herokuapp.com/ | https://git.heroku.com/roboreactoruser.git
#postgresql-rigid-15553  #heroku cloud postgresql robouserdb https://robouserdb.herokuapp.com/ | https://git.heroku.com/robouserdb.git
Host = "ec2-18-215-96-54.compute-1.amazonaws.com"
Database = "d8rl9i6joj63v8",
Password = "b85574f77cd76ccbaef7a0f661086c6b28724d236c730c74c2d8021934e8bbe1"
Port = "5432"
username = getpass.getuser()
print(username)
def query():
      #Getting the host url https://dashboard.heroku.com/apps  
      conn = psycopg2.connect(
               host = Host,
               database = Database,
               password = Password,
               port = Port,
      )
      c = conn.curcor()
      c.execute('''CREATE TABLE IF NOT EXIST customers
      (first_name Text,
      last_name Text,
      e_mail Text,
      password Text,
      payment_status Text,
      Cardholder Text,
      schedule Text,
      Recharge Text);''')
      c.commit()
      c.close()
      print(c)
def submit():
      #Getting the host url https://dashboard.heroku.com/apps  
      conn = psycopg2.connect(
               host = Host,
               database = Database,
               password = Password,
               port = Port,
      )
      c = conn.curcor()
      c.execute('''CREATE TABLE IF NOT EXIST customers
      (first_name Text,
      last_name Text,
      e_mail Text,
      password Text,
      payment_status Text,
      cardholder Text,
      schedule Text,
      recharge Text);''')
      # Create a cursor
      c = conn.cursor()
      # Insert data into table 
      C1 = f_name.get() 
      C2 = l_name.get() 
      C3 = email.get()
      C4 = passwd.get()
      C5 = payment_stus.get()  
      C6 = cardholder.get() 
      C7 = schedule.get() 
      C8 = recharge.get()
      c.execute('''INSERT INTO customers (first_name,last_name,e_mail,password,payment_status,cardholder,schedule,recharge)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',(f_name.get(),l_name.get(),email.get(),passwd.get(),payment_stus.get(),cardholder.get(),schedule.get(),recharge.get())
      )

class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()

        #Load the UI Page
        uic.loadUi('Roboticfirmwaregenerator.ui', self)
        self.setWindowTitle('Roboreactor firmware generator  User:'+"\t"+username)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(p)
        #Adding the roboreactor firmware generator function right here 

    
class MainWindow(QtWidgets.QMainWindow):
   
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('Loginpage.ui', self)
        self.setWindowTitle('Welcome to roboreactor User:'+"\t"+username)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(p)
        self.pushButton.clicked.connect(self.Login)
        
    def Login(self):
            print("Logging into the database......")
            #making the database input data here 
            self.w = MainWindow2()
            self.w.show() 
            self.hide() 



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__':         
    main()