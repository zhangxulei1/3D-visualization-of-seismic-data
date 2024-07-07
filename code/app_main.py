from data_format_conversion import sgy2npy
from body_render import surface_rendering, contour3d_rendering
from slices import slice, slice_isosurfaces
from slices import slot_slice_xoryorz_slider
from iso_surface_render import surface_render, slot_iso_surface_slider
from signals import signal_object_slice, SignalObject, signal_sliceXYZ
from fault_go_render import fault_go_rendering, fault_data_format_conversion

import threading

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMessageBox, QMainWindow,
    QFileDialog
)

from display_menu import Ui_AppMainWindow
from PyQt6.QtCore import QObject, pyqtSignal
from PySide2.QtCore import Slot


import sys
import os
import numpy as np
from threading import Thread
import segyio
import string


# 全局变量 地震数据,x, y, z三个维度的值的大小
sesimic_data = []

# 定义信号类
class SliceXorYorZSliderSignalClass(QObject):
    signal = pyqtSignal(str, int)

# 等值面信号类 发出的信号
class ISOSurfaceSliderSignalClass(QObject):
    signal = pyqtSignal(int, float) # 等值面的值，透明度

# 定义发送信号函数
# 切片xyz的滑动条
def send_signal_slicexoryorz_slider(obj, xyz, slice_x_index):
    print("send_signal_slicexoryorz_slider发送信号开始")
    obj.signal.emit(xyz, slice_x_index)
    print("send_signal_slicexoryorz_slider发送信号成功")

# 定义发送信号函数
# 等值面滑动条改变之后进行发送的函数
def send_signal_isosurface_slider(obj, value, opacity):
    print("send_signal_isosurface_slider发送信号开始")
    obj.signal.emit(value, opacity)
    print("send_signal_isosurface_slider发送信号成功")


# 解析文件
def analyse_filename(fileName):
    filetype = fileName[-3:]
    result = []
    # segy文件
    if (filetype == "egy"):
        npyfile =  fileName[:-4] + "npy"
        try:
            seismic = segyio.tools.cube(fileName)
        except Exception as e:
            print("segy数据不是标准的segy数据")
            result = [-1, -1, -1, -1]
            return result
        result = [seismic, seismic.shape[0], seismic.shape[1], seismic.shape[2]]
        return result

    if (filetype == "sgy"):
        npyfile = fileName[:-3] + "npy"
        try:
            seismic = segyio.tools.cube(fileName)
        except Exception as e:
            print("sgy数据不是标准的sgy数据")
            result = [-1, -1, -1, -1]
            return result
        result = [seismic, seismic.shape[0], seismic.shape[1], seismic.shape[2]]
        return result

    if (filetype == "bin"):
        with open(fileName, "rb") as f:
            rectype = np.dtype(np.float32)
            bdata = np.fromfile(f, dtype=rectype)
        # bin文件无法指定维度的大小
        result = [bdata, 0, 0, 0]
        return result

    if (filetype == "npy"):
        npy_data = np.load(fileName)
        x, y, z = npy_data.shape[0], npy_data.shape[1], npy_data.shape[2]
        result = [npy_data, x, y, z]
        return result

# 定义一个线程类
class ThreadAnalyseFile(threading.Thread):
    def __init__(self, func, args=()):
        super(ThreadAnalyseFile, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(self.args[0])

    def get_result(self):
        return self.result

    # def stop(self):  # 线程停止还没弄


class MyDisplay3D(Ui_AppMainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # 打开文件
        self.file_open.triggered.connect(
            self.file_open_in
        )
        # 维度的改变
        self.x_lineEdit.editingFinished.connect(
            self.modify_x
        )
        self.y_lineEdit.editingFinished.connect(
            self.modify_y
        )
        self.z_lineEdit.editingFinished.connect(
            self.modify_z
        )
        # 体绘制
        self.body_display.triggered.connect(
            self.body_display_accomplish
        )
        # 体绘制的复选框
        self.bodyDisplay_checkBox.stateChanged.connect(
            self.body_display_accomplish
        )
        # 断层自动追踪的复选框
        self.fault_go_Display_checkBox.stateChanged.connect(
            self.fault_go_display_accomplish
        )
        # 切片
        self.sclie_display.triggered.connect(
            self.sclie_display_accomplish
        )
        # 切片的复选框
        self.slice_checkBox.stateChanged.connect(
            self.sclie_display_accomplish
        )
        # 切片x轴的滑动条的位置
        self.slicex_horizontalSlider.valueChanged.connect(
            # 发出信号
            # 1.输入框的值进行变动
            self.slicex_slider_move_accomplish
            # 2.重新绘制
        )
        # 切片y轴的滑动条的位置
        self.slicey_horizontalSlider.valueChanged.connect(
            self.slicey_slider_move_accomplish
        )
        # 切片z轴的滑动条的位置
        self.slicez_horizontalSlider.valueChanged.connect(
            self.slicez_slider_move_accomplish
        )
        # 切片x轴的文本框的输入
        self.slicex_lineEdit.editingFinished.connect(
            self.slicex_lineEdit_editingFinished_accomplish
        )
        # 切片y轴的文本框的输入
        self.slicey_lineEdit.editingFinished.connect(
            self.slicey_lineEdit_editingFinished_accomplish
        )
        # 切片z轴的文本框的输入
        self.slicez_lineEdit.editingFinished.connect(
            self.slicez_lineEdit_editingFinished_accomplish
        )
        # 等值面的复选框
        self.isosurface_checkBox.stateChanged.connect(
            self.isosurface_checkBox_accomplish
        )
        # 等值面 值 的滑动条
        self.isosurface_horizontalSlider.valueChanged.connect(
            self.isosurface_horizontalSlider_move_accomplish
        )
        # 等值面 等值面值的 文本框的输入
        self.isosurface_lineEdit.editingFinished.connect(
            self.isosurface_lineEdit_editingFinished_accomplish
        )

        # 等值面透明度滑动条的实现
        self.transparency_horizontalSlider.valueChanged.connect(
            self.transparency_horizontalSlider_move_accomplish
        )

        # 等值面中 透明度文本框的输入
        self.transparency_lineEdit.editingFinished.connect(
            self.transparency_lineEdit_editingFinished_accomplish
        )

        # 等值面绘制(菜单栏中的情况)
        self.isosurface_display.triggered.connect(
            self.isosurface_display_accomplish
        )
        # 等值面的复选框
        signal_sliceXYZ.connect(self.slot_slice_current_index)



    @Slot(str, int)
    def slot_slice_current_index(self, xyz, index):
        if(xyz == 'x'):
            self.slicex_horizontalSlider.setValue(index)
        if (xyz == 'y'):
            self.slicey_horizontalSlider.setValue(index)
        if (xyz == 'z'):
            self.slicez_horizontalSlider.setValue(index)

    # 切片的滑动条初始设置
    def slice_slider_init(self):
        # 如果是.bin数据的话，此时文件的打开还没有进行指定x,y,z的维度。此时x,y,z设置为1。防止数组越界
        x, y, z = sesimic_data[1], sesimic_data[2], sesimic_data[3]
        if (x <= 0 ):
            x = 1
        if (y <= 0):
            y = 1
        if (z <= 0):
            z = 1

        # 切片x的初始化
        self.slicex_horizontalSlider.setMinimum(0)
        self.slicex_horizontalSlider.setMaximum(x - 1)
        self.slicex_horizontalSlider.setTickInterval(1)
        self.slicex_horizontalSlider.setValue(0)
        self.slicex_lineEdit.setText("0")

        # 切片y的初始化
        self.slicey_horizontalSlider.setMinimum(0)
        self.slicey_horizontalSlider.setMaximum(y - 1)
        self.slicey_horizontalSlider.setTickInterval(1)
        self.slicey_horizontalSlider.setValue(0)
        self.slicey_lineEdit.setText("0")

        # 切片z的初始化
        self.slicez_horizontalSlider.setMinimum(0)
        self.slicez_horizontalSlider.setMaximum(z - 1)
        self.slicez_horizontalSlider.setTickInterval(1)
        self.slicez_horizontalSlider.setValue(0)
        self.slicez_lineEdit.setText("0")

    # 单独一个等值面的初始化设置
    def isosurface_slider_init(self):
        min_value, max_value = sesimic_data[0].min(), sesimic_data[0].max()
        print(int(min_value), int(max_value))

        self.isosurface_horizontalSlider.valueChanged.disconnect(self.isosurface_horizontalSlider_move_accomplish)
        self.isosurface_horizontalSlider.setMinimum(int(min_value))
        self.isosurface_horizontalSlider.setMaximum(int(max_value))
        self.isosurface_horizontalSlider.setValue(int(min_value) + 1)
        interval = int((max_value - min_value) / 20)
        self.isosurface_horizontalSlider.setTickInterval(interval)
        self.isosurface_lineEdit.setText("0")
        self.isosurface_horizontalSlider.valueChanged.connect(self.isosurface_horizontalSlider_move_accomplish)

        # 透明的滑动条初始化的设置
        # 先进行不关联这个函数
        self.transparency_horizontalSlider.valueChanged.disconnect(self.transparency_horizontalSlider_move_accomplish)
        opacity_interval = 1
        self.transparency_horizontalSlider.setMinimum(int(1)) # 之后需要缩小10倍，即0.1 - 1之间
        self.transparency_horizontalSlider.setMaximum(int(10))
        self.transparency_horizontalSlider.setValue(int(10))
        self.transparency_horizontalSlider.setTickInterval(opacity_interval)
        self.transparency_lineEdit.setText("1")
        self.transparency_horizontalSlider.valueChanged.connect(self.transparency_horizontalSlider_move_accomplish)

    # 打开文件
    def file_open_in(self):
        filter = "ALL files (*);;SEGY files (*.segy);;SGY files (*.sgy);;" \
                 "BIN files (*.bin);;NumPy files (*.npy);;VTK files (*.vtk)"
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                         filter)

        # 文件为空的话
        if(fileType == ""):
            return

        self.fileName_lineEdit.setText(fileName)

        # 定义一个函数，根据文件的后缀名，进行分辨出文件类型，并进行格式转化，将转化的文件进行输出
        p = ThreadAnalyseFile(func=analyse_filename, args=(fileName, ))
        p.start()
        p.join()
        file_section = p.get_result()

        if (file_section[1] == -1): # 这时候表示segy数据不是标准文件
            QMessageBox.critical(self, "错误", "segy文件不是标准的segy文件，请重新选择文件")

        # 输入三个维度，根据维度进行reshape数组
        else:
            global sesimic_data
            sesimic_data = file_section # 地震数据 np类型
            print(type(file_section))
            self.x_lineEdit.setText(str(file_section[1]))
            self.y_lineEdit.setText(str(file_section[2]))
            self.z_lineEdit.setText(str(file_section[3]))

        # 如果是.bin数据的话，此时文件的打开还没有进行指定x,y,z的维度
        # 调用函数，切片的滑动条设置
        self.slice_slider_init()
        # 调用函数, 单独等值面的初始化
        self.isosurface_slider_init()

    # 修改x的维度
    def modify_x(self):
        print("x is modify")
        global sesimic_data
        x = self.x_lineEdit.text()
        if (sesimic_data[1] != int(x)) :
            sesimic_data[1] = int(x)
            self.slice_slider_init()

    # 修改y的维度
    def modify_y(self):
        print("y is modify")
        global sesimic_data
        y = self.y_lineEdit.text()
        if (sesimic_data[2] != int(y)):
            sesimic_data[2] = int(y)
            self.slice_slider_init()

    # 修改z的维度
    def modify_z(self):
        print("z is modify")
        global sesimic_data
        z = self.z_lineEdit.text()
        if (sesimic_data[3] != int(z)):
            sesimic_data[3] = int(z)
            self.slice_slider_init()

    # 体绘制的实现
    def body_display_accomplish(self):
        print("体绘制函数启动")
        global sesimic_data
        if sesimic_data:
            x, y, z = sesimic_data[1], sesimic_data[2], sesimic_data[3]
            sesimic_data[0] = sesimic_data[0].reshape(x, y, z)
            mlab = surface_rendering(sesimic_data[0])
            self.setCentralWidget(mlab.show())

    # 断层自动追踪实现
    def fault_go_display_accomplish(self):
        global  sesimic_data
        x, y, z = sesimic_data[1], sesimic_data[2], sesimic_data[3]
        sesimic_data[0] = sesimic_data[0].reshape(x, y, z)
        if(x % 128 or y % 128 or z %128):
            print("输入的模型不是128x128x128的倍数")

        # 进行断层预测
        fault_data = fault_data_format_conversion(sesimic_data[0])
        fault_data[(fault_data >= 0.8) & (fault_data <= 1)] = 1
        slice_isosurfaces(sesimic_data[0], fault_data, [1])

    # 切片的实现
    def sclie_display_accomplish(self):
        print("切片函数启动")
        global sesimic_data
        if sesimic_data:
            x, y, z = sesimic_data[1], sesimic_data[2], sesimic_data[3]
            sesimic_data[0] = sesimic_data[0].reshape(x, y, z)
            slice(sesimic_data[0])

    # 切片x滑动条的实现
    def slicex_slider_move_accomplish(self):
        # 1.输入框的值进行变动
        x_index = self.slicex_horizontalSlider.value()
        self.slicex_lineEdit.setText(str(x_index))
        # 2.重新绘制,发出信号，让slice中进行接收处理
        global sliceXSliderSignal
        sliceXSliderSignal = SliceXorYorZSliderSignalClass()
        sliceXSliderSignal.signal.connect(slot_slice_xoryorz_slider)
        send_signal_slicexoryorz_slider(sliceXSliderSignal, 'x', x_index)

    # 切片y滑动条的实现
    def slicey_slider_move_accomplish(self):
        # 1.输入框的值进行变动
        y_index = self.slicey_horizontalSlider.value()
        self.slicey_lineEdit.setText(str(y_index))
        # 2.重新绘制,发出信号，让slice中进行接收处理
        sliceYSliderSignal = SliceXorYorZSliderSignalClass()
        sliceYSliderSignal.signal.connect(slot_slice_xoryorz_slider)
        send_signal_slicexoryorz_slider(sliceYSliderSignal, 'y', y_index)

    # 切片z滑动条的实现
    def slicez_slider_move_accomplish(self):
        # 1.输入框的值进行变动
        z_index = self.slicez_horizontalSlider.value()
        self.slicez_lineEdit.setText(str(z_index))
        # 2.重新绘制,发出信号，让slice中进行接收处理
        sliceZSliderSignal = SliceXorYorZSliderSignalClass()
        sliceZSliderSignal.signal.connect(slot_slice_xoryorz_slider)
        send_signal_slicexoryorz_slider(sliceZSliderSignal, 'z', z_index)

    # 切片x轴的文本框的输入
    def slicex_lineEdit_editingFinished_accomplish(self):
        slice_index = self.slicex_lineEdit.text()
        self.slicex_horizontalSlider.setValue(int(slice_index))

    # 切片y轴的文本框的输入
    def slicey_lineEdit_editingFinished_accomplish(self):
        slice_index = self.slicey_lineEdit.text()
        self.slicey_horizontalSlider.setValue(int(slice_index))

    # 切片z轴的文本框的输入
    def slicez_lineEdit_editingFinished_accomplish(self):
        slice_index = self.slicez_lineEdit.text()
        self.slicez_horizontalSlider.setValue(int(slice_index))

    # 等值面复选框的实现
    def isosurface_checkBox_accomplish(self):
        global sesimic_data
        if sesimic_data:
            x, y, z = sesimic_data[1], sesimic_data[2], sesimic_data[3]
            sesimic_data[0] = sesimic_data[0].reshape(x, y, z)
            min_value = int(sesimic_data[0].min()) + 1 # 第一开始刻画的等值面为最小值+1
            surface_render(sesimic_data[0], [min_value])


    # 单独一个等值面 值的 滑动条的实现
    def isosurface_horizontalSlider_move_accomplish(self):
        value = self.isosurface_horizontalSlider.value()
        self.isosurface_lineEdit.setText(str(value))
        opacity = self.transparency_horizontalSlider.value() * 0.1  # 透明度
        # 2. 进行重新绘制，让iso_surface中进行接收信号并出来
        isosurfaceSliderSignal = ISOSurfaceSliderSignalClass()
        isosurfaceSliderSignal.signal.connect(slot_iso_surface_slider)
        send_signal_isosurface_slider(isosurfaceSliderSignal, value, opacity)

    # 等值面中值出入框的实现
    def isosurface_lineEdit_editingFinished_accomplish(self):
        isosurface_value = self.isosurface_lineEdit.text()
        self.isosurface_horizontalSlider.setValue(int(isosurface_value))

    # 等值面中透明度滑动条的实现
    def  transparency_horizontalSlider_move_accomplish(self):
        value = self.isosurface_horizontalSlider.value()
        opacity = self.transparency_horizontalSlider.value() * 0.1  # (透明度的取值范围[0.1, 1]，而滑动条的值为1-10，所以需要缩小10倍）
        self.transparency_lineEdit.setText(str(opacity))

        # 透明度变了之后，进行重新绘制等值面
        isosurfaceSliderSignal = ISOSurfaceSliderSignalClass()
        isosurfaceSliderSignal.signal.connect(slot_iso_surface_slider)
        send_signal_isosurface_slider(isosurfaceSliderSignal, value, opacity)

    # 等值面中透明度输入框的实现
    def transparency_lineEdit_editingFinished_accomplish(self):
        opacity_value = self.transparency_lineEdit.text()
        opacity_value = int(float(opacity_value) * 10)
        self.transparency_horizontalSlider.setValue(opacity_value)

    # 等值面的实现
    def isosurface_display_accomplish(self):
        global sesimic_data
        if sesimic_data:
            x, y, z = sesimic_data[1], sesimic_data[2], sesimic_data[3]
            sesimic_data[0] = sesimic_data[0].reshape(x, y, z)
            contour3d_rendering(sesimic_data[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myDisplay3D = MyDisplay3D()
    sys.exit(app.exec())