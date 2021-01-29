import os

from PIL import Image
import time


def decorate(fun):
    '''打印函数被调用的时间及调用次数'''
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        start_time = time.time()
        data = fun(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        count += 1
        print("被调用%d次，本次调用花费时间%f秒。" % (count, dt))
        return data

    return wrapper


class CutValueImage(object):
    '''切图'''

    def __init__(self, data):
        self.num = 0
        self.rangle = data
        # print('four: ', rangle)

    @decorate
    def cut_img(self, name, path):
        page = self.num + 1
        try:
            i = Image.open(r'{}'.format(name))
            frame4 = i.crop(self.rangle)
            rgb_im = frame4.convert('RGB')
            rgb_im.save(r'{}'.format(path))
            # os.remove(self.name)
        except Exception as e:
            print(e)
        return print('..图片已修改..当前第{}张'.format(page))


if __name__ == '__main__':
    pass

    pt = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\a\20201205221650251413.png'
    op = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\values\test.png'

    value = (0, 0, 1000, 480)  # 列表页
    CutValueImage(value).cut_img(pt, op)

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
