import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import Caesar

def convert(ui):
    input = ui.textEdit.toPlainText()
    num = int(ui.lineEdit_2.text())
    s1 = ''
    for i in range(len(input)):
        b = ord(input[i]) + num
        while (b > 122):
            b -= 26
        s1 += chr(b)
    ui.textEdit_2.setText(str(s1))

def donvert(ui):
    input = ui.textEdit_2.toPlainText()
    num = int(ui.lineEdit_2.text())
    s1 = ''
    for i in range(len(input)):
        b = ord(input[i]) - num
        while (b < 97):
            b += 26
        s1 += chr(b)
    ui.textEdit.setText(str(s1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Caesar.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(convert,ui))
    ui.pushButton_2.clicked.connect(partial(donvert, ui))
    sys.exit(app.exec_())

