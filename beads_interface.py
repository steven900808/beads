import tkinter as tk
import numpy as np
from tkinter.constants import RIGHT
from tkinter.ttk import *
import os
from PIL import Image
import matplotlib.pyplot as plt  # pip install matplotlib

location = r'C:\桌面\aot'  # 儲存之txt與圖片檔案位置
picture_location = r'C:\桌面\aot\flower.jpg'  # 開啟圖片之位置
filetext = r'C:\桌面\aot\test.txt'
save_result_text = r'C:\桌面\aot\result.txt'

myarray = np.array([["0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                                                                                                                                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                                                                                                                                                                                                                                                                                                                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                                                                                                                                                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def rgb_to_hex(r, g, b):
    return ('{:X}{:X}{:X}').format(r, g, b)


def cal_a(a):  # 128 192 255
    if a < 255:
        a = int(round(a/10, 0)*10)
    return a


def cal_b(b):
    if b < 255:
        b = int(round(b/10, 0)*10)
    return b


def cal_c(c):
    if c < 255:
        c = int(round(c/10, 0)*10)
    return c


os.chdir(location)  # 圖片路徑
img = Image.open(picture_location).convert("RGB")                # 圖片檔名
# img.save('test.png')                               # 存檔
img_width, img_height = img.size            # 讀取圖片長寬2560 1600
if img_width >= img_height:  # 將照片變為正方形
    new_X = (img_width - img_height)/2
    new_x = img_width - new_X
    new_img = img.crop((new_X, 0, new_x, img_height))
if img_width < img_height:
    new_Y = (img_height - img_width)/2
    new_y = img_height - new_Y
    new_img = img.crop((0, new_Y, img_width, new_y))

new_img = new_img.resize((int(29), int(29)))      # 縮小圖片為29*29
new_img = new_img.resize((29, 29), resample=Image.NEAREST)  # 放大圖檔
# new_img.save('test1.png')                               # 存檔
for y in range(new_img.size[1]):
    for x in range(new_img.size[0]):
        pix = new_img.getpixel((x, y))
        # print(pix)
        a = pix[0]
        b = pix[1]
        c = pix[2]
        # cal_a(a)
        # cal_b(b)
        # cal_c(c)
        first = cal_a(a)
        second = cal_b(b)
        third = cal_c(c)
        # print(first, second, third)
        color = rgb_to_hex(first, second, third)
        if len(color) == 5:
            color = color + "0"
        if len(color) == 4:
            color = color + "00"
        if len(color) == 3:
            color = color + "000"
        (myarray[[y], [x]]) = ("@#") + color
        if x == 0:
            (myarray[[y], [x]]) = (",@#") + color
        if x == 28:
            (myarray[[y], [x]]) = ("@#") + color
    if y == 28:
        (myarray[[y], [x]]) = ("@#") + color


new_img = new_img.resize((1000, 1000), resample=Image.NEAREST)  # 放大圖檔
new_img.save('2929.png')                               # 存檔

# print(myarray)
np.savetxt(filetext, myarray, fmt='%s', delimiter=',')


elements = []
filename = filetext
with open(filename) as file:
    for line in file:
        line = line.strip().split(",@")
        elements.append(line)

ele_array = np.array(elements)
ele_array = np.delete(ele_array, 0, axis=1)  # 刪除第一列''
# print(ele_array)
# print('%s\nshape is %s' % (type(ele_array), ele_array.shape))

a = plt.axes([.18, .1, .65, .8],
             facecolor='k')  # pyplot api 命令-黑色背景
ax1 = plt.gca()
ax1.patch.set_facecolor("grey")    # 设置 ax1 区域背景颜色
ax1.patch.set_alpha(1)    # 设置 ax1 区域背景颜色透明度
plt.title('bead')
plt.xlim(-1, 29)
plt.ylim(29, -1)
labels = ['1', '6', '11', '16', '21', '26']
for y in range(0, 29):
    for x in range(0, 29):
        plt.plot(x, y, marker='o', color='black', markerfacecolor='grey')
'''畫拼豆'''
for y in range(29):
    for x in range(29):
        color = (ele_array[[y], [x]])
        color = ','.join(str(i) for i in color)
        plt.plot(x, y, color=color, marker='o')


plt.xticks(range(0, 29, 5), labels)
plt.yticks(range(0, 29, 5), labels)
plt.show()

num_red = 0
num_blue = 0
num_orange = 0
num_black = 0
num_white = 0

a = np.zeros((29, 29))
selectcolor = ''
elements = []
filename = filetext
with open(filename) as file:
    for line in file:
        line = line.strip().split(",@")
        elements.append(line)
ele_array = np.array(elements)
ele_array = np.delete(ele_array, 0, axis=1)  # 刪除第一列
a = ele_array

b = 0
x = 0.00
y = 0.00
dx = 0
dy = 0

window = tk.Tk()
window.title('主控')
window.geometry('800x600')
window.configure(background='white')


def duelx(x):
    if 0 < x <= 30:
        dx = 0
    elif 30 < x <= 50:
        dx = 1
    elif 50 < x <= 70:
        dx = 2
    elif 70 < x <= 90:
        dx = 3
    elif 90 < x <= 110:
        dx = 4
    elif 110 < x <= 130:
        dx = 5
    elif 130 < x <= 150:
        dx = 6
    elif 150 < x <= 170:
        dx = 7
    elif 170 < x <= 190:
        dx = 8
    elif 190 < x <= 210:
        dx = 9
    elif 210 < x <= 230:
        dx = 10
    elif 230 < x <= 250:
        dx = 11
    elif 250 < x <= 270:
        dx = 12
    elif 270 < x <= 290:
        dx = 13
    elif 290 < x <= 310:
        dx = 14
    elif 310 < x <= 330:
        dx = 15
    elif 330 < x <= 350:
        dx = 16
    elif 350 < x <= 370:
        dx = 17
    elif 370 < x <= 390:
        dx = 18
    elif 390 < x <= 410:
        dx = 19
    elif 410 < x <= 430:
        dx = 20
    elif 430 < x <= 450:
        dx = 21
    elif 450 < x <= 470:
        dx = 22
    elif 470 < x <= 490:
        dx = 23
    elif 490 < x <= 510:
        dx = 24
    elif 510 < x <= 530:
        dx = 25
    elif 530 < x <= 550:
        dx = 26
    elif 550 < x <= 570:
        dx = 27
    elif 570 < x <= 600:
        dx = 28
    return dx


def duely(y):
    if 0 < y <= 30:
        dy = 0
    elif 30 < y <= 50:
        dy = 1
    elif 50 < y <= 70:
        dy = 2
    elif 70 < y <= 90:
        dy = 3
    elif 90 < y <= 110:
        dy = 4
    elif 110 < y <= 130:
        dy = 5
    elif 130 < y <= 150:
        dy = 6
    elif 150 < y <= 170:
        dy = 7
    elif 170 < y <= 190:
        dy = 8
    elif 190 < y <= 210:
        dy = 9
    elif 210 < y <= 230:
        dy = 10
    elif 230 < y <= 250:
        dy = 11
    elif 250 < y <= 270:
        dy = 12
    elif 270 < y <= 290:
        dy = 13
    elif 290 < y <= 310:
        dy = 14
    elif 310 < y <= 330:
        dy = 15
    elif 330 < y <= 350:
        dy = 16
    elif 350 < y <= 370:
        dy = 17
    elif 370 < y <= 390:
        dy = 18
    elif 390 < y <= 410:
        dy = 19
    elif 410 < y <= 430:
        dy = 20
    elif 430 < y <= 450:
        dy = 21
    elif 450 < y <= 470:
        dy = 22
    elif 470 < y <= 490:
        dy = 23
    elif 490 < y <= 510:
        dy = 24
    elif 510 < y <= 530:
        dy = 25
    elif 530 < y <= 550:
        dy = 26
    elif 550 < y <= 570:
        dy = 27
    elif 570 < y <= 600:
        dy = 28
    return dy


def print_aamouse_click(event):
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    canvas.create_oval((dx*20)+10, (dy*20)+10, (dx*20) +
                       30, (dy*20)+30, fill=aa)
    a[dy][dx] = aa
    # a[dy][dx] = 1
    global num_red
    num_red = num_red+1
    numm_red = str(num_red)
    lb_red.config(text="" + numm_red)
    print("填上顏色為：", aa)
    # canvas.bind("<Leave>", buttonbreak)


def print_bbmouse_click(event):
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    canvas.create_oval((dx*20)+10, (dy*20)+10, (dx*20) +
                       30, (dy*20)+30, fill=bb)
    a[dy][dx] = bb
    # a[dy][dx] = 2
    global num_blue
    num_blue = num_blue+1
    numm_blue = str(num_blue)
    lb_blue.config(text="" + numm_blue)
    print("填上顏色為：", bb)
    # canvas.bind("<Leave>", buttonbreak)


def print_ccmouse_click(event):
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    canvas.create_oval((dx*20)+10, (dy*20)+10, (dx*20) +
                       30, (dy*20)+30, fill=cc)
    a[dy][dx] = cc
    # a[dy][dx] = 3
    global num_orange
    num_orange = num_orange+1
    numm_orange = str(num_orange)
    lb_orange.config(text="" + numm_orange)
    print("填上顏色為：", cc)
    # canvas.bind("<Leave>", buttonbreak)


def print_ddmouse_click(event):
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    canvas.create_oval((dx*20)+10, (dy*20)+10, (dx*20) +
                       30, (dy*20)+30, fill='#64C864')
    a[dy][dx] = dd
    # a[dy][dx] = 4
    global num_black
    num_black = num_black+1
    numm_black = str(num_black)
    lb_black.config(text="")
    print("填上顏色為：#64C864")
    # canvas.bind("<Leave>", buttonbreak)


def print_eemouse_click(event):
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    canvas.create_oval((dx*20)+10, (dy*20)+10, (dx*20) +
                       30, (dy*20)+30, fill=ff)
    a[dy][dx] = ee
    # a[dy][dx] = 5
    global num_white
    num_white = num_white+1
    numm_white = str(num_white)
    lb_white.config(text="" + numm_white)
    print("填上顏色為：", ff)
    # canvas.bind("<Leave>", buttonbreak)


def print_selectmouse_click1(event):
    global selectcolor
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    selectcolor = a[dy][dx]
    print("選取顏色為：", a[dy][dx])
    # canvas.bind("<Leave>", buttonbreak)


def print_selectmouse_click2(event):
    global selectcolor
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    # selectcolor = print_selectmouse_click1()
    canvas.create_oval((dx*20)+10, (dy*20)+10, (dx*20) +
                       30, (dy*20)+30, fill=selectcolor)
    # canvas.bind("<Leave>", buttonbreak)
    print("填上顏色為：", selectcolor)


def print_space_button1(event):
    global selectcolor
    x = event.x
    y = event.y
    dx = duelx(x)
    dy = duely(y)
    # selectcolor = print_selectmouse_click1()
    canvas.create_oval((dx*20)+10, (dy*20)+10, (dx*20) +
                       30, (dy*20)+30, fill='white')
    # canvas.bind("<Leave>", buttonbreak)
    a[dy][dx] = 0
    print("填上顏色為：空白",)


def clickaabutton(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_aamouse_click)
    print("目前選取顏色為：", aa)


def clickbbbutton(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_bbmouse_click)
    print("目前選取顏色為：", bb)


def clickccbutton(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_ccmouse_click)
    print("目前選取顏色為：", cc)


def clickddbutton(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_ddmouse_click)
    print("目前選取顏色為：", '#64C864')


def clickeebutton(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_eemouse_click)
    print("目前選取顏色為：", ff)


def clickselect_button1(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_selectmouse_click1)
    print("點擊拼豆點位，做顏色選取")


def clickselect_button2(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_selectmouse_click2)
    print("目前選取顏色為：", selectcolor)


def space_button1(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    canvas.bind("<Button>", print_space_button1)
    print("目前選取顏色為：空白")


def clicksavebutton(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    print(a)
    np.savetxt(save_result_text, a, fmt='%s', delimiter=',')


def clickresetbutton(event):
    key_dict = {1: '左', 2: '中', 3: '右'}
    print(event.type, "單擊了滑鼠{}鍵".format(key_dict[event.num]))
    for k in range(0, 29):
        for l in range(0, 29):
            canvas.create_oval((l*20)+10, (k*20)+10,
                               (l*20)+30, (k*20)+30, fill='gray')
    for k in range(0, 29):
        for l in range(0, 29):
            color = (ele_array[[k], [l+1]])
            color = ','.join(str(i) for i in color)
            # print(color)
            canvas.create_oval((l*20)+10, (k*20)+10, (l*20) +
                               30, (k*20)+30, fill=color)

    global num_red
    global num_blue
    global num_orange
    global num_black
    global num_white
    num_red = 0
    num_blue = 0
    num_orange = 0
    num_black = 0
    num_white = 0

    nummm_red = str(num_red)
    lb_red.config(text="" + nummm_red)
    nummm_blue = str(num_blue)
    lb_blue.config(text="" + nummm_blue)
    nummm_orang = str(num_orange)
    lb_orange.config(text="" + nummm_orang)
    nummm_black = str(num_black)
    lb_black.config(text="" + nummm_black)
    nummm_white = str(num_white)
    lb_white.config(text="" + nummm_white)


canvas = tk.Canvas(window, height=600, width=600, bg='gray')
canvas.place(x=0, y=0)
canvas.create_rectangle(0, 0, 600, 600, width=5)

elements = []
filename = filetext
with open(filename) as file:
    for line in file:
        line = line.strip().split(",@")
        elements.append(line)
ele_array = np.array(elements)
# print('%s\nshape is %s' % (type(ele_array), ele_array.shape))

for k in range(0, 29):
    for l in range(0, 29):
        canvas.create_oval((l*20)+10, (k*20)+10, (l*20)+30, (k*20)+30)

unique, counts = np.unique(ele_array, return_counts=True)
k = (dict(zip(counts, unique)))
# print(sorted(k.items(), key=lambda x: x[1], reverse=True))
result = sorted(k.items(), key=lambda x: x[1], reverse=True)
del result[-1]
result.sort(reverse=True)  # result為所有顏色hex號碼中出現數量最多至最小
print("顏色hex代號出現次數=>", result)
aa = result[1]
bb = result[2]
cc = result[3]
dd = result[4]
ee = result[5]
ff = result[6]
gg = result[7]
a_num = aa[0]
b_num = bb[0]
c_num = cc[0]
d_num = dd[0]
e_num = ee[0]
f_num = ff[0]
g_num = gg[0]
a_num = str(a_num)
aa = aa[1]
bb = bb[1]
cc = cc[1]
dd = dd[1]
ee = ee[1]
ff = ff[1]
gg = gg[1]

lb_red = Label(background="white", foreground="black", text=a_num)
lb_red.config(font="微軟正黑體 20")
lb_red.place(x=650, y=25)

lb_blue = Label(background="white", foreground="black", text=b_num)
lb_blue.config(font="微軟正黑體 20")
lb_blue.place(x=650, y=125)

lb_orange = Label(background="white", foreground="black", text=c_num)
lb_orange.config(font="微軟正黑體 20")
lb_orange.place(x=650, y=200)

lb_black = Label(background="white", foreground="black", text=d_num)
lb_black.config(font="微軟正黑體 20")
lb_black.place(x=650, y=250)

lb_white = Label(background="white", foreground="black", text=e_num)
lb_white.config(font="微軟正黑體 20")
lb_white.place(x=650, y=300)


for k in range(0, 29):
    for l in range(0, 29):
        color = (ele_array[[k], [l+1]])
        color = ','.join(str(i) for i in color)
        # print(color)
        canvas.create_oval((l*20)+10, (k*20)+10, (l*20) +
                           30, (k*20)+30, fill=color)
        # if color == aa:
        #     a[k][l] = 0
        # elif color == bb:
        #     a[k][l] = 2
        # elif color == cc:
        #     a[k][l] = 3
        # elif color == dd:
        #     a[k][l] = 4
        # elif color == ee:
        #     a[k][l] = 5
        # elif color == ff:
        #     a[k][l] = 6
        # if color != (aa or bb or cc or dd or ee or ff or gg):
        #     a[k][l] = 0


redbutton = tk.Button(window, bg=aa, height=5, width=10)
redbutton.place(x=700, y=0)
redbutton.bind("<Button>", clickaabutton)

bluebutton = tk.Button(window, bg=bb, height=5, width=10)
bluebutton.place(x=700, y=100)
bluebutton.bind("<Button>", clickbbbutton)

orangebutton = tk.Button(window, bg=cc, height=2, width=10)
orangebutton.place(x=700, y=200)
orangebutton.bind("<Button>", clickccbutton)

blackbutton = tk.Button(window, bg='#64C864', height=2, width=10)
blackbutton.place(x=700, y=250)
blackbutton.bind("<Button>", clickddbutton)

whitebutton = tk.Button(window, bg=ff, height=2, width=10)
whitebutton.place(x=700, y=300)
whitebutton.bind("<Button>", clickeebutton)


whitebutton = tk.Button(window, bg="grey", height=2, width=10, text='選取')
whitebutton.place(x=700, y=350)
whitebutton.bind("<Button>", clickselect_button1)
whitebutton = tk.Button(window, bg="grey", height=2,
                        width=10, text='選取之\n顏色按鈕')
whitebutton.place(x=700, y=400)
whitebutton.bind("<Button>", clickselect_button2)
whitebutton = tk.Button(window, bg="white", height=2, width=10, text='空白')
whitebutton.place(x=700, y=450)
whitebutton.bind("<Button>", space_button1)

savebutton = tk.Button(window, bg='white', text='save', height=2, width=10)
savebutton.place(x=700, y=500)
savebutton.bind("<Button>", clicksavebutton)

resetbutton = tk.Button(window, bg='white',
                        text='reset', height=2, width=10)
resetbutton.place(x=700, y=550)
resetbutton.bind("<Button>", clickresetbutton)

window.mainloop()
