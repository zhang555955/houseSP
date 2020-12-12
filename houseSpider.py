#coding:utf-8

from urllib import request
from lxml import etree
from time import sleep
from models import House
"""
url = "https://bj.lianjia.com/zufang/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}

req = request.Request(url,headers = headers)

response = request.urlopen(req)

content = response.read().decode()

print(content)


url = "https://bj.lianjia.com/zufang/changping/"

headers = {
    "Referer": "https://bj.lianjia.com/zufang/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}

req = request.Request(url,headers = headers)

response = request.urlopen(req)

content = response.read().decode()

html = etree.HTML(content)

house_list = html.xpath('//ul[@id="house-lst"]/li/div[@class="info-panel"]/h2/a')
for house in house_list:
    attrib = house.attrib
    housename = attrib["title"]
    houseurl = attrib["href"]

    print("%s : %s"%(housename,houseurl))


num = 0
def getHouse(url,refer):
    global num
    headers = {
        "Referer": refer,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    req = request.Request(url,headers = headers)

    response = request.urlopen(req)

    content = response.read().decode()

    html = etree.HTML(content)

    house_list = html.xpath('//ul[@id="house-lst"]/li/div[@class="info-panel"]/h2/a')
    for house in house_list:
        attrib = house.attrib
        housename = attrib["title"]
        houseurl = attrib["href"]

        print("%s : %s"%(housename,houseurl))
        num += 1
if __name__ == "__main__":
    for i in range(1,28):
        if i == 1:
            url = "https://bj.lianjia.com/zufang/changping/"
            refer = "https://bj.lianjia.com/zufang/"
        else:
            refernum = i - 1
            url = "https://bj.lianjia.com/zufang/changping/pg%s/"%i
            refer = "https://bj.lianjia.com/zufang/changping/pg%s/"%refernum
        print("第 %s 页开始爬取"%i)
        getHouse(url,refer)
        sleep(1)
        print("第 %s 页爬取结束"%i)
    print(num)

def getUser(url,refer):

    headers = {
        "Referer": "https://bj.lianjia.com/zufang/changping/pg2/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    req = request.Request(url,headers = headers)

    response = request.urlopen(req)

    content = response.read().decode()

    html = etree.HTML(content)

    user = html.xpath('//div[@class="brokerInfoText"]')[0]

    name = user.xpath('div[@class="brokerName"]/a')[0].text
    pf = user.xpath('div[@class="evaluate"]/span')[0].text
    num = user.xpath('div[@class="evaluate"]/span')[1].text

    print(name)
    print(pf.strip())
    print(num)
"""
num = 0

def getUser(url, refer):
    headers = {
        "Referer": refer,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    req = request.Request(url, headers=headers)

    response = request.urlopen(req)

    content = response.read().decode()

    html = etree.HTML(content)

    user = html.xpath('//div[@class="brokerInfoText"]')[0]

    name = user.xpath('div[@class="brokerName"]/a')[0].text
    pf = user.xpath('div[@class="evaluate"]/span')[0].text
    num = user.xpath('div[@class="evaluate"]/span')[1].text

    print(name)
    print(pf.strip())
    print(num)
    return name,pf.strip(),num

def getHouse(url, refer):
    global num
    headers = {
        "Referer": refer,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    req = request.Request(url, headers=headers)

    response = request.urlopen(req)

    content = response.read().decode()

    html = etree.HTML(content)

    house_list = html.xpath('//ul[@id="house-lst"]/li/div[@class="info-panel"]/h2/a')
    for house in house_list:
        attrib = house.attrib
        housename = attrib["title"]
        houseurl = attrib["href"]
        print("%s : %s" % (housename, houseurl))
        print("%s 开始爬取"%housename)
        name, pf, Num = getUser(houseurl,url)
        print("%s 爬取结束"%housename)
        sleep(1)
        num += 1
        h = House()
        h.houseName = housename
        h.houseUrl = houseurl
        h.houseUser = name
        h.userPF = pf
        h.lookNum = Num
        h.save()


if __name__ == "__main__":
    for i in range(1, 28):
        if i == 1:
            url = "https://bj.lianjia.com/zufang/changping/"
            refer = "https://bj.lianjia.com/zufang/"
        else:
            refernum = i - 1
            url = "https://bj.lianjia.com/zufang/changping/pg%s/" % i
            refer = "https://bj.lianjia.com/zufang/changping/pg%s/" % refernum
        print("第 %s 页开始爬取" % i)
        getHouse(url, refer)
        sleep(1)
        print("第 %s 页爬取结束" % i)
    print(num)


