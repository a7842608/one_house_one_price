# encoding:utf-8
import json

import requests
import base64


class BaiduOCR(object):
    '''百度ocr'''

    def __init__(self):
        self.appid = '23103487'
        self.api_key = '5jsOaxnRpsmfainDWf4K2XlE'
        self.secret_key = 'Wyo3Q1g7zBG7g4B0brGvksz0RlHmVOEu'
        # self.access_token = '24.42b3e9ecc01559bcb8a1db2e5635df71.2592000.1609678248.282335-23099643'
        self.host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            self.api_key, self.secret_key)

    # def get_token(self):
    #     response = requests.get(self.host)
    #     if response:
    #         actoken = response.json()
    #         print(actoken)
    #         return actoken['access_token']

    # def get(self, img, token):
    def get(self, img):
        token = '24.c18eaeb5a78052580b44865c670d7347.2592000.1609762174.282335-23103487'
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token={}".format(token)
        params = {"image": img}
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            return response.json()

    def file(self, path):
        # def file(self):
        #     path = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\baidu_cut_image\test.png'
        # 二进制方式打开图片文件
        f = open(path, 'rb')
        img = base64.b64encode(f.read())
        return img

    def run(self, path):
        # def run(self):
        #     token = self.get_token()
        data = self.file(path)
        # data = self.file()
        a = self.get(data)
        return a


if __name__ == '__main__':
    pass
    # pt = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\ohop_image\title2\2_t_20201205221650251413.png'
    # ip = r'C:\Users\86138\Desktop\20200905房小团\ohop\img\20201204182606339231.png'
    # a = BaiduOCR()
    # b = a.run(pt)
    # print(b['words_result'])

    l = [{'words': '幢号:'}, {'words': '2930'}, {'words': '31'}, {'words': '32'}]
    a = [i['words'] for i in l]
    print(a)
