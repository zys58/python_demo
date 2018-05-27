# _*_codeing:utf-8 _*_

import urllib2,re
from bs4 import BeautifulSoup
import time,socket

# #获取主页源码
fanly_url = "http://zhide.fanli.com/p" # 多页
format_url = "http://zhide.fanli.com/detail/1-" # 商品链接


class Faly():
    def __init__(self):
        self.user_agent = "" #todo
        self.html_data = []

        # 获取主页源码,多页
    def get_html(self,start_page=1,end_page=3):
        for i in range(start_page,end_page+1):
            rt = urllib2.Request(fanly_url+str(i))# 用地址创建一个对象
            rt.add_header('User_Agent',self.user_agent)
            try:
                my_data = urllib2.urlopen(rt).read()# 打开网页，获取源码
                print my_data #获取网页源码
                time.sleep(2)# 停止2秒
                self.html_data.append(my_data)
                socket.setdefaulttimeout(15)# 15秒超时
            except urllib2.URLError,e:
                if hasattr(e,'reason'):# 判断异常是否存在的一个函数
                    print u"链接失败",e.reason
        return str(self.html_data)
# 获取产品的超链接
class GetData():
    def __init__(self):
        self.html = Faly().get_html()# 获取源码
        self.href = []#放6未代码
        self.ls = []
        self.url = []
     # 获取产品超链接
    def get_hrefurl(self):
        reg = r'data-id=''\d{6}'# 商品正则
        result = re.compile(reg)# 编译提高效率
        tag = result.findall(self.html)
        #tag = re.findall(result,self.html)
        #print tag
        for i in tag:
            self.href.append(i)
            print self.href

        # 去重
        reg2 = r"\d{6}"
        result2 = re.findall(reg2.str(self.href))
        if len(result2):
            for data  in result2:
                if data not in self.ls:
                    self.ls.append(data)
                    url = format_url+str(data)#完整的商品链接
                    self.url.append(url)
                    print self.url[-1]
        return self.url
# 获取是产品信息
class Href_mg():
    def __init__(self):
        self.list = GetData().get_hrefurl()#超链
        self.txt_list = []#商品信息
    def show_mg(self):
        for item in range(len(self.list)):
            if len(self.list):
                url = str(self.list[list])
                mg = urllib2.Request(url)
                try:
                    soup = urllib2.urlopen(mg).read()
                    txt = soup.find_all('h1') #找到标签
                    self.txt_list.append(txt)
                    print self.txt_list[-1] #打印商品列表
                except urllib2.URLError,e:
                    print e.reason
        return str(self.txt_list)
if __name__ =="__main__":#判断文件入口
    path = "yaozhi.txt"
    with open(path,'a') as file:
        data = Href_mg().show_mg()# 获取产品内容
        reg4 = r'<.*+>'
        data_s = re.sub(reg4,'',data).replace('全网最低','').replace('[','').replace(']','').replace(',','\n').strip().replace(' ','')
        print data_s
        file.write(data_s)












