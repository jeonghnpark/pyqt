from PyQt5.QtWidgets import QTabWidget, QDialog, QApplication, QWidget \
    ,QLabel,QLineEdit, QVBoxLayout, QGroupBox,QPushButton,QDialogButtonBox \
    ,QGroupBox, QCheckBox, QComboBox, QMenuBar,QAction
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,400)
        self.initWindow()

    def initWindow(self):
        menuBar=QMenuBar()
        fileMenu=menuBar.addMenu("file")
        exitAction=QAction('exit',self)
        fileMenu.addAction(exitAction)
        vbox=QVBoxLayout()
        tabwidget=QTabWidget()
        tabwidget.addTab(ContactDetail(),"Contact Detail")
        tabwidget.addTab(PersonalDetail(), "Personal Detail")
        self.buttonbox=QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonbox.accepted.connect(self.acc)
        self.buttonbox.rejected.connect(self.rej)

        vbox.addWidget(tabwidget)
        vbox.addWidget(self.buttonbox)
        self.setLayout(vbox)


    def acc(self):
        pass
    def rej(self):
        pass

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
