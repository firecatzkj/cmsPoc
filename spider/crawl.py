# -*- coding: utf-8 -*-
import requests
import random
from lxml import etree


class MySpider:
    def __init__(self, keyword):
        self.keyword = keyword
        self.user_agent = open("user-Agent", "r+").readlines()

    def record(self, url):
        with open("url.txt", "a+") as f:
            f.write(url + "\n")

    def getheader(self):
        flag = random.randint(1, len(self.user_agent) - 1)
        current_agent = str(self.user_agent[flag]).strip()
        return current_agent

    def crawl(self, url):
        sess = requests.session()
        sess.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": "www.baidu.com",
            # "User-Agent": self.getheader(),
            "User-Agent": "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        return sess.get(url, timeout=10 )

    def run(self):
        base_url = "https://www.baidu.com/s?wd={}&pn={}"
        link_xpath = '//*[@id="{}"]/h3/a/@href'
        for i in range(0, 500, 10):
            current_url = base_url.format(self.keyword, i)
            #print(current_url)
            content = self.crawl(current_url).text
            # print(content)
            for j in range(i, i + 11, 1):
                c_xpath = link_xpath.format(j)
                #print(c_xpath)
                root = etree.HTML(content)
                res = root.xpath(c_xpath)
                #print(res)
                if len(res) == 0:
                    continue
                else:
                    bd_url = res[0]
                    try:
                        true_rul = self.crawl(bd_url).url
                        print(true_rul)
                        self.record(true_rul)
                    except Exception as e:
                        print("error: ", e)

if __name__ == '__main__':
    aaa = MySpider("inurl: 'index.php?m=content'")
    aaa.run()






