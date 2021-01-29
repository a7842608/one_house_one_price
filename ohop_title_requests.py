import re
import threading
from lxml import etree

import requests

from utils.db import ConnectDatabase
from utils.ip_pool import IpPool
from utils.sleep import TimeSleep
from utils.user_agent import USERAGENT

db = ConnectDatabase('tuan')
# cut = CutImage()
ua = USERAGENT()
te = TimeSleep()
ip = IpPool()
agency = ip.ip_pool()


# print(agency['http'])

class Worm(object):
    def __init__(self, page):

        self.url = 'https://api.hzfc.cn/hzfcweb_ifs/interaction/wsslc?p={}'.format(page)
        self.headers = {
            'User-Agent': '',
            'Cookie': 'zh_choose_undefined=s; SERVERID=71bfd367a49f5c3316644ab3e3801eff|1606547547|1606544095',
        }
        # self.proxies = ip.ip_pool()
        # self.proxies = {
        #     "http": ip.ip_pool(),
        # }

    def get_data(self):
        # print(self.proxies, '222')
        # resp = requests.get(self.url)
        # print(resp.status_code)
        # print(resp.text)
        # if resp.status_code != 200:
        #     try:
        #         response = requests.get(self.url, headers=self.headers, proxies=self.proxies)
        #         return response.content
        #     except:
        #         print('请求失败')
        #         # return response.content
        # else:
        #     response = requests.get(self.url, headers=self.headers)
        #     return response.content
        response = requests.get(self.url, headers=self.headers)
        return response.content

    def detial_data(self, data):
        data = data.decode()
        html = etree.HTML(data)
        value_list = html.xpath('//a[@title="点击进入详情页"]/@onclick')
        a = [re.split(r'[""]', i)[1] for i in value_list]
        b = ['https://api.hzfc.cn/hzfcweb_ifs/interaction/wsslc_detail_yfyj?id={}'.format(i) for i in a]
        return b

    def parse_data(self, data_list):
        # url = data_list[0]
        url = data_list
        response = requests.get(url, headers=self.headers).content
        html = etree.HTML(response)
        try:
            name = html.xpath('//p[@class="lp-fl"]/text()')[0]
        except:
            name = '空'
        try:
            use = html.xpath('//p[@class="ico1"]/span/text()')[0]
        except:
            use = '空'
        try:
            numberno = html.xpath('//p[@class="ico2"]/span/text()')[0]
            number_list = numberno.split(',')
            number = number_list[0]
        except:
            number = '空'
        try:
            adress = html.xpath('//p[@class="ico3"]/span/text()')[0]
        except:
            adress = '空'
        try:
            company = html.xpath('//p[@class="ico4"]/span/text()')[0]
        except:
            company = '空'
        try:
            housed = html.xpath('//div[@class="buildshow03 ggduhin"]/div/div[2]/div')[0].xpath('string(.)')
            tt = housed.replace('\r\n', '').replace(' ', '').replace('号', ',').replace('楼', '').replace('幢', ',')
        except:
            tt = '空'
        # return name, use, number, adress, company, housed
        return str(name), str(use), str(number), str(adress), company, tt

    def save_data(self, name, use, number, adress, company, housed):
        print(name, use, number, adress, company, housed)
        sql = "insert into ohop_start_value(na_me,use_cla,number,adress,company,house_dong) values('%s', '%s', '%s', '%s', '%s', '%s');" % (
        name, use, number, adress, company, housed)
        db.run(sql)

    def run(self):
        response = self.get_data()
        data_list = self.detial_data(response)
        for i in data_list:
            a, b, c, d, e, f = self.parse_data(i)
            self.save_data(a, b, c, d, e, f)
        # a, b, c, d, e, f = self.parse_data(data_list[0])
        # self.save_data(a, b, c, d, e, f)


if __name__ == '__main__':
    for i in range(1, 60):
        agency = ip.ip_pool()
        worm = Worm(i)
        worm.run()

    # worm = Worm(1)
    # worm.run()
    # db.close()
