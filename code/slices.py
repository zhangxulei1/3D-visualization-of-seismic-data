import numpy as np
from mayavi import mlab
from tools import Colorbar
from signals import signal_sliceXYZ
from PyQt6.QtCore import QObject, pyqtSignal

# 定义全局变量
slice_source = None
planes = []


class SliceXYZSignal(QObject):
    """包含整型参数的信号类"""
    signal = pyqtSignal(int, int)


def slice_send_signal(obj, xyz, slice_index):
    """发出信号的函数"""
    obj.signal.emit(xyz, slice_index)


def slot_slice_xoryorz_slider(xoryorz, slice_index):
    """接收信号的函数"""
    global planes
    print("slices中slot_slice_xoryorz_slider接收到了信号")
    plane = None
    if xoryorz == 'x':
        plane = planes[0]
        plane.ipw.slice_index = slice_index
        print(f'{xoryorz}轴方向,index={slice_index}')
    elif xoryorz == 'y':
        plane = planes[1]
        plane.ipw.slice_index = slice_index
        print(f'{xoryorz}轴方向,index={slice_index}')
    elif xoryorz == 'z':
        plane = planes[2]
        plane.ipw.slice_index = slice_index
    mlab.draw()


def slice_receive_signal(xyz, value):
    """信号接收函数"""
    print("接收到了信号", xyz, value)


def on_slice_change(obj, event):
    """注册回调函数"""
    my_signal = SliceXYZSignal()
    my_signal.signal.connect(slice_receive_signal)
    slice_index = obj.GetSliceIndex()
    normal = obj.GetNormal()

    if normal[0] == 1:
        print("当前切片方向为 X-轴方向")
        signal_sliceXYZ.emit('x', slice_index)
    elif normal[1] == 1:
        print("当前切片方向为 Y-轴方向")
        signal_sliceXYZ.emit('y', slice_index)
    elif normal[2] == 1:
        print("当前切片方向为 Z-轴方向")
        signal_sliceXYZ.emit('z', slice_index)


def slice(data, colormap='jet', colorbar_list=None, slices_list=None,
          slices_idx=None, colorbar_min=None, colorbar_max=None):
    """创建三个方向的切面"""
    global planes, slice_source

    slice_source = mlab.pipeline.scalar_field(data)
    slice_source.spacing = [1, 1, -1]

    slices_list = slices_list or ['x', 'y', 'z']
    colorbar_list = colorbar_list or Colorbar()
    colorbar_list.init_vertical()
    slices_idx = slices_idx or [0, 0, data.shape[2] - 1]
    colorbar_min = colorbar_min or data.min()
    colorbar_max = colorbar_max or data.max()

    for i, slice_axis in enumerate(slices_list):
        plane = mlab.pipeline.image_plane_widget(
            slice_source,
            plane_orientation=f'{slice_axis}_axes',
            slice_index=slices_idx[i],
            colormap=colormap
        )
        plane.ipw.add_observer('InteractionEvent', on_slice_change)
        planes.append(plane)

    scalar_lut_manager = mlab.scalarbar(
        plane, title=colorbar_list.title, orientation=colorbar_list.orientation,
        nb_labels=colorbar_list.nb_labels, label_fmt=colorbar_list.label_fmt
    )
    scalar_lut_manager.data_range = [colorbar_min, colorbar_max]

    mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    mlab.outline()
    mlab.show()


def slice_isosurfaces(data, faultdata, contours, colormap='jet', colorbar_list=None,
                      slices_list=None, slices_idx=None, colorbar_min=None, colorbar_max=None):
    """创建切片和等值面的实现"""
    global planes, slice_source

    slice_source = mlab.pipeline.scalar_field(data)
    slice_source.spacing = [1, 1, -1]

    slices_list = slices_list or ['x', 'y', 'z']
    colorbar_list = colorbar_list or Colorbar()
    colorbar_list.init_vertical()
    slices_idx = slices_idx or [0, 0, data.shape[2] - 1]
    colorbar_min = colorbar_min or data.min()
    colorbar_max = colorbar_max or data.max()

    for i, slice_axis in enumerate(slices_list):
        plane = mlab.pipeline.image_plane_widget(
            slice_source,
            plane_orientation=f'{slice_axis}_axes',
            slice_index=slices_idx[i],
            colormap=colormap
        )
        plane.ipw.add_observer('InteractionEvent', on_slice_change)
        planes.append(plane)

    scalar_lut_manager = mlab.scalarbar(
        plane, title=colorbar_list.title, orientation=colorbar_list.orientation,
        nb_labels=colorbar_list.nb_labels, label_fmt=colorbar_list.label_fmt
    )
    scalar_lut_manager.data_range = [colorbar_min, colorbar_max]

    mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    mlab.outline()

    fault_src = mlab.pipeline.scalar_field(faultdata)
    fault_src.spacing = [1, 1, -1]
    mlab.pipeline.iso_surface(fault_src, contours=contours, opacity=0.5, colormap=colormap)

    mlab.show()
