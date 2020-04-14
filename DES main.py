# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import DES
from DESstruct import *

def code(from_code, key, code_len, key_len):
    output = ""
    trun_len = 0

    # 将密文和密钥转换为二进制
    code_string = functionCharToA(from_code, code_len)
    code_key = functionCharToA(key, key_len)

    # 如果密钥长度不是16的整数倍则以增加0的方式变为16的整数倍
    if code_len % 16 != 0:
        real_len = (code_len // 16) * 16 + 16
    else:
        real_len = code_len

    if key_len % 16 != 0:
        key_len = (key_len // 16) * 16 + 16
    key_len *= 4

    # 每个16进制占4位
    trun_len = 4 * real_len
    # 对每64位进行一次加密
    for i in range(0, trun_len, 64):
        run_code = code_string[i:i + 64]
        l = i % key_len
        run_key = code_key[l:l + 64]

        # 64位明文、密钥初始置换
        run_code = codefirstchange(run_code)
        run_key = keyfirstchange(run_key)

        # 16次迭代
        for j in range(16):
            # 取出明文左右32位
            code_r = run_code[32:64]
            code_l = run_code[0:32]

            # 64左右交换
            run_code = code_r

            # 右边32位扩展置换
            code_r = functionE(code_r)

            # 获取本轮子密钥
            key_l = run_key[0:28]
            key_r = run_key[28:56]
            key_l = key_l[LS_Table[j]:28] + key_l[0:LS_Table[j]]
            key_r = key_r[LS_Table[j]:28] + key_r[0:LS_Table[j]]
            run_key = key_l + key_r
            key_y = functionKeySecondChange(run_key)

            # 异或
            code_r = codeXor(code_r, key_y)

            # S盒代替/选择
            code_r = functionS(code_r)

            # P转换
            code_r = functionP(code_r)

            # 异或
            code_r = codeXor(code_l, code_r)
            run_code += code_r
        # 32互换
        code_r = run_code[32:64]
        code_l = run_code[0:32]
        run_code = code_r + code_l

        # 将二进制转换为16进制、逆初始置换
        output += functionCodeChange(run_code)
    return output

def decode(string, key, key_len, string_len):
    output = ""
    trun_len = 0
    num = 0

    # 将密文转换为二进制
    code_string = functionCharToA(string, string_len)
    # 获取字密钥
    code_key = getkey(key, key_len)

    # 如果密钥长度不是16的整数倍则以增加0的方式变为16的整数倍
    real_len = (key_len // 16) + 1 if key_len % 16 != 0 else key_len // 16
    trun_len = string_len * 4
    # 对每64位进行一次加密
    for i in range(0, trun_len, 64):
        run_code = code_string[i:i + 64]
        run_key = code_key[num % real_len]

        # 64位明文初始置换
        run_code = codefirstchange(run_code)

        # 16次迭代
        for j in range(16):
            code_r = run_code[32:64]
            code_l = run_code[0:32]

            # 64左右交换
            run_code = code_r

            # 右边32位扩展置换
            code_r = functionE(code_r)

            # 获取本轮子密钥
            key_y = run_key[15 - j]

            # 异或
            code_r = codeXor(code_r, key_y)

            # S盒代替/选择
            code_r = functionS(code_r)

            # P转换
            code_r = functionP(code_r)

            # 异或
            code_r = codeXor(code_l, code_r)

            run_code += code_r
        num += 1

        # 32互换
        code_r = run_code[32:64]
        code_l = run_code[0:32]
        run_code = code_r + code_l

        # 将二进制转换为16进制、逆初始置换
        output += functionCodeChange(run_code)
    return output

    # 获取子密钥
def getkey(key, key_len):

        # 将密钥转换为二进制
        code_key = functionCharToA(key, key_len)

        a = [''] * 16
        real_len = (key_len // 16) * 16 + 16 if key_len % 16 != 0 else key_len

        b = [''] * (real_len // 16)
        for i in range(real_len // 16):
            b[i] = a[:]
        num = 0
        trun_len = 4 * key_len
        for i in range(0, trun_len, 64):
            run_key = code_key[i:i + 64]
            run_key = keyfirstchange(run_key)
            for j in range(16):
                key_l = run_key[0:28]
                key_r = run_key[28:56]
                key_l = key_l[LS_Table[j]:28] + key_l[0:LS_Table[j]]
                key_r = key_r[LS_Table[j]:28] + key_r[0:LS_Table[j]]
                run_key = key_l + key_r
                key_y = functionKeySecondChange(run_key)
                b[num][j] = key_y[:]
            num += 1

        return b
    # 异或
def codeXor(code, key):
    code_len = len(key)
    return_list = ''
    for i in range(code_len):
        if code[i] == key[i]:
            return_list += '0'
        else:
            return_list += '1'
    return return_list

    # 密文或明文初始置换
def codefirstchange(code):
    changed_code = ''
    for i in range(64):
        changed_code += code[IP_Table[i] - 1]
    return changed_code

    # 密钥初始置换
def keyfirstchange(key):
    changed_key = ''
    for i in range(56):
        changed_key += key[PC1_Table[i] - 1]
    return changed_key

    # 逆初始置换
def functionCodeChange(code):
    lens = len(code) // 4
    return_list = ''
    for i in range(lens):
        list = ''
        for j in range(4):
            list += code[IPInv_Table[i * 4 + j] - 1]
        return_list += "%x" % int(list, 2)
    return return_list

    # 扩展置换
def functionE(code):
    return_list = ''
    for i in range(48):
        return_list += code[E_Table[i] - 1]
    return return_list

    # 置换P
def functionP(code):
    return_list = ''
    for i in range(32):
        return_list += code[P_Table[i] - 1]
    return return_list

    # S盒代替选择置换
def functionS(key):
    return_list = ''
    for i in range(8):
        row = int(str(key[i * 6]) + str(key[i * 6 + 5]), 2)
        raw = int(str(key[i * 6 + 1]) + str(key[i * 6 + 2]) + str(key[i * 6 + 3]) + str(key[i * 6 + 4]), 2)
        return_list += functionTos(S_Box[i][row][raw], 4)
    return return_list

    # 密钥置换选择2
def functionKeySecondChange(key):
    return_list = ''
    for i in range(48):
        return_list += key[PC2_Table[i] - 1]
    return return_list

    # 将十六进制转换为二进制字符串
def functionCharToA(code, lens):
    return_code = ''
    lens = lens % 16
    for key in code:
        code_ord = int(key, 16)
        return_code += functionTos(code_ord, 4)
    if lens != 0:
        return_code += '0' * (16 - lens) * 4
    return return_code

    # 二进制转换
def functionTos(o, lens):
    return_code = ''
    for i in range(lens):
        return_code = str(o >> i & 1) + return_code
    return return_code


# 将unicode字符转换为16进制
def tohex(string):
    return_string = ''
    for i in string:
        return_string += "%02x" % ord(i)
    return return_string


def tounicode(string):
    return_string = ''
    string_len = len(string)
    for i in range(0, string_len, 2):
        return_string += chr(int(string[i:i + 2], 16))
    return return_string


# 入口函数
def desencode(from_code, key):
    # 转换为16进制
    from_code = tohex(from_code)
    key = tohex(key)

    key_len = len(key)
    string_len = len(from_code)

    if string_len < 1 or key_len < 1:
        print('error input')
        return False
    key_code = code(from_code, key, string_len, key_len)
    return key_code


def desdecode(key_code, key):
    key = tohex(key)

    key_len = len(key)
    string_len = len(key_code)
    if string_len % 16 != 0:
        return False
    if string_len < 1 or key_len < 1:
        return False

    from_code = decode(key_code, key, key_len, string_len)
    return tounicode(from_code)


def convert(ui):
    from_code = ui.textEdit.toPlainText()
    key = ui.textEdit_2.toPlainText()
    keycode = desencode(from_code, key)
    ui.textEdit_3.setText(keycode)

def donvert(ui):
    key_code = ui.textEdit_3.toPlainText()
    key = ui.textEdit_2.toPlainText()
    from_code = desdecode(key_code, key)
    ui.textEdit_4.setText(from_code)

def clear(ui):
    ui.textEdit.clear()
    ui.textEdit_2.clear()
    ui.textEdit_3.clear()
    ui.textEdit_4.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = DES.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(convert,ui))
    ui.pushButton_2.clicked.connect(partial(donvert, ui))
    ui.pushButton_3.clicked.connect(partial(clear, ui))
    sys.exit(app.exec_())