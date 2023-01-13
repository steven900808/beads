# 關閉程式都用ui中的關閉程式不然就要關掉整個terminal
from sqlite3 import Time
import numpy as np
import tkinter as tk
from matplotlib import pyplot as plt
import os
import sys
from calendar import c
from operator import mod, ne
from pickle import FALSE
from tkinter import TRUE
import numpy as np
from ctypes import *
import time
import binascii
from calendar import c
import numpy as np
from ctypes import *
import time
orgspeedsetting = 100  # 手臂移動速度
orgaccelerationsetting = 80  # 手臂移動加速度
timesleep = 0.8  # 手臂移動每個點位時間間隔

delay = 0.33  # delay plate
#################################### 測試時註解##########################################################################測試時註解###############################################################
# 連接arduino之序列副設定
# s=serial.Serial("/dev/ttyACM0",9600)

################################### 測試時註解##########################################################################測試時註解###############################################################
# 手臂移動程式設定
# so_file = "/home/showmay/HIWIN/Modbus_Hiwin/src/libmodbus_ROS/src/My_test/Hiwin_API.so"
# modbus = CDLL(so_file)
# modbus.DO.argtypes = [c_int, c_int]
# modbus.PTP.argtypes = [c_int, c_int, c_int, c_int, c_int]
# modbus.libModbus_Connect()
# modbus.Holding_Registers_init()
# def PTP_Move_org(Point, speed=orgspeedsetting, acceleration=orgaccelerationsetting, ):
#     C_PTP_XYZ = (c_double * len(Point))(*Point)         # C Array
#     modbus.PTP(1, speed, acceleration, 0, 0, C_PTP_XYZ)  #toolbase
#     modbus.Arm_State_REGISTERS()
#     time.sleep(0.2)
#     modbus.Arm_State_REGISTERS()
#     modbus.Arm_State_REGISTERS()
#     while 1:
#         if(modbus.Arm_State_REGISTERS() == 1):
#             break
#################################### 測試時註解##########################################################################測試時註解###############################################################
'''
cd "/home/showmay/HIWIN/Modbus_Hiwin/src/libmodbus_ROS/src/My_test"   
'''
base_point = [[0],  # org座標系的原點[0]
              [-15.591, 481.798, 260.271, 66.848, 3.720,
                  83.702],  # 側邊傾斜裝填org[1] 手臂預設座標，寫死ㄉ
              [0, 368, 293.5, -180, 0, 90]  # 手臂回正org[2] 手臂預設座標，寫死ㄉ

              ]

firstA_insert = -180
firstB_insert = -3
firstC_insert = 90

result_movex = 0
result_movey = 0
final_X = 0
final_Y = 0

firstplace_X = 0
firstplace_Y = 0
firstplace_Z = 0
firstplace_A = 0
firstplace_B = 0
firstplace_C = 0

irstplace_X_zero = 0
firstplace_Y_zero = 0
firstplace_Z_zero = 0
firstplace_A_zero = 0
firstplace_B_zero = 0
firstplace_C_zero = 0

first_place = [firstplace_X, firstplace_Y, firstplace_Z,
               firstplace_A, firstplace_B, firstplace_C]

first_place[0] = firstplace_X
first_place[1] = firstplace_Y
first_place[2] = firstplace_Z
first_place[3] = firstplace_A
first_place[4] = firstplace_B
first_place[5] = firstplace_C

count_palte = [0, 0, 0, 0, 0]


def entryxy():  # 校正點位txt儲存
    global result_movex
    global result_movey
    global firstplace_X
    global firstplace_Y
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)

    movex = float(varx.get())
    movey = float(vary.get())
    result_movex = ((movex-firstplace_X)-140)/28
    result_movey = ((firstplace_Y-movey)-140)/28
    print("校正後之點位X:", movex, "\t", "第一點位X:", firstplace_X, "\t", "計算：", result_movex, "\t",
          "\n", "第一點位Y:", firstplace_Y, "\t", "校正後之點位Y:", movey, "\t", "計算：", result_movey, "\n")
    result_movex = str(result_movex)
    result_movey = str(result_movey)
    with open('/home/showmay/Desktop/simulatoer_test/move_result.txt', 'w') as z:
        z.write(result_movex)
        z.write("\n")
        z.write(result_movey)
        z.write("\n")


def entryxy_zero():  # 校正點位txt儲存
    global result_movex_zero
    global result_movey_zero
    global firstplace_X_zero
    global firstplace_Y_zero
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X_zero = line[0]
        firstplace_Y_zero = line[1]
        print(firstplace_X_zero, firstplace_Y_zero)
        firstplace_X_zero = float(firstplace_X_zero)
        firstplace_Y_zero = float(firstplace_Y_zero)

    movex_zero = float(varx_zero.get())
    movey_zero = float(vary_zero.get())
    result_movex_zero = ((movex_zero-firstplace_X_zero)-140)/28
    result_movey_zero = ((firstplace_Y_zero-movey_zero)-140)/28
    print("校正後之點位X:", movex_zero, "\t", "第一點位X:", firstplace_X_zero, "\t", "計算：", result_movex_zero, "\t",
          "\n", "第一點位Y:", firstplace_Y_zero, "\t", "校正後之點位Y:", movey_zero, "\t", "計算：", result_movey_zero, "\n")
    result_movex_zero = str(result_movex_zero)
    result_movey_zero = str(result_movey_zero)
    with open('/home/showmay/Desktop/simulatoer_test/move_zero_result.txt', 'w') as z:
        z.write(result_movex_zero)
        z.write("\n")
        z.write(result_movey_zero)
        z.write("\n")


def entryfirstplace():  # 點位txt讀取b軸-3
    global var_firstplacex
    global var_firstplacey
    global var_firstplacez

    global firstplace_X
    global firstplace_Y
    global firstplace_Z
    global firstplace_A
    global firstplace_B
    global firstplace_C

    var_firstplacex = float(var_firstx.get())
    var_firstplacey = float(var_firsty.get())
    var_firstplacez = float(var_firstz.get())

    var_firstplaceA = float(var_firstA.get())
    var_firstplaceB = float(var_firstB.get())
    var_firstplaceC = float(var_firstC.get())

    var_firstplacex = str(var_firstplacex)
    var_firstplacey = str(var_firstplacey)
    var_firstplacez = str(var_firstplacez)

    var_firstplaceA = str(var_firstplaceA)
    var_firstplaceB = str(var_firstplaceB)
    var_firstplaceC = str(var_firstplaceC)
    print(var_firstplacex, var_firstplacey, var_firstplacez,
          var_firstplaceA, var_firstplaceB, var_firstplaceC)
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_result.txt', 'w') as z:
        z.write(var_firstplacex)
        z.write("\n")
        z.write(var_firstplacey)
        z.write("\n")
        z.write(var_firstplacez)
        z.write("\n")
        z.write(var_firstplaceA)
        z.write("\n")
        z.write(var_firstplaceB)
        z.write("\n")
        z.write(var_firstplaceC)
        z.write("\n")
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)


def entryfirstplace_zero():  # 點位txt讀取b軸0
    global var_firstplacex_zero
    global var_firstplacey_zero
    global var_firstplacez_zero

    global firstplace_X_zero
    global firstplace_Y_zero
    global firstplace_Z_zero
    global firstplace_A_zero
    global firstplace_B_zero
    global firstplace_C_zero

    var_firstplacex_zero = float(var_firstx_zero.get())
    var_firstplacey_zero = float(var_firsty_zero.get())
    var_firstplacez_zero = float(var_firstz_zero.get())
    var_firstplacez_zero = var_firstplacez_zero+0.3
    var_firstplaceA_zero = float(var_firstA_zero.get())
    var_firstplaceB_zero = float(var_firstB_zero.get())
    var_firstplaceC_zero = float(var_firstC_zero.get())

    var_firstplacex_zero = str(var_firstplacex_zero)
    var_firstplacey_zero = str(var_firstplacey_zero)
    var_firstplacez_zero = str(var_firstplacez_zero)

    var_firstplaceA_zero = str(var_firstplaceA_zero)
    var_firstplaceB_zero = str(var_firstplaceB_zero)
    var_firstplaceC_zero = str(var_firstplaceC_zero)

    print(var_firstplacex_zero, var_firstplacey_zero, var_firstplacez_zero,
          var_firstplaceA_zero, var_firstplaceB_zero, var_firstplaceC_zero)
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'w') as z:
        z.write(var_firstplacex_zero)
        z.write("\n")
        z.write(var_firstplacey_zero)
        z.write("\n")
        z.write(var_firstplacez_zero)
        z.write("\n")
        z.write(var_firstplaceA_zero)
        z.write("\n")
        z.write(var_firstplaceB_zero)
        z.write("\n")
        z.write(var_firstplaceC_zero)
        z.write("\n")
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X_zero = line[0]
        firstplace_Y_zero = line[1]
        firstplace_Z_zero = line[2]
        firstplace_A_zero = line[3]
        firstplace_B_zero = line[4]
        firstplace_C_zero = line[5]
        firstplace_X_zero = float(firstplace_X_zero)
        firstplace_Y_zero = float(firstplace_Y_zero)
        firstplace_Z_zero = float(firstplace_Z_zero)
        firstplace_A_zero = float(firstplace_A_zero)
        firstplace_B_zero = float(firstplace_B_zero)
        firstplace_C_zero = float(firstplace_C_zero)

# 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555


def main_fiveplatebutton(event):  # ui中主程式(主程式排五拼豆) 進行點位移動
    s.write('I'.encode())
    s.write('I'.encode())
    global move_amount
    global timesleep
    move_amount = 1
    global i
    global j
    global result_movex
    global result_movey
    global final_X
    global final_Y
    with open('/home/showmay/Desktop/simulatoer_test/move_result.txt', 'r') as x:
        line = x.readlines()
        final_X = line[0]
        final_Y = line[1]
        print(final_X, "\n", final_Y)
        final_X = float(final_X)
        final_Y = float(final_Y)
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)
    for i in range(0, 29):  # y
        for j in range(0, 29):  # x
            ############################################################################################################
            # 抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point
            first_place = [firstplace_X, firstplace_Y, firstplace_Z +
                           5, firstplace_A, firstplace_B, firstplace_C]
            # point_invariant=[189.062, 182.890, 154.5, -180, 0 , 90]  #用第一點位計算須移動之點位＝base_point[3]
            ############################################################################################################
            # 抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point
            new_point = first_place
            if (myArray[i][j] != 0):
                myservo8 = myArray[[i], [j]]
                myservo9 = myArray[[i], [j+2]]
                myservo10 = myArray[[i], [j+4]]
                myservo11 = myArray[[i], [j+6]]
                myservo12 = myArray[[i], [j+8]]
                plt.show(block=False)
                new_point[0] = (new_point[0] + (j*5+final_X*i))  # 檢查是否減少誤差
                new_point[1] = (new_point[1] - (i*5+final_Y*j))

                if ((j % 2 == 1) and (i % 2 == 1)):
                    print("本次移動為第", move_amount, "次")
                    draw_fiveplate(new_point)
                    print(
                        "手臂已移動至定點=======================================================>", new_point)
                    move_amount += 1
                    myArray[[i], [j, j+2, j+4, j+6, j+8]] = 0
                    putdown_updown_fiveplate(
                        new_point, myservo8, myservo9, myservo10, myservo11, myservo12, count_palte, j, i)
                if ((j % 2 == 0) and (i % 2 == 0)):
                    print("本次移動為第", move_amount, "次")
                    draw_fiveplate(new_point)
                    print(
                        "手臂已移動至定點=======================================================>", new_point)
                    move_amount += 1
                    myArray[[i], [j, j+2, j+4, j+6, j+8]] = 0
                    putdown_updown_fiveplate(
                        new_point, myservo8, myservo9, myservo10, myservo11, myservo12, count_palte, j, i)

    with open('/home/showmay/Desktop/simulatoer_test/move_zero_result.txt', 'r') as x:
        line = x.readlines()
        final_X = line[0]
        final_Y = line[1]
        print(final_X, "\n", final_Y)
        final_X = float(final_X)
        final_Y = float(final_Y)
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)
    for i in range(29, 0, -1):
        for j in range(0, 29):
            first_place = [
                firstplace_X, (firstplace_Y), (firstplace_Z+5), firstplace_A, (firstplace_B), firstplace_C]
            new_point = first_place
            # 程式判斷從第一點位起當遇到地一個不為零的數字，便取出其後共5個數字成為myservo馬達所需轉動對象。若下屆比賽需更改為不分色擺放，將if (myArray[i][j] != 0)變成if (myArray[i][j] == 1然後繼續往下面改拼豆擺放的指令就好
            if (myArray[i][j] != 0):
                myservo8 = myArray[[i], [j]]
                myservo9 = myArray[[i], [j+2]]
                myservo10 = myArray[[i], [j+4]]
                myservo11 = myArray[[i], [j+6]]
                myservo12 = myArray[[i], [j+8]]
                plt.show(block=False)
                new_point[0] = (new_point[0] + (j*5+final_X*i))  # 檢查是否減少誤差
                new_point[1] = (new_point[1] - (i*5+final_Y*j))
                print("本次移動為第", move_amount, "次")
                draw_fiveplate(new_point)
                print(
                    "手臂已移動至定點=======================================================>", new_point)
                move_amount += 1
                # 當擺放完成後便將拼豆矩陣此次擺放拚豆，更改為零，ex:此次拼豆擺放[[3],[1],[3],[0],[5]]則擺放完成變為[[0],[0],[0],[0],[0]]
                myArray[[i], [j, j+2, j+4, j+6, j+8]] = 0
                putdown_updown_fiveplate(
                    new_point, myservo8, myservo9, myservo10, myservo11, myservo12, count_palte, j, i)
    print("結束")
# 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555


def putdown_updown_fiveplate(new_point, myservo8, myservo9, myservo10, myservo11, myservo12, count_palte, j, i):  # 點位移動後進行拼豆擺放
    global timesleep
    global sleep
    global delay
    new_point[2] = new_point[2]-5
    if count_palte[0] > 48:  # i==y,j==x
        if i > 5 and i <= 25:
            if j > 10 and j <= 16:
                new_point[2] = new_point[2]+0.5
    if count_palte[0] == 0:
        PTP_Move_org(new_point)
        print("0")
    PTP_Move_org(new_point)
    print("checkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", new_point)
    if count_palte[0] == 0:
        time.sleep(1)
    print("  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩ ",
          new_point, "\n", myservo8, myservo9, myservo10, myservo11, myservo12)
    # 轉到出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口
    if myservo8 != 0 and myservo9 != 0 and myservo10 != 0 and myservo11 != 0 and myservo12 != 0:
        print('5                               8，9，10，11，12')  # print表須掉落
        sleep = timesleep+(delay*5)
        s.write('5'.encode())  # 回傳代號自行設定
        count_palte[0] = count_palte[0]+1
        count_palte[1] = count_palte[1]+1
        count_palte[2] = count_palte[2]+1
        count_palte[3] = count_palte[3]+1
        count_palte[4] = count_palte[4]+1
    if myservo8 != 0 and myservo9 != 0 and myservo10 != 0 and myservo11 != 0 and myservo12 == 0:
        print('4                               8，9，10，11')
        s.write('4'.encode())
        sleep = timesleep+(delay*4)
        count_palte[0] = count_palte[0]+1
        count_palte[1] = count_palte[1]+1
        count_palte[2] = count_palte[2]+1
        count_palte[3] = count_palte[3]+1
    if myservo8 != 0 and myservo9 != 0 and myservo10 != 0 and myservo11 == 0 and myservo12 == 0:
        print('3                               8，9，10')
        s.write('3'.encode())
        sleep = timesleep+(delay*3)
        count_palte[0] = count_palte[0]+1
        count_palte[1] = count_palte[1]+1
        count_palte[2] = count_palte[2]+1
    if myservo8 != 0 and myservo9 != 0 and myservo10 == 0 and myservo11 == 0 and myservo12 == 0:
        print('2                               8，9')
        s.write('2'.encode())
        sleep = timesleep+(delay*2)
        count_palte[0] = count_palte[0]+1
        count_palte[1] = count_palte[1]+1
    if myservo8 != 0 and myservo9 == 0 and myservo10 == 0 and myservo11 == 0 and myservo12 == 0:
        print('1                               8')
        s.write('1'.encode())
        sleep = timesleep+(delay*1.5)
        count_palte[0] = count_palte[0]+1
    if myservo8 != 0 and myservo9 != 0 and myservo10 == 0 and myservo11 == 0 and myservo12 != 0:
        print('6                               8，9，12')
        s.write('6'.encode())
        sleep = timesleep+(delay*4)
        count_palte[0] = count_palte[0]+1
        count_palte[1] = count_palte[1]+1
        count_palte[4] = count_palte[4]+1
    if myservo8 != 0 and myservo9 != 0 and myservo10 == 0 and myservo11 != 0 and myservo12 != 0:
        print('7                               8，9，11，12')
        s.write('7'.encode())
        sleep = timesleep+(delay*4.5)
        count_palte[0] = count_palte[0]+1
        count_palte[1] = count_palte[1]+1
        count_palte[3] = count_palte[3]+1
        count_palte[4] = count_palte[4]+1
    print("第八轉盤共轉", count_palte[0])
    print("第九轉盤共轉", count_palte[1])
    print("第十轉盤共轉", count_palte[2])
    print("第十一轉盤共轉", count_palte[3])
    print("第十二轉盤共轉", count_palte[4])
    print("轉動轉盤放置拼鬥")
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", sleep)
    plt.pause(sleep)
    if count_palte[0] < 48:  # 全部轉回入口轉回入口轉回入口轉回入口轉回入口轉回入口11111111111111111
        print('入口：11111（D）')
        s.write('I'.encode())
        time.sleep(0.2)
    else:
        print('入口：22221（d）')
        s.write('i'.encode())

    if count_palte[0] > 48:
        timesleep = 1
        new_point[0] = new_point[0] + 1.6
        PTP_Move_org(new_point, speed=100, acceleration=100)
        new_point[0] = new_point[0] - 3.2
        PTP_Move_org(new_point, speed=100, acceleration=100)
        new_point[0] = new_point[0] + 1.6
        PTP_Move_org(new_point, speed=100, acceleration=100)
        new_point[1] = new_point[1] + 1.6
        PTP_Move_org(new_point, speed=100, acceleration=100)
        new_point[1] = new_point[1] - 3.2
        PTP_Move_org(new_point, speed=100, acceleration=100)
        new_point[1] = new_point[1] + 1.6

    new_point[2] = new_point[2]+5
    PTP_Move_org(new_point)
    print("  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧ ", new_point)
# testttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt


def test_fiveplatebutton(event):     # ui中主程式(測試矩陣) 進行點位移動測試
    global move_amount
    move_amount = 1
    global i
    global j
    global result_movex
    global result_movey
    global final_X
    global final_Y
    with open('/home/showmay/Desktop/simulatoer_test/move_result.txt', 'r') as x:
        line = x.readlines()
        final_X = line[0]
        final_Y = line[1]
        print(final_X, "\n", final_Y)
        final_X = float(final_X)
        final_Y = float(final_Y)
    for i in range(0, 29):
        for j in range(0, 29):
            with open('/home/showmay/Desktop/simulatoer_test/XYZ_result.txt', 'r') as x:
                line = x.readlines()
                firstplace_X = line[0]
                firstplace_Y = line[1]
                firstplace_Z = line[2]
                firstplace_A = line[3]
                firstplace_B = line[4]
                firstplace_C = line[5]
                firstplace_X = float(firstplace_X)
                firstplace_Y = float(firstplace_Y)
                firstplace_Z = float(firstplace_Z)
                firstplace_A = float(firstplace_A)
                firstplace_B = float(firstplace_B)
                firstplace_C = float(firstplace_C)
            ############################################################################################################
            # 抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point
            first_place = [
                firstplace_X, (firstplace_Y), (firstplace_Z), firstplace_A, (firstplace_B), firstplace_C]
            ############################################################################################################
            # 抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point#抬高大於base_point
            first_place[2] = first_place[2]+5
            new_point = first_place
            if (myArray_test[i][j] != 0):
                plt.show(block=False)
                new_point[0] = (new_point[0] + (j*5+final_X*i))  # 檢查是否減少誤差
                new_point[1] = (new_point[1] - (i*5+final_Y*j))
                if ((j % 2 == 0) and (i % 2 == 0)):
                    print("本次移動為第", move_amount, "次")
                    PTP_Move_org(new_point)
                    print(
                        "手臂已移動至定點=======================================================>", new_point)
                    move_amount += 1
                    myArray_test[[i], [j, j+2, j+4, j+6, j+8]] = 0
                    putdown_updown_fiveplate_test(new_point)
    with open('/home/showmay/Desktop/simulatoer_test/move_zero_result.txt', 'r') as x:
        line = x.readlines()
        final_X = line[0]
        final_Y = line[1]
        print(final_X, "\n", final_Y)
        final_X = float(final_X)
        final_Y = float(final_Y)
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)
    for i in range(29, 0, -1):
        for j in range(0, 29):
            first_place = [
                firstplace_X, (firstplace_Y), (firstplace_Z+5), firstplace_A, (firstplace_B), firstplace_C]
            new_point = first_place
            if (myArray_test[i][j] != 0):
                plt.show(block=False)
                new_point[0] = (new_point[0] + (j*5+final_X*i))  # 檢查是否減少誤差
                new_point[1] = (new_point[1] - (i*5+final_Y*j))
                print("本次移動為第", move_amount, "次")
                PTP_Move_org(new_point)
                print(
                    "手臂已移動至定點=======================================================>", new_point)
                move_amount += 1
                print([i], [j, j+2, j+4, j+6, j+8])
                myArray_test[[i], [j, j+2, j+4, j+6, j+8]] = 0
                putdown_updown_fiveplate_test(new_point)
    print("end")


def putdown_updown_fiveplate_test(new_point):  # 測試矩陣的測試擺放
    global timesleep
    new_point[2] = new_point[2]-5
    PTP_Move_org(new_point)
    print("  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩  ⇩ ", new_point, "\n")
    # 轉到出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口出口
    print("轉動轉盤放置拼鬥")
    plt.pause(timesleep)
    new_point[2] = new_point[2]+5
    PTP_Move_org(new_point)
    print("  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧  ⇧ ", new_point)
# testttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt


def fillbutton(event):  # 傾斜功能
    s.write('O'.encode())  # outoutoutoutoutoutoutoutoutout
    time.sleep(2)
    PTP_Move_org(base_point[1], speed=60, acceleration=70)
    PTP_Move_org(base_point[1], speed=60, acceleration=70)
    print("側邊傾斜", base_point[1])


def fillbacknormalbutton(event):  # 回正功能
    PTP_Move_org(base_point[2], speed=100, acceleration=100)
    print("回正", base_point[2])


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def movetofirstplace(event):  # 點位計算中移動至第一點位做檢查
    global firstplace_X
    global firstplace_Y
    global firstplace_Z
    global firstplace_A
    global firstplace_B
    global firstplace_C
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)
    first_place = [firstplace_X, firstplace_Y, firstplace_Z,
                   firstplace_A, firstplace_B, firstplace_C]
    print("移動至第一點位", first_place)
    PTP_Move_org(first_place)


def moverightdown_button(event):  # 點位計算中移動至第一點位的對角點位做檢查
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)
        first_place[0] = firstplace_X
        first_place[1] = firstplace_Y
        first_place[2] = firstplace_Z
        first_place[3] = firstplace_A
        first_place[4] = firstplace_B
        first_place[5] = firstplace_C
    a = first_place
    a[2] = a[2]+5
    PTP_Move_org(a)
    a[2] = a[2]-5
    a[0] = a[0]+140
    a[1] = a[1]-140
    PTP_Move_org(a)
    print("move diagonal", a)


def minor3_button(event):  # 點位計算中移動至第一點位b軸-3做檢查
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)
    first_place = [firstplace_X, firstplace_Y, firstplace_Z,
                   firstplace_A, firstplace_B, firstplace_C]
    first_place[2] = first_place[2]+8
    first_place[1] = first_place[1]-9
    PTP_Move_org(first_place)
    first_place[4] = first_place[4]-3
    PTP_Move_org(first_place)
    print(first_place)


def moverightdown_zero_button(event):  # 點位計算中移動至第一點位的b軸-3的對角點位做檢查
    with open('/home/showmay/Desktop/simulatoer_test/XYZ_zero_result.txt', 'r') as x:
        line = x.readlines()
        firstplace_X = line[0]
        firstplace_Y = line[1]
        firstplace_Z = line[2]
        firstplace_A = line[3]
        firstplace_B = line[4]
        firstplace_C = line[5]
        firstplace_X = float(firstplace_X)
        firstplace_Y = float(firstplace_Y)
        firstplace_Z = float(firstplace_Z)
        firstplace_A = float(firstplace_A)
        firstplace_B = float(firstplace_B)
        firstplace_C = float(firstplace_C)
        first_place[0] = firstplace_X
        first_place[1] = firstplace_Y
        first_place[2] = firstplace_Z
        first_place[3] = firstplace_A
        first_place[4] = firstplace_B
        first_place[5] = firstplace_C
    a = first_place
    a[2] = a[2]+5
    PTP_Move_org(a)
    a[2] = a[2]-5
    a[0] = a[0]+140
    a[1] = a[1]-140
    PTP_Move_org(a)
    print("move diagonal", a)


def shutdownbutton(event):  # 關閉程式
    os._exit(0)


def plateout(event):
    s.write('O'.encode())
    print("馬達回歸出口")


def platein(event):
    s.write('I'.encode())
    print("馬達回歸入口")


def testplatebutton(event):
    print("測試轉盤轉動")
    s.write('I'.encode())
    time.sleep(1)
    s.write('O'.encode())
    time.sleep(1.5)


def secondenterbutton(event):
    print("第二入口")
    s.write('i'.encode())


def fillbacknormalbutton_close(event):
    PTP_Move_org(base_point[2], speed=50, acceleration=50)
    print("回正", base_point[2])
    time.sleep(1)
    s.write('I'.encode())  # 轉到入口轉到入口轉到入口轉到入口轉到入口轉到入口轉到入口
    os._exit(0)


def draw_fiveplate(new_point):  # 擺放拚豆時畫出拚豆寶寶ㄉ功能，檢查程式有沒有露點位擺放之類ㄉ
    if (myArray[i][j] == 1):
        plt.plot(j, i, color='tomato', marker='o')
    if (myArray[i][j] == 2):
        plt.plot(j, i, color='springgreen', marker='o')
    if (myArray[i][j] == 3):
        plt.plot(j, i, 'yo')
    if (myArray[i][j] == 4):
        plt.plot(j, i, 'ko')
    if (myArray[i][j] == 5):
        plt.plot(j, i, 'wo')
    if (myArray[i][j+2] == 1):
        plt.plot(j+2, i, color='tomato', marker='o')
    if (myArray[i][j+2] == 2):
        plt.plot(j+2, i, color='springgreen', marker='o')
    if (myArray[i][j+2] == 3):
        plt.plot(j+2, i, 'yo')
    if (myArray[i][j+2] == 4):
        plt.plot(j+2, i, 'ko')
    if (myArray[i][j+2] == 5):
        plt.plot(j+2, i, 'wo')
    if (myArray[i][j+4] == 1):
        plt.plot(j+4, i, color='tomato', marker='o')
    if (myArray[i][j+4] == 2):
        plt.plot(j+4, i, color='springgreen', marker='o')
    if (myArray[i][j+4] == 3):
        plt.plot(j+4, i, 'yo')
    if (myArray[i][j+4] == 4):
        plt.plot(j+4, i, 'ko')
    if (myArray[i][j+4] == 5):
        plt.plot(j+4, i, 'wo')
    if (myArray[i][j+6] == 1):
        plt.plot(j+6, i, color='tomato', marker='o')
    if (myArray[i][j+6] == 2):
        plt.plot(j+6, i, color='springgreen', marker='o')
    if (myArray[i][j+6] == 3):
        plt.plot(j+6, i, 'yo')
    if (myArray[i][j+6] == 4):
        plt.plot(j+6, i, 'ko')
    if (myArray[i][j+6] == 5):
        plt.plot(j+6, i, 'wo')
    if (myArray[i][j+8] == 1):
        plt.plot(j+8, i, color='tomato', marker='o')
    if (myArray[i][j+8] == 2):
        plt.plot(j+8, i, color='springgreen', marker='o')
    if (myArray[i][j+8] == 3):
        plt.plot(j+8, i, 'yo')
    if (myArray[i][j+8] == 4):
        plt.plot(j+8, i, 'ko')
    if (myArray[i][j+8] == 5):
        plt.plot(j+8, i, 'wo')


def count_fiveplatebutton(event):  # 偷吃步的部分檢查拚豆總數及填充個數，UI主程式中五轉盤填充的功能
    m = 1
    for i in range(0, 28):
        for j in range(0, 29):
            if (myArray[i][j] != 0):
                if ((j % 2 == 0) and (i % 2 == 0)):
                    print("第1入口第", m, "顆填充",
                          myArray[[i], [j, j+2, j+4, j+6, j+8]])
                    myArray[[i], [j, j+2, j+4, j+6, j+8]] = 0
                    m += 1
                    if m > 10:
                        if (m % 10) == 1:
                            print("\n")
                if ((j % 2 == 1) and (i % 2 == 1)):
                    print("第1入口第", m, "顆填充",
                          myArray[[i], [j, j+2, j+4, j+6, j+8]])
                    myArray[[i], [j, j+2, j+4, j+6, j+8]] = 0
                    m += 1
                    if m > 10:
                        if (m % 10) == 1:
                            print("\n")
    for i in range(29, 0, -1):
        for j in range(0, 29):
            if (myArray[i][j] != 0):
                print("第1入口第", m, "顆填充", myArray[[i], [j, j+2, j+4, j+6, j+8]])
                myArray[[i], [j, j+2, j+4, j+6, j+8]] = 0
                m += 1
                if (m % 10) == 1:
                    print("\n")

    sys.exit()


def extra_window(event):
    extra_window = tk.Toplevel()
    extra_window.geometry('1160x600')  # 1200*300
    extra_window.configure(background='grey')
    extra_window.title('正式—正式—正式—正式—正式—正式—正式')
    callout = tk.Button(extra_window, bg='#4D8D1A', text='主程式五拚豆',
                        height=10, width=15, font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=0, y=0)  # 按鈕位置（整個方框）
    callout.bind("<Button>", main_fiveplatebutton)
    callout = tk.Button(extra_window, bg='#FA34A9', text='回正關閉', height=10, width=15, font=(
        'italic', 16, 'bold'), command=extra_window.destroy)  # 按鈕長寬
    callout.place(x=900, y=0)  # 按鈕位置（整個方框）
    callout.bind("<Button>", fillbacknormalbutton_close)
    callout = tk.Button(extra_window, bg='white', text='關閉小UI', height=10, width=15, font=(
        'italic', 16, 'bold'), command=extra_window.destroy)  # 按鈕長寬
    callout.place(x=600, y=0)  # 按鈕位置（整個方框）
    callout = tk.Button(extra_window, bg='#1E73B7', text='五轉盤填充',
                        height=10, width=15, font=('italic', 16, 'bold'))
    callout.place(x=300, y=300)
    callout.bind("<Button>", count_fiveplatebutton)
    callout = tk.Button(extra_window, bg='#5C737C', text='第二入口',
                        height=10, width=15, font=('italic', 16, 'bold'))
    callout.place(x=0, y=300)
    callout.bind("<Button>", secondenterbutton)
    callout = tk.Button(extra_window, bg='#8DD6A9', text='測試矩陣',
                        height=10, width=15, font=('italic', 16, 'bold'))
    callout.place(x=300, y=0)
    callout.bind("<Button>", test_fiveplatebutton)


def testarray_button(event):
    extraaa_window = tk.Toplevel()
    extraaa_window.geometry('200x860+1630+70')
    extraaa_window.configure(background='grey')
    extraaa_window.title('test-test-test-test-test-test')
    callout = tk.Button(extraaa_window, bg='#16AF6E',
                        text='移動至第一點位', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=0, y=0, relwidth=1, relheight=0.17)  # 按鈕位置（整個方框）
    callout.bind("<Button>", movetofirstplace)
    callout = tk.Button(extraaa_window, bg='#FA34A9',
                        text='B==0\n移動至右下角', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=0, y=160, relwidth=1, relheight=0.17)  # 按鈕位置（整個方框）
    callout.bind("<Button>", moverightdown_zero_button)

    callout = tk.Button(extraaa_window, bg='#16AF6E',
                        text='第一點位\n抬升\nB軸-3', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=0, y=390, relwidth=1, relheight=0.17)  # 按鈕位置（整個方框）
    callout.bind("<Button>", minor3_button)
    callout = tk.Button(extraaa_window, bg='red',
                        text='B==-3\n移動至右下角', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=0, y=550, relwidth=1, relheight=0.17)  # 按鈕位置（整個方框）
    callout.bind("<Button>", moverightdown_button)

    callout = tk.Button(extraaa_window, bg='white', text='關閉小UI', font=(
        'italic', 16, 'bold'), command=extraaa_window.destroy)
    callout.place(x=0, y=710, relwidth=1, relheight=0.17)


def testplate_button(event):
    extraaa_window = tk.Toplevel()
    extraaa_window.geometry('1000x200')
    extraaa_window.configure(background='grey')
    extraaa_window.title('test-test-test-test-test-test')
    callout = tk.Button(extraaa_window, bg='#40C9E9',
                        text='第一入口', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=0, y=0, relwidth=0.2, relheight=1)  # 按鈕位置（整個方框）
    callout.bind("<Button>", platein)
    callout = tk.Button(extraaa_window, bg='#40C9E9',
                        text='第二入口', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=200, y=0, relwidth=0.2, relheight=1)  # 按鈕位置（整個方框）
    callout.bind("<Button>", secondenterbutton)
    callout = tk.Button(extraaa_window, bg='#FA34A9',
                        text='出口', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=400, y=0, relwidth=0.2, relheight=1)  # 按鈕位置（整個方框）
    callout.bind("<Button>", plateout)
    callout = tk.Button(extraaa_window, bg='#16AF6E',
                        text='出口入口', font=('italic', 16, 'bold'))  # 按鈕長寬
    callout.place(x=600, y=0, relwidth=0.2, relheight=1)  # 按鈕位置（整個方框）
    callout.bind("<Button>", testplatebutton)

    callout = tk.Button(extraaa_window, bg='white', text='關閉小UI', font=(
        'italic', 16, 'bold'), command=extraaa_window.destroy)
    callout.place(x=800, y=0, relwidth=0.2, relheight=1)


if __name__ == "__main__":

    a = plt.axes([.18, .1, .65, .8],
                 facecolor='k')  # pyplot api 命令-黑色背景
    ax1 = plt.gca()
    ax1.patch.set_facecolor("grey")    # 设置 ax1 区域背景颜色
    ax1.patch.set_alpha(1)    # 设置 ax1 区域背景颜色透明度
    plt.title('bead')
    plt.xlim(-1, 29)
    plt.ylim(29, -1)
    for y in range(0, 29):
        for x in range(0, 29):
            plt.plot(x, y, marker='o', color='black', markerfacecolor='grey')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    window_small = tk.Tk()
    window_small_zero = tk.Tk()
    window = tk.Tk()

    window_small.title('B軸-3～B軸-3')
    window_small.geometry('600x390+1020+500')
    window_small.configure(background='black')
    varx = tk.DoubleVar()
    vary = tk.DoubleVar()
    mylabelx = tk.Label(window_small, text='xxxxx',
                        background='white', height=2, width=5)
    mylabelx.place(x=0, y=5)
    varx = tk.Entry(window_small, background='red', highlightthickness=5,
                    highlightbackground='black', highlightcolor='#40C9E9')
    varx.place(x=50, y=0, relwidth=0.5, relheight=0.125)
    mylabely = tk.Label(window_small, text='yyyyy',
                        background='white', height=2, width=5)
    mylabely.place(x=0, y=55)
    vary = tk.Entry(window_small, background='red', highlightthickness=5,
                    highlightbackground='black', highlightcolor='#40C9E9')
    vary.place(x=50, y=50, relwidth=0.5, relheight=0.125)

    mylabelx = tk.Label(window_small, text='點位X',
                        background='white', height=2, width=5)
    mylabelx.place(x=00, y=104)
    var_firstx = tk.Entry(window_small, background='red', highlightthickness=5,
                          highlightbackground='black', highlightcolor='#40C9E9')
    var_firstx.place(x=50, y=100, relwidth=0.5, relheight=0.125)

    mylabely = tk.Label(window_small, text='點位Y',
                        background='white', height=2, width=5)
    mylabely.place(x=00, y=154)
    var_firsty = tk.Entry(window_small, background='red', highlightthickness=5,
                          highlightbackground='black', highlightcolor='#40C9E9')
    var_firsty.place(x=50, y=150, relwidth=0.5, relheight=0.125)

    mylabelz = tk.Label(window_small, text='點位Z',
                        background='white', height=2, width=5)
    mylabelz.place(x=00, y=205)
    var_firstz = tk.Entry(window_small, background='red', highlightthickness=5,
                          highlightbackground='black', highlightcolor='#40C9E9')
    var_firstz.place(x=50, y=200, relwidth=0.5, relheight=0.125)

    mylabelA = tk.Label(window_small, text='點位A',
                        background='white', height=2, width=5)
    mylabelA.place(x=00, y=255)
    var_firstA = tk.Entry(window_small, background='red', highlightthickness=5,
                          highlightbackground='black', highlightcolor='#40C9E9')
    var_firstA.insert(0, firstA_insert)  # A第一點位
    var_firstA.place(x=50, y=248, relwidth=0.5, relheight=0.125)

    mylabelB = tk.Label(window_small, text='點位B',
                        background='white', height=2, width=5)
    mylabelB.place(x=00, y=300)
    var_firstB = tk.Entry(window_small, background='red', highlightthickness=5,
                          highlightbackground='black', highlightcolor='#40C9E9')
    var_firstB.insert(0, firstB_insert)  # B第一點位
    var_firstB.place(x=50, y=294, relwidth=0.5, relheight=0.125)

    mylabelC = tk.Label(window_small, text='點位C',
                        background='white', height=2, width=5)
    mylabelC.place(x=00, y=345)
    var_firstC = tk.Entry(window_small, background='red', highlightthickness=5,
                          highlightbackground='black', highlightcolor='#40C9E9')
    var_firstC.insert(0, firstC_insert)  # C第一點位
    var_firstC.place(x=50, y=340, relwidth=0.5, relheight=0.125)

    mybutton = tk.Button(window_small, text='儲存！', command=entryxy)
    mybutton.place(x=360, y=0, relwidth=0.4, relheight=0.23)
    mybutton = tk.Button(window_small, text='存第一點位！', command=entryfirstplace)
    mybutton.place(x=360, y=100, relwidth=0.4, relheight=0.73)

    window_small_zero.title('B軸為0～B軸為0')
    window_small_zero.geometry('600x390+1020+70')
    window_small_zero.configure(background='black')
    varx_zero = tk.DoubleVar()
    vary_zero = tk.DoubleVar()
    mylabelx_zero = tk.Label(
        window_small_zero, text='xxxxx', background='white', height=2, width=5)
    mylabelx_zero.place(x=0, y=5)
    varx_zero = tk.Entry(window_small_zero, background='#FA34A9',
                         highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    varx_zero.place(x=50, y=0, relwidth=0.5, relheight=0.125)
    mylabely_zero = tk.Label(
        window_small_zero, text='yyyyy', background='white', height=2, width=5)
    mylabely_zero.place(x=0, y=55)
    vary_zero = tk.Entry(window_small_zero, background='#FA34A9',
                         highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    vary_zero.place(x=50, y=50, relwidth=0.5, relheight=0.125)

    mylabelx_zero = tk.Label(
        window_small_zero, text='點位X', background='white', height=2, width=5)
    mylabelx_zero.place(x=00, y=104)
    var_firstx_zero = tk.Entry(window_small_zero, background='#FA34A9',
                               highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    var_firstx_zero.place(x=50, y=100, relwidth=0.5, relheight=0.125)

    mylabely_zero = tk.Label(
        window_small_zero, text='點位Y', background='white', height=2, width=5)
    mylabely_zero.place(x=00, y=154)
    var_firsty_zero = tk.Entry(window_small_zero, background='#FA34A9',
                               highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    var_firsty_zero.place(x=50, y=150, relwidth=0.5, relheight=0.125)

    mylabelz_zero = tk.Label(
        window_small_zero, text='點位Z', background='white', height=2, width=5)
    mylabelz_zero.place(x=00, y=205)
    var_firstz_zero = tk.Entry(window_small_zero, background='#FA34A9',
                               highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    var_firstz_zero.place(x=50, y=200, relwidth=0.5, relheight=0.125)

    mylabelA_zero = tk.Label(
        window_small_zero, text='點位A', background='white', height=2, width=5)
    mylabelA_zero.place(x=00, y=255)
    var_firstA_zero = tk.Entry(window_small_zero, background='#FA34A9',
                               highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    var_firstA_zero.insert(0, firstA_insert)  # A第一點位
    var_firstA_zero.place(x=50, y=248, relwidth=0.5, relheight=0.125)

    mylabelB_zero = tk.Label(
        window_small_zero, text='點位B', background='white', height=2, width=5)
    mylabelB_zero.place(x=00, y=300)
    var_firstB_zero = tk.Entry(window_small_zero, background='#FA34A9',
                               highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    var_firstB_zero.insert(0, 0)  # B第一點位
    var_firstB_zero.place(x=50, y=294, relwidth=0.5, relheight=0.125)

    mylabelC_zero = tk.Label(
        window_small_zero, text='點位C', background='white', height=2, width=5)
    mylabelC_zero.place(x=00, y=345)
    var_firstC_zero = tk.Entry(window_small_zero, background='#FA34A9',
                               highlightthickness=5, highlightbackground='black', highlightcolor='#40C9E9')
    var_firstC_zero.insert(0, firstC_insert)  # C第一點位
    var_firstC_zero.place(x=50, y=340, relwidth=0.5, relheight=0.125)

    mybutton = tk.Button(window_small_zero, text='儲存！',
                         background='#F8F4E5', command=entryxy_zero)
    mybutton.place(x=360, y=0, relwidth=0.4, relheight=0.23)
    mybutton = tk.Button(window_small_zero, text='存第一點位！',
                         background='#F8F4E5', command=entryfirstplace_zero)
    mybutton.place(x=360, y=100, relwidth=0.4, relheight=0.73)

    window.title('準備時間＊準備時間＊準備時間＊準備時間＊準備時間＊準備時間＊準備時間＊準備時間＊準備時間＊準備時間')
    window.geometry('885x760')
    window.configure(background='grey')

    myArray = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4,
            4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5,
            5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5,
            5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5,
            5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 4, 4, 4, 4,
            5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 0, 0, 0,
            4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 4, 4, 4, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 4, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 5, 5, 5, 4, 4, 4, 4,
            4, 4, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 5, 4, 5, 4, 2, 4, 2,
            2, 2, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 5, 5, 4, 4, 2, 2, 4,
            4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 5, 4, 5, 4, 2, 2, 4,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 4, 5, 5, 5, 4, 2, 2, 4,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 4, 5, 4, 5, 4, 2, 2, 4,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 5, 5, 4, 4, 2, 2, 4,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 4, 4, 4, 4, 2, 2, 4, 5, 4, 5, 4, 2, 2, 4,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 5, 5, 5, 4, 2, 2, 4,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 2, 2, 2, 2, 4, 1, 1, 4, 4, 4, 2, 2, 4, 4,
            4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 4, 1, 1, 4, 2, 2, 2, 4, 2, 2,
            2, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 4, 4, 1, 1, 1, 4, 2, 2, 4, 4, 4, 4,
            4, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 4, 2, 4, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 4, 2, 4, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 1, 1, 4, 2, 4, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 4, 4, 2, 4, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    myArray_test = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 29
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    callout = tk.Button(window, bg='#8DD6A9', text='點位計算',
                        font=('italic', 60, 'bold'))
    callout.place(x=00, y=80, relheight=0.415, relwidth=0.5)
    callout.bind("<Button>", testarray_button)

    callout = tk.Button(window, bg='#40C9E9', text='傾斜裝填',
                        font=('italic', 16, 'bold'))
    callout.place(x=450, y=0, relheight=0.1, relwidth=0.5)
    callout.bind("<Button>", fillbutton)

    callout = tk.Button(window, bg='#4D8D1A', text='主程式',
                        font=('italic', 60, 'bold'))  # 按鈕長寬
    callout.place(x=450, y=80, relheight=0.415, relwidth=0.5)
    callout.bind("<Button>", extra_window)

    callout = tk.Button(window, bg='#5C737C', text='轉盤',
                        font=('italic', 16, 'bold'))
    callout.place(x=0, y=0, relheight=0.1, relwidth=0.5)
    callout.bind("<Button>", testplate_button)

    callout = tk.Button(window, bg='#FC1008', text='關閉程式',
                        font=('italic', 60, 'bold'))  # 按鈕長寬
    callout.place(x=0, y=400, relheight=0.47, relwidth=0.5)
    callout.bind("<Button>", shutdownbutton)

    callout = tk.Button(window, bg='#FA34A9', text='回正',
                        font=('italic', 60, 'bold'))
    callout.place(x=450, y=400, relheight=0.47, relwidth=0.5)
    callout.bind("<Button>", fillbacknormalbutton)
    window.mainloop()
