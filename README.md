# AIWordcloud

图形化词云图生成软件，整合了网络爬虫功能  

UI使用 `PyQt5` 设计实现, `BeautifulSoup` + `Newspaper` 双模爬虫引擎, 可根据网站内容方便切换, `jieba` 中文分词, `wordcloud` 生成词云图

可以一键式生成 *~~专业品质~~* 的词云图  

**效果展示** (镜花缘全集):  
![](temp.png)

**Pyinstall 推荐打包命令:**  
`pyinstaller Main.py -i M:\AIWordcloud(GUI)\data\icon\icon.ico -w --exclude-module PySide2 --exclude-module nltk`

**已知问题:**
```
- 无法通过一键爬取动态网页的内容，暂时手动需复制后利用本地功能生成图片
- 通过本地TXT生成词云图可能会出现卡顿，因为程序要分析文本的编码格式后再开始生成
- 一些奔溃或错误
```
---
当前版本 1.2  
