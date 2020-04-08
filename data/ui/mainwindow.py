# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

#下列代码根据我设计的 .ui 文件生成，加入了两个自定义的函数 log() 和 clear()
class Ui_MainWindow(QWidget): #继承自父类QtWidgets.QWidget
    def __init__(self,parent=None):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 680)
        MainWindow.setMinimumSize(QtCore.QSize(1160, 680))
        MainWindow.setMaximumSize(QtCore.QSize(1160, 680))
        MainWindow.setStyleSheet("boder=2px")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.Title1 = QtWidgets.QLabel(self.centralwidget)
        self.Title1.setGeometry(QtCore.QRect(60, 30, 651, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(34)
        self.Title1.setFont(font)
        self.Title1.setObjectName("Title1")
        self.Title2 = QtWidgets.QLabel(self.centralwidget)
        self.Title2.setGeometry(QtCore.QRect(200, 90, 350, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.Title2.setFont(font)
        self.Title2.setObjectName("Title2")
        self.URLEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.URLEdit.setGeometry(QtCore.QRect(150, 150, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.URLEdit.setFont(font)
        self.URLEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.URLEdit.setObjectName("URLEdit")
        self.URLEdit.isClearButtonEnabled()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.previewbt = QtWidgets.QPushButton(self.centralwidget)
        self.previewbt.setGeometry(QtCore.QRect(160, 180, 241, 23))
        self.previewbt.setObjectName("previewbt")
        self.beginbt = QtWidgets.QPushButton(self.centralwidget)
        self.beginbt.setGeometry(QtCore.QRect(170, 250, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.beginbt.setFont(font)
        self.beginbt.setObjectName("beginbt")
        self.setting = QtWidgets.QGroupBox(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(60, 290, 451, 141))
        self.setting.setFlat(False)
        self.setting.setCheckable(False)
        self.setting.setObjectName("setting")
        
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_2 = QtWidgets.QLabel(self.setting)
        self.label_2.setGeometry(QtCore.QRect(40, 25, 81, 31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.mode_choose = QtWidgets.QComboBox(self.setting)
        self.mode_choose.setGeometry(QtCore.QRect(120, 25, 241, 25))
        self.mode_choose.setObjectName("mode_choose")
        self.mode_choose.addItem("")
        self.mode_choose.addItem("")
        self.wordorcharacter = QtWidgets.QComboBox(self.setting) #选择是否分单个字词选择框
        self.wordorcharacter.setGeometry(QtCore.QRect(120, 65, 150, 25))
        self.wordorcharacter.setObjectName("wordorcharacter")
        self.wordorcharacter.addItem("")
        self.wordorcharacter.addItem("")
        self.label_3 = QtWidgets.QLabel(self.setting)
        self.label_3.setGeometry(QtCore.QRect(40, 65, 81, 25))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.setting)
        self.label_4.setGeometry(QtCore.QRect(40, 105, 81, 25))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.NumEdit = QtWidgets.QLineEdit(self.setting) #字词数量编辑框
        self.NumEdit.setText('75') #设置默认值
        self.NumEdit.setGeometry(QtCore.QRect(120, 105, 75, 25))
        self.NumEdit.setFont(font)
        self.NumEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NumEdit.setObjectName("NumEdit")
        self.NumEdit.setValidator(QtGui.QIntValidator())
        self.NumEdit.setMaxLength(3);
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 440, 451, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.previewgroup = QtWidgets.QGroupBox(self.centralwidget)
        self.previewgroup.setGeometry(QtCore.QRect(560, 20, 581, 581))
        self.previewgroup.setObjectName("previewgroup")
        self.picturebox = QtWidgets.QWidget(self.previewgroup)
        self.picturebox.setGeometry(QtCore.QRect(10, 20, 561, 511))
        self.picturebox.setObjectName("picturebox")
        self.picture = QtWidgets.QLabel(self.picturebox)
        self.picture.setGeometry(QtCore.QRect(0, 0, 561, 511))
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(530, 10, 20, 621))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scfilebt = QtWidgets.QPushButton(self.centralwidget)
        self.scfilebt.setGeometry(QtCore.QRect(400, 260, 101, 23))
        self.scfilebt.setObjectName("scfilebt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI 全自动词云图生成器"))
        self.Title1.setText(_translate("MainWindow", "AI全自动词云图生成器"))
        self.Title2.setText(_translate("MainWindow", "V1.2 By 官咏颉-学号:20191209"))
        self.label.setText(_translate("MainWindow", "网站URL:"))
        self.previewbt.setText(_translate("MainWindow", "预览网页(打开一个游览器窗口)"))
        self.beginbt.setText(_translate("MainWindow", "开始爬取"))
        self.setting.setTitle(_translate("MainWindow", "高级设置"))
        self.label_2.setText(_translate("MainWindow", "爬取模式："))
        self.label_3.setText(_translate("MainWindow", "分词模式："))
        self.label_4.setText(_translate("MainWindow", "词组数量："))
        # self.NumEdit.setPlaceholderText("75") #设置默认值
        self.mode_choose.setItemText(1, _translate("MainWindow", "BeautifulSoup 爬取网站正文"))
        self.mode_choose.setItemText(0, _translate("MainWindow", "Newspaper AI智能识别正文 (默认)"))
        self.wordorcharacter.setItemText(1, _translate("MainWindow", "字符词云图"))
        self.wordorcharacter.setItemText(0, _translate("MainWindow", "字词词云图"))
        self.previewgroup.setTitle(_translate("MainWindow", "词云图预览:"))
        self.scfilebt.setText(_translate("MainWindow", "选择本地文件"))
        
    def log(self,info):
        QApplication.processEvents() #刷新ui界面,避免线程堵塞造成的卡顿
        self.textBrowser.append(str(info))   #在指定的区域显示提示信息
        self.cursor=self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  #光标移到最后，这样就会自动显示出来
        QApplication.processEvents()

    def clear(self):
        QApplication.processEvents()
        self.textBrowser.clear()   
        self.cursor=self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  #光标移到最后，这样就会自动显示出来
        QApplication.processEvents()
