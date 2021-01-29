import os

from utils.tess_ocr import OcrImageView


def read_file():
    rootdir = r'.\ohop\1lie'
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
            name_id = basename.split('_')[0]
            # print(name_id)


if __name__ == '__main__':
    pt = r'C:\Users\86138\Desktop\20200905房小团\one_house_one_price\values\20201206034158042270.png'
    tessocr = OcrImageView(pt)
    # print(tessocr)

    a = str(tessocr).split('\n')
    print(a)
