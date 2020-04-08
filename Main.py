# -*- coding: utf-8 -*-

__author__='gyj2006@foxmail.com'

import sys,os

#该程序UI部分使用PyQt5实现
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import webbrowser

from data.ui.mainwindow import *  #导入预先制作的UI包,在目录./data/ui下(mainwindow.py)

from data.spider import *

from wordcloud import WordCloud

import ctypes

from chardet.universaldetector import UniversalDetector

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("wordcloud_gyj") #解除程序任务栏图标无法显示的问题

'''
简而言之，我的理解就是pyqt是要给python解释的，
也就是说windows在运行的时候认识到的是python，
而你写的程序则被看做是python这个主程序的一个子程序，
这个时候你就要站出来告诉windows，我这个窗口强制使用单独的AppUserModelID ，
现在这个窗口拥有了一个新资源支配权限，更多的可定制。
'''

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling,True) #启用高dpi缩放
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps,True) #使用高dpi图标

app = QApplication(sys.argv)
ui = Ui_MainWindow() #很重要的代码，引入ui对象 故全局定义

#用于检测本地文件的编码,避免出错,使用 chardet 库
def readFile(file_path):
    bigdata = open(file_path,'rb')
    detector = UniversalDetector() #用于判断大文件的编码，效率较高
    for line in bigdata.readlines():    
        detector.feed(line)    
        if detector.done:   #当编码判断准确性较高时，就停止判断         
            break
    detector.close()
    bigdata.close()
    print(detector.result['encoding']) #返回格式是一个字典，我们只需要编码
    ui.log('检测到此文件编码格式为: '+detector.result['encoding'])
    return detector.result['encoding']

#用于生成词云图并保存
def create_wordcloud(_dict):
    if _dict['string'] is not '': #判断分词结果是否为空字符串，结束程序，避免发生错误
        ui.log('正在生成词云图......')
        fontpath='data/font/SourceHanSerifCN-Medium-6.otf'
        wc = WordCloud(font_path=fontpath,  # 设置字体
                background_color="white",  # 背景颜色
                random_state=42,
                scale=4 #图像缩放，增加清晰度
                )
        my_wordcloud = my_wordcloud = wc.generate_from_frequencies(_dict['frequencies']) #由于已经是经过处理的字典格式,可直接生成词云图
        my_wordcloud.to_file('temp.png')
        ui.picture.setPixmap(QPixmap('temp.png')) #读取刚刚生成的词云图，并显示在 picture 容器中
        ui.picture.setScaledContents (True) #设定自动缩放
        ui.log('词云图生成成功!图象已自动保存至 '+os.path.dirname(os.path.abspath(__file__))+'\\temp.png')
        return my_wordcloud
    else: 
        ui.log('Error:检测到无实际内容,可以点击预览按钮查看网站是否正常')
        ui.log('温馨提示:本程序无法爬取部分动态网站,可以尝试其他网站或本地分析')
        return

#预览网页的操作
def on_preview_click():
    print('preview_click')
    URLValue = ui.URLEdit.text()
    if URLValue == '':
        ui.log("Error:URL不能为空")
        return 
    ui.log('预览URL为: '+str(URLValue))
    webbrowser.open(str(URLValue))
    ui.log('已打开默认浏览器')

#网络爬取文档并作词云图的操作
def on_begin_click():
    ui.clear() #于UI_MainWindow类中自写函数，清空ui内控制台的内容
    mode=str(ui.mode_choose.currentText())
    fc_mode=str(ui.wordorcharacter.currentText())
    ui.log('Begin!开始进行程序') #于UI_MainWindow类中自写函数，于ui内控制台输出内容
    ui.log('您选择了: '+mode+' 爬取模式') 
    ui.log('您选择了: '+fc_mode+' 分词模式')

    URLValue = ui.URLEdit.text() #读取输入框中URL
    if URLValue == '':
        ui.log("Error:URL不能为空")
        return 

    ui.log('正在爬取的URL为: '+str(URLValue))

    if mode == 'BeautifulSoup 爬取网站正文 (默认)': #两种不同的爬取模式
        context = bs4spider(URLValue)
    else:
        context = smartspider(URLValue)

    ui.log('爬取成功!')

    ui.log('开始分词......')
    
    Num = int(ui.NumEdit.text()) #获取词组数量
    #进行分词
    result = split(''.join(context),fc_mode,Num) #该函数集成度较高,可以在函数内完成指定模式分词与词组数量
    
    ui.log('分词完成,输出分词结果:')
    ui.log(result['string'])

    create_wordcloud(result)
    
#本地读取文件并建图的操作
def on_load_click():
    fc_mode=str(ui.wordorcharacter.currentText())
    #选取文件并保存路径
    fileName_choose, filetype = QFileDialog.getOpenFileName(None,  
                                "选取文件",  
                                os.path.dirname(os.path.abspath(__file__)), # 起始路径 
                                "文本文档 (*.txt)")   # 设置文件扩展名过滤,用双分号间隔

    if fileName_choose == "":
        print("\n取消选择")
        ui.log("\n取消选择")
        return

    print("\n你选择的文件为:")
    ui.log("\n你选择的文件为:" + fileName_choose)
    print(fileName_choose)

    ui.clear()
    ui.log('Begin!开始进行程序')
    ui.log('读取本地文件: '+str(fileName_choose))
    ui.log('您选择了: '+fc_mode+' 分词模式')
    ui.log('开始分析文档编码...')
    file_encoding = readFile(fileName_choose)
    text = open(fileName_choose,'r',encoding=file_encoding,errors='ignore').read()
    ui.log('读取成功!')

    ui.log('开始分词......')

    print(ui.NumEdit.text())
    Num = int(ui.NumEdit.text()) #获取词组数量
    #进行分词
    result = split(''.join(text),fc_mode,Num) #该函数集成度较高,可以在函数内完成指定模式分词与词组数量

    print(type(result))
    ui.log('分词完成,输出分词结果:')
    ui.log(result['string'])
    print(result['string'])
    
    create_wordcloud(result)
    


if __name__ == '__main__':
    #显示UI界面
    mainWindow = QMainWindow() #建立窗口对象
    
    ui.setupUi(mainWindow) #调用ui初始化函数

    mainWindow.setWindowIcon(QIcon('./data/icon/icon.ico')) #设置 mainWindow 对象的图标

    try:
        #为按钮绑定槽函数，使其可以调用程序功能
        ui.previewbt.clicked.connect(on_preview_click)
        ui.beginbt.clicked.connect(on_begin_click)
        ui.scfilebt.clicked.connect(on_load_click)
    except OSError as err:
        print("OS 错误: {0}".format(err))
        ui.log("OS 错误: {0}".format(err))
    except ValueError:
        print("数值错误！")
        ui.log("数值错误 ValueError！")
    except:
        print("未知错误:", sys.exc_info()[0])
        ui.log("未知错误: ", sys.exc_info()[0])
    #显示窗口
    mainWindow.show()
    #结束程序
    sys.exit(app.exec_())