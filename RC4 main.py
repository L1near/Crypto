# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import RC4
import binascii

def convert(ui):
    text = ui.textEdit.toPlainText()
    plaintext = ''
    kstr1 = ''
    global c1
    global size
    c1 = ''
    for i in text:
        p1 = (bin(ord(i)).replace('0b','').zfill(8))
        plaintext += p1
    size = len(plaintext)

    key1 = ui.textEdit_2.toPlainText()#5-16个字符
    key = ''
    for i in key1:
        k1 = (bin(ord(i)).replace('0b','').zfill(8))
        key += k1
    ksize = len(key)

    #初始化S盒
    s = [0] * 256
    for ii in range(256):
        s[ii] = ii
    #利用密钥打乱s盒
    j = 0
    for iii in range(256):
        j = (j+int(s[iii])+int(key[iii % ksize])) % 256
        temp = s[j]
        s[j] = s[iii]
        s[iii] = temp
    # 生成密钥流
    i = 0
    j = 0
    for k in range(size):
        i = (i+1)%256
        j = (j+s[i]) %256
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
        kstr.append(bin(s[(s[i]+s[j]) %256]).replace('0b',''))

    #加密
    for i in range(size):
        c.append(int(kstr[i]) ^ int(plaintext[i]))
    for i in range(len(kstr)):
        kstr1 += kstr[i]
    for i in c:
        i = str(i)
        c1 += chr(int(i, 2))
    ui.textEdit_3.setText(kstr1)
    ui.textEdit_4.setText(c1)

def donvert(ui):
    # input = ui.textEdit_4.toPlainText()
    # cryptotext = ''
    # m1 = ''
    # for i in input:
    #     p2 = (bin(ord(i)).replace('0b', '').zfill(8))
    #     cryptotext += p2
    # size = len(c1)
    global m
    m = []
    m1 = ''
    key2 = ui.textEdit_2.toPlainText()  # 5-16个字符
    key = ''
    for i in key2:
        k2 = (bin(ord(i)).replace('0b', '').zfill(8))
        key += k2
    ksize = len(key)
    #初始化S盒
    s = [0] * 256
    for ii in range(256):
        s[ii] = ii
    #利用密钥打乱s盒
    j = 0
    for iii in range(256):
        j = (j+int(s[iii])+int(key[iii % ksize])) % 256
        temp = s[j]
        s[j] = s[iii]
        s[iii] = temp
    # 生成密钥流
    i = 0
    j = 0
    for k in range(size):
        i = (i+1)%256
        j = (j+s[i]) %256
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
        kstr[k] = bin(s[(s[i]+s[j]) %256]).replace('0b','')
    for i in range(size):
        m.append(int(kstr[i]) ^ int(bin(ord(c1[i])).replace('0b','')))
    m = list(map(str,m))
    m = ''.join(m)
    for i in range(len(m) // 8):
        m1 += chr(int(m[8 * i:8 * (i + 1)], 2))
    ui.textEdit_5.setText(m1)

def clear(ui):
    ui.textEdit.clear()
    ui.textEdit_2.clear()
    ui.textEdit_3.clear()
    ui.textEdit_4.clear()
    ui.textEdit_5.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = RC4.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    kstr = []
    c = []
    ui.pushButton.clicked.connect(partial(convert,ui))
    ui.pushButton_2.clicked.connect(partial(donvert, ui))
    ui.pushButton_3.clicked.connect(partial(clear, ui))
    sys.exit(app.exec_())
