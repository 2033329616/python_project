# encoding:utf-8

from ctypes import *
import pyHook
import pythoncom
import sys
import time
import win32gui, win32ui, win32con, win32api
from PIL import Image

"""捕捉鼠标获得坐标然后截图"""
class ScreenShot(object):
    def __init__(self):
        """初始化类"""
        self._old_state = ''   #保存鼠标前后的两个状态
        self._new_state = ''
        self._old_x = 0        #截图的坐标
        self._old_y = 0
        self._new_x = 0
        self._new_y = 0

        # 安装钩子，监听键盘消息
        self._hm = pyHook.HookManager()
        self._hm.MouseAll = self.__onMouseEvent
        self._hm.HookMouse()
        pythoncom.PumpMessages()

    def __onMouseEvent(self, event):
        # 鼠标事件处理,私有方法声明两个下滑线
        # print('='*30)
        # event.WindowName有时候会不好用
        # 所以调用底层API喊来获取窗口标题
        windowTitle = create_string_buffer(512)
        windll.user32.GetWindowTextA(event.Window, byref(windowTitle), 512)
        windowName = windowTitle.value.decode('gbk')
        
        self._old_state = self._new_state
        self._new_state = str(event.MessageName) 
        if self._new_state == "mouse left down":       #鼠标左键按下获取坐标(x0,y0)
            self._old_x, self._old_y = event.Position
        if self._new_state == "mouse left up":         #鼠标左键升起获取坐标(x1,y1)
            self._new_x, self._new_y = event.Position

        # print('当前您正处于"{0}"窗口'.format(windowName))
        # print('刚刚按下了"{0}"键'.format(str(event.MessageName)))
        
        if (self._new_state == 'mouse left up') and (self._old_state == 'mouse move'):  #截图动作出现
            # print(old_state)
            self._hm.UnhookMouse()   #解除鼠标监视
            self._hm = None
            # sys.exit()
            # pythoncom.EnableQuitMessage(0)
            win32api.PostQuitMessage()  # 使pythoncom.PumpMessages()结束
        return True

    def get_position(self):
        """返回鼠标获取的区域坐标，以[x,y,w,h]列表的形式"""
        if self._new_x > self._old_x:       #从左上角向右下方划分区域
            return [self._old_x, self._old_y, self._new_x-self._old_x, self._new_y-self._old_y]
        elif self._new_x < self._old_x:     #从右下角向左上方划分区域
            return [self._new_x, self._new_y, self._old_x-self._new_x, self._old_y-self._new_y]

    def window_capture(self, filename, args):
        """filename:文件名，args是[x,y,w,h]列表"""
        hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        # w = MoniterDev[0][2][2]
        # h = MoniterDev[0][2][3] 
        x = args[0]   #截图区域左上角的x,y坐标
        y = args[1]
        w = args[2]   #截图区域的宽和高
        h = args[3]
        # print w,h　　　#图片大小

        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (x,y), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, filename)

if __name__ == '__main__':
    
    screen = ScreenShot()
    position = screen.get_position()
    print(position)

    begin = time.time()
    screen.window_capture("temp.jpg", position)
    end = time.time()
    print(end - begin)
    img = Image.open('temp.jpg')
    img.show()