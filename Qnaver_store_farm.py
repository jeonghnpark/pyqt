from PyQt5.QtWidgets import QTabWidget, QDialog, QApplication, QWidget \
    ,QLabel,QLineEdit, QVBoxLayout,QHBoxLayout ,QGroupBox,QPushButton,QDialogButtonBox \
    ,QGroupBox, QFileDialog,QInputDialog,QCheckBox,QTableWidget,QTableWidgetItem,QComboBox,QListWidget ,QMenuBar,QAction,QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import requests
from bs4 import BeautifulSoup
from functools import partial
import sqlite3
from datetime import datetime, timedelta
from save_prod_list_db import all_items

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,800,800)
        self.initWindow()

    def initWindow(self):
    
        vbox=QVBoxLayout()
        tabwidget=QTabWidget()
        tabwidget.addTab(MyStorFarm(), "나의 스토어팜")
        tabwidget.addTab(ContactDetail(),"신상품 찾기")
        tabwidget.addTab(ImageLoad(), "트렌트분석")
        
        # self.buttonbox=QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # self.buttonbox.accepted.connect(self.acc)
        # self.buttonbox.rejected.connect(self.rej)

        vbox.addWidget(tabwidget)
        # vbox.addWidget(self.buttonbox)
        self.setLayout(vbox)

    def acc(self):
        self.close()
    def rej(self):
        pass


class FarmList(QWidget):
    def __init__(self,li):
        super().__init__()
        self.InitUi(li)
    
    def InitUi(self,li):
        self.listwidget=QListWidget()
        self.listwidget.addItems(li)
        self.hbox=QHBoxLayout()
        self.addBtn=QPushButton('add')

        self.hbox.addWidget(self.listwidget)
        self.hbox.addWidget(self.addBtn)
        
        self.addBtn.clicked.connect(partial(self.addFarm,li))
        self.setLayout(self.hbox)

    def addFarm(self,li):
        string, ok=QInputDialog.getText(self,'Add Farm','추가할 스토어팜 주소를 입력하세요')
        if ok and string is not None:
            row=self.listwidget.currentRow()
            self.listwidget.insertItem(row,string)
            li.append(string)
            print(li)

    # def list_clicked(self):
    #     item=self.listwidget.currentItem()
    #     self.label.setText(str(item.text()))

class MyStorFarm(QWidget):
    def __init__(self):
        super().__init__()
        hbox=QHBoxLayout()
        namelabel=QLabel("스토어팜주소")
        self.farm_combo=QComboBox()
        self.li=['https://smartstore.naver.com/heyhannah','https://smartstore.naver.com/monsclub']
        self.farm_combo.addItems(self.li)
        self.shop_title_label=QLabel()
        self.show_farm_name()
        self.btn_show_prod=QPushButton('조회')
        self.btn_show_prod.setIcon(QtGui.QIcon('update.png'))
        self.gear_btn=QPushButton()
        self.gear_btn.setIcon(QtGui.QIcon('gear.png'))

        hbox.addWidget(namelabel)
        hbox.addWidget(self.farm_combo)
        hbox.addWidget(self.shop_title_label)
        hbox.addWidget(self.btn_show_prod)
        hbox.addWidget(self.gear_btn)
    
        self.gear_btn.clicked.connect(partial(self.setFarm,self.li))
        self.btn_show_prod.clicked.connect(self.get_prod)
        self.farm_combo.currentTextChanged.connect(self.show_farm_name)

        vbox=QVBoxLayout()
        self.tablewidget=QTableWidget()
        self.tablewidget.setRowCount(300)
        self.tablewidget.setColumnCount(6)
        self.tablewidget.setItem(0,0,QTableWidgetItem("상품명"))
        self.tablewidget.setItem(0,1,QTableWidgetItem("찜"))
        self.tablewidget.setItem(0,2,QTableWidgetItem("구매"))
        self.tablewidget.setItem(0,3,QTableWidgetItem("리뷰"))
        

        # itemslist=all_items()
        conn=sqlite3.connect('emaildb.sqlite')
        cur=conn.cursor()
        tod=datetime.today().strftime('%Y-%m-%d')

        # for item in itemslist:
        #     cur.execute('''
        #             REPlACE INTO PROD (dt,title, pid, jjim, sold,review) VALUES (?,?,?,?,?,?);''', (tod,item['name'],item['pid'] ,item['jjim'],item['sold'],item['review']))
        
        cur.execute('''
                    Select title, jjim, sold, review from PROD where dt='2020-04-14' ''')
        
        conn.commit()
        
        rows=cur.fetchall()
        
        for i,row in enumerate(rows):
            # print(i, row[0])
            for j, elem in enumerate(row):
                
            #     print(i+1,j,elem)
            #     self.tablewidget.setItem(i+1,j,QTableWidgetItem(elem))
                self.tablewidget.setItem(i+1,j,QTableWidgetItem(str(row[j])))
            # print(row[1])
                # self.tablewidget.setItem(i+1,1,QTableWidgetItem(str(row[1])))
                

        cur.close()
        
        
        self.groupbox=QGroupBox()
        self.groupbox.setLayout(hbox)

        vbox.addWidget(self.groupbox)
        vbox.addWidget(self.tablewidget)

        self.setLayout(vbox)

    def get_prod(self):
        url=self.farm_combo.currentText()
        print(url)
        

    def setFarm(self,li):
        self.farmlist=FarmList(self.li)
        # print(self.li)
        # self.farm_combo.addItems(self.li)
        self.farmlist.show()
        
    def show_farm_name(self):
        # self.shop_title_label.setText("sssss")
        url=self.farm_combo.currentText()
        req=requests.get(url)
        soup=BeautifulSoup(req.text, 'html.parser')
        self.shop_title_label.setText(soup.find('title').text.strip())
        # self.shop_title_label.setText("aaa")

class ContactDetail(QWidget):
    def __init__(self):
        super().__init__()
        vboxmain=QVBoxLayout()
        vbox1=QVBoxLayout()
        groupbox=QGroupBox('Select gender')
        
        combo=QComboBox()
        li=['male', 'female']
        combo.addItems(li)
        vbox1.addWidget(combo)
        groupbox.setLayout(vbox1)
        
        groupbox2=QGroupBox('select your language')
        ch1=QCheckBox('C++')
        ch2=QCheckBox("java")
        ch3=QCheckBox('c#')
        vbox2=QVBoxLayout()
        vbox2.addWidget(ch1)
        vbox2.addWidget(ch2)
        vbox2.addWidget(ch3)
        
        groupbox2.setLayout(vbox2)
        
        vboxmain.addWidget(groupbox)
        vboxmain.addWidget(groupbox2)
        self.setLayout(vboxmain)

class ImageLoad(QWidget):
    def __init__(self):
        super().__init__()
        btn=QPushButton("load image")
        self.lb=QLabel("hello")
        btn.clicked.connect(self.imBtn)
        vbox=QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(self.lb)
        self.setLayout(vbox)
        
    def imBtn(self):
        fname=QFileDialog.getOpenFileName(self,'파일이름?','D:\Program Files\WarCraft II\IMG\잡지부록판CD-COVER')
        imagePath=fname[0]
        pixmap=QPixmap(imagePath)
        self.lb.setPixmap(QPixmap(pixmap))
        # self.resize(pixmap.width(), pixmap.height())
    

App=QApplication(sys.argv)
win=Window()
win.show()
App.exec()
