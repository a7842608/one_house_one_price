# coding=utf-8

import time
import random

from selenium import webdriver

from utils.db import ConnectDatabase
from utils.ip_pool import IpPool
from utils.user_agent import USERAGENT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

f = open('log.txt', 'a+', encoding='utf-8')

database = 'ohop'
db = ConnectDatabase(database)
ua = USERAGENT()
ip = IpPool()

'''
:param
一房一价 列头
'''


class TitleWorm(object):
    def __init__(self, num, agency):

        print('当前第:[ %d ]页' % i)
        # 驱动参数
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-agent={}'.format(ua.user_agent))
        self.options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
        self.options.add_argument('--headless')  # 无界面模式
        self.options.add_argument('--disable-gpu')  # 隐藏gpu界面
        self.options.add_argument('--proxy-server=http://{}'.format(agency))  # ip 代理
        self.driver = webdriver.Chrome('C:/Users/qibin/Desktop/chromedriver',
                                       chrome_options=self.options)
        # self.url = 'http://fgj.hangzhou.gov.cn/col/col1229404539/index.html'
        self.url = 'https://api.hzfc.cn/hzfcweb_ifs/interaction/ysspgg?p={}'.format(num)
        self.page = num

    def parse(self):
        for n in range(1, 16):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div/ul/div/div/li[{}]/a'.format(n)))
                )
            except TimeoutException as e:
                f.write(str(e) + '\n' + '第{}页'.format(self.page) + '第{}条'.format(n))
                continue
            else:
                element.click()  # 1-16
                # 1. 获取当前所有的标签页的句柄构成的列表
                # 2. 根据标签页句柄列表索引下标进行切换
                current_windows = self.driver.window_handles
                self.driver.switch_to.window(current_windows[1])

            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div[3]/p'))
                )
            except TimeoutException as e:
                f.write(str(e) + '\n' + '第{}页'.format(self.page) + '第{}条'.format(n))
                continue
            else:
                v_title = element.text

            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div[3]/div/div[2]/table/tbody/tr[2]'))
                )
            except TimeoutException as e:
                f.write(str(e) + '\n' + '第{}条'.format(n))
                continue
            else:
                # '开发公司', '开发项目名', '房屋坐落位置', '用途', '预售证号', '公示日期', '核发日期'
                t_value = self.driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr[2]/td')
                a = [i.text for i in t_value]
                # ['杭州港中旅钱江城市发展有限公司', '杭政储出[2018]61号地块商品住宅（设配套公建）8#、16#楼', '归锦府8幢、16幢', '住宅', '2020000129',
                # '2020-11-17', '2020-11-20']
            try:
                sql = "insert into ohop_title(build_company, house_project, house_position, house_use, will_sale_number, public_date, give_date, lottery_title) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                    str(a[0]), str(a[1]), str(a[2]), str(a[3]), str(a[4]), str(a[5]), str(a[6]), str(v_title))
            except IndexError as e:
                f.write(str(e) + '\n' + '第{}页'.format(self.page) + '第{}条'.format(n))
                continue
            else:
                print('当前第:[ %d ] 条' % n)
                print(a)
                db.run(sql)
                self.driver.close()
                self.driver.switch_to.window(current_windows[0])

    def quit(self):

        self.driver.quit()

    def run(self):
        self.driver.get(self.url)
        self.parse()
        self.quit()


if __name__ == '__main__':
    for i in range(1, 64):
        agency = ip.ip_pool()
        worm = TitleWorm(i, agency)
        worm.run()
    f.close()
    db.close()
