from PyQt5.QtWidgets import QTabWidget, QDialog, QApplication, QWidget \
    ,QLabel,QLineEdit, QVBoxLayout, QGroupBox,QPushButton,QDialogButtonBox \
    ,QGroupBox, QFileDialog,QCheckBox,QComboBox, QMenuBar,QAction,QMainWindow
import sys
from PyQt5.QtGui import QPixmap

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,400)
        self.initWindow()

    def initWindow(self):
        

        vbox=QVBoxLayout()
        tabwidget=QTabWidget()
        tabwidget.addTab(ContactDetail(),"Contact Detail")
        tabwidget.addTab(PersonalDetail(), "Personal Detail")
        tabwidget.addTab(ImageLoad(), "Image Load")
        
        self.buttonbox=QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonbox.accepted.connect(self.acc)
        self.buttonbox.rejected.connect(self.rej)

        vbox.addWidget(tabwidget)
        vbox.addWidget(self.buttonbox)
        self.setLayout(vbox)

    def acc(self):
        self.close()
    def rej(self):
        pass
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
    

class PersonalDetail(QWidget):
    def __init__(self):
        super().__init__()
        namelabel=QLabel("Name")
        namelineedit=QLineEdit()
        addressLabel=QLabel('Address')
        addressLineEdit=QLineEdit()
        vbox=QVBoxLayout()
        vbox.addWidget(namelabel)
        vbox.addWidget(namelineedit)
        vbox.addWidget(addressLabel)
        vbox.addWidget(addressLineEdit)

        self.setLayout(vbox)


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

App=QApplication(sys.argv)
win=Window()
win.show()
App.exec()
