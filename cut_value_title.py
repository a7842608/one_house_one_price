import os
import time

from utils.baidu_ocr_api import BaiduOCR
from utils.db import ConnectDatabase
from utils.ocr_cut_img import CutValueImage

# (int(x), int(y), int(x + w), int(y + h))

# title = (450, 450, 1460, 1000)
# CutValueImage(title).cut_img(p, op)

db = ConnectDatabase('ohop')


def file_list():
    rootdir = r'.\ohop_image\title1'
    # rootdir = r'.\ohop_image'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        # for i in range(3, 4):
        pos = os.path.join(rootdir, list[i])
        # print(pos)
        if os.path.isfile(pos):
            # 你想对文件的操作
            pt = os.path.abspath(pos)
            # print(pt)
            basename = os.path.basename(pos)
            name_id = basename.split('_')[2].split('.')[0]
            print(name_id)

            # op = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\ohop_image\title1\1_t_20201205221650251413.png'
            a = BaiduOCR()
            time.sleep(0.5)
            b = a.run(pt)
            try:
                number = b['words_result'][1]['words']
            except:
                number = ''

            sql = "insert into union_yfyj_title(file_name, parse_number) values('{}','{}');".format(name_id,
                                                                                                    str(number))
            db.run(sql)
    db.close()
    # # op = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\values\{}'.format(basename)
    # op = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\values\{}'.format(basename)
    #
    # value = (0, 0, 1000, 480)  # value
    # CutValueImage(value).cut_img(pt, op)

    # value = (450, 450, 1460, 1000) # 列表页
    # CutValueImage(value).cut_img(pt, op)

    # title = (450, 150, 1460, 400)  # 列头
    # CutValueImage(title).cut_img(pt, op)

    # title = (90, 0, 210, 100)  # pid
    # CutValueImage(title).cut_img(pt, op)

    # title = (90, 100, 1000, 170)  # house_dong
    # CutValueImage(title).cut_img(pt, op)

    # title = (0, 50, 145, 500)  # 1lie
    # CutValueImage(title).cut_img(pt, op)

    # title = (145, 50, 250, 500)  # 2lie
    # CutValueImage(title).cut_img(pt, op)

    # title = (265, 50, 355, 500)  # 3lie
    # CutValueImage(title).cut_img(pt, op)

    # title = (355, 50, 485, 500) # 4lie
    # CutValueImage(title).cut_img(pt, op)

    # title = (455, 50, 585, 500)  # 5lie
    # CutValueImage(title).cut_img(pt, op)

    # title = (575, 50, 690, 500)  # 6lie
    # CutValueImage(title).cut_img(pt, op)

    # title = (740, 50, 865, 500)  # 7lie
    # CutValueImage(title).cut_img(pt, op)

    # title = (880, 50, 985, 500)  # 8lie
    # CutValueImage(title).cut_img(pt, op)


if __name__ == '__main__':
    file_list()
