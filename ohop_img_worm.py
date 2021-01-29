import random
import re

from utils.db import ConnectDatabase

import time
import datetime

from selenium import webdriver


from utils.ip_pool import IpPool
from utils.sleep import TimeSleep
from utils.user_agent import USERAGENT

db = ConnectDatabase('ohop')
# cut = CutImage()
ua = USERAGENT()
te = TimeSleep()
ip = IpPool()


# agency_ = ip.ip_pool()
# agency = ip.ip_pool()
# print(agency['http'])


class Worm(object):
    def __init__(self, num, agency):
        # 驱动参数
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-agent={}'.format(ua.user_agent))
        self.options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
        # self.options.add_argument('--headless')  # 无界面模式
        self.options.add_argument('--disable-gpu')  # 隐藏gpu界面
        self.options.add_argument('--proxy-server=http://{}'.format(agency))  # ip 代理
        self.driver = webdriver.Chrome('C:/Users/qibin/Desktop/chromedriver',
                                       chrome_options=self.options)
        self.url = 'https://api.hzfc.cn/hzfcweb_ifs/interaction/wsslc?p={}'.format(num)

    def window(self, page):
        self.driver.find_element_by_xpath('/html/body/div[3]/div[{}]/ul[1]/li[1]/a'.format(page)).click()
        # driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul[1]/li[1]/a').click()
        # driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul[1]/li[1]/a').click()
        # driver.find_element_by_xpath('/html/body/div[3]/div[4]/ul[1]/li[1]/a').click()
        # driver.find_element_by_xpath('/html/body/div[3]/div[5]/ul[1]/li[1]/a').click()
        # time.sleep(0.5)
        current_windows = self.driver.window_handles
        self.driver.switch_to.window(current_windows[1])
        # driver.switch_to.window(current_windows[2])
        # driver.switch_to.window(current_windows[3])
        # driver.switch_to.window(current_windows[4])
        # driver.switch_to.window(current_windows[5])
        # time.sleep(1)

    def other_house_dong(self):
        try:
            # //a[contains(text(),"幢")]
            pp = self.driver.find_elements_by_xpath('//div[@class="lptypebar"][2]/div/a')
            ppage = len(pp)
        except:
            ppage = 1
        print('这个楼盘有{}页'.format(ppage))
        return ppage

    def scrolltop(self):
        time.sleep(te.random_sleep_time)
        # js = 'scrollTo(0,1000)'
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(1)

    def parse_data(self):
        '''获取名称'''
        try:
            time_str = str(datetime.datetime.now())
            name = ''.join(re.split('[- :.]', time_str))
            print(time_str)
        except:
            name = random.randint(10000, 99999)
        return name

    def save_img(self, name):
        path = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\ohop_image\{}.png'.format(name)
        self.driver.save_screenshot(path)
        # cut.cut_img(path)

    def next_img(self):
        self.driver.find_element_by_xpath('//a[@class="next_page"]').click()

    def close(self):
        self.driver.quit()

    def run(self):
        time.sleep(te.random_sleep_time)
        self.driver.get(self.url)

        page = 1
        while page < 6:
            self.window(page)
            time.sleep(te.random_sleep_time)
            nu = self.other_house_dong()
            for p in range(int(nu)):
                print('当前在{}个楼盘'.format(p))
                try:
                    if p == 1:
                        continue
                    else:
                        # 在这点栋数
                        self.driver.find_element_by_xpath(
                            '//*[@id="tabs-1"]/div[2]/div[2]/div/div[2]/div/a[{}]'.format(p)).click()
                        time.sleep(te.random_sleep_time)
                        self.scrolltop()

                except:
                    print('点不了,莫名其妙的')
                while True:
                    time.sleep(te.random_sleep_time)
                    path = self.parse_data()
                    self.scrolltop()
                    time.sleep(0.5)
                    self.save_img(path)
                    # 下一页
                    try:
                        time.sleep(te.random_sleep_time)
                        self.next_img()
                    except:
                        break
            self.driver.close()
            page += 1
            self.driver.switch_to.window(self.driver.window_handles[0])
            if page == 6:
                break
        self.driver.close()


if __name__ == '__main__':
    for num in range(39, 55):
        # for num in range(25, 25):
        # num = 2
        agency = ip.ip_pool()
        worm = Worm(num, agency)
        print('当前第{}页'.format(num))
        # time.sleep(2.5)
        # worm.run(agency_)
        worm.run()

# 3-8
# 6-2-? ///6-2-5
# 9  19 20-15
