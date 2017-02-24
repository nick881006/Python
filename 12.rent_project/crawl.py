#coding=utf-8
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv

url="http://sh.58.com/pinpaigongyu/pn/{page}/?minprice=3000_5000"

#已完成的页数序号，初时为0
page=0

# 打开rent.csv文件
csv_file = open("rent.csv","wb")
# 创建writer对象，指定文件与分隔符
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print "fetch: ", url.format(page=page)
    # 抓取目标页面
    response = requests.get(url.format(page=page))
    # 创建一个BeautifulSoup对象
    html = BeautifulSoup(response.text)
    # 获取class=list的元素下的所有li元素
    house_list = html.select(".list > li")

    # 循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        # 得到标签包裹着的文本
        house_title = house.select("h2")[0].string.encode("utf8")
        # urljoin得到完整的url地址, 得到标签内属性的值
        house_url = urljoin(url, house.select("a")[0]["href"])
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string.encode("utf8")

        # 写数据
        csv_writer.writerow([house_title, house_location, house_money, house_url])

# 关闭文件
csv_file.close()