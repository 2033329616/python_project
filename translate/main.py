# -*- coding: utf-8 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from PyQt5.QtGui import QImage
import sys
import ui.ui_translate as ui
import translate.translate as tl
import HandleJs

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self._ui = ui.Ui_MainWindow()
        self._ui.setupUi(self)
        self._translate_num = 0  # 0表示使用谷歌，1表示百度
        # 初始化翻译类
        self._transl = tl.translate()

    # 定义槽函数
    def translate(self):
        # self._ui.textEdit.setText('hello world！')
        # self._ui.textEdit.
        content = self._ui.textEdit.toPlainText().replace('\n', ' ')     # 获取文本的内容并#去除多余的回车
        self._ui.textEdit.setText(content) 
        # print(self._translate_num)
        if content != '':
            # print(content)
            # print(self._translate_num)
            if self._translate_num == 0:
                result = self._transl.google_translate(content)      # 使用谷歌翻译
            else:
                result = self._transl.baidu_translate(content)       # 使用百度翻译
            # print(result)
            self._ui.textBrowser.setText(result)          # 输出文本的内容
        else:
            self._ui.textBrowser.clear()



    #定义槽显示不同的图片
    def display(self):
        """"没有开发好,图像显示部分不全！！！！！！！！！！！！！！！"""
        index = self._ui.comboBox.currentIndex()           #获取当前的选项的次序号
        self._translate_num= index
        content = self._ui.comboBox.itemText(index)        #读取下拉列表的内容
        # print(content)
        # self._ui.graphicsView.setBackgroundBrush(QImage('.//0.jpg'))
        # self._ui.graphicsView = QImage('D:\\project\\translate\\0.jpg')
        # self._ui.graphicsView.show()
        # self.setWindowTitle('Icon')
        # self.setWindowIcon(QIcon('0.ico'))

    def clear_text(self):
        """"清除文本框中的内容"""
        content = self._ui.textEdit.clear()
        self._ui.textBrowser.clear()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭', '确认退出吗？', QMessageBox.StandardButtons(
            QMessageBox.Yes | QMessageBox.No))
        if reply:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())
