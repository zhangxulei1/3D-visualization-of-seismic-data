import numpy as np
from mayavi import mlab
from tools import Colorbar, Font

from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


surfaces = None
source = None

class IsoSurfaceSignal(QObject):
    pyqtSignal(int, float)  # 暂时没有用到这个

# 槽函数
# 接收来自于app_main函数中的信号surface_slider
@pyqtSlot(int, float)
def slot_iso_surface_slider(value, opacity):
    global surfaces

    print("slot_surface_slider接收到了信号")
    # 更新等值线列表
    new_surfaces = mlab.pipeline.iso_surface(source, contours=[value], opacity=opacity, colormap="bone")
    surfaces.remove()
    # 更新 surfaces 对象
    surfaces = new_surfaces
    print("mlab.draw()之前")

    mlab.draw()

# 特定值的等值面的绘制(可以带有透明的那种)
def surface_render(data, contours, opacity=None, colormap=None, colorbar_list=None,
                         colorbar_min=None, colorbar_max=None, font_list=None):
    """
    :param data:
    :param contours: 等值面的数 即固定数的数组[2000,3000] 表示绘制值为2000，3000的面
    :param opacity: 整体的透明度(0.0 - 1.0)
    :param colormap: 色棒映射
    :param colorbar_list: 色棒中的参数
    :param colorbar_min: 色棒中的最小值
    :param colorbar_max: 色棒中的最大值
    :param font_list: 字体中的参数
    :return:
    """
    global source
    source = mlab.pipeline.scalar_field(data)

    if opacity is None:
        opacity = 0.5

    if colormap is None:
        colormap = 'jet'

    if colorbar_list is None:
        colorbar_list = Colorbar()
        colorbar_list.init_vertical()

    if colorbar_min is None:
        colorbar_min = data.min()

    if colorbar_max is None:
        colorbar_max = data.max()

    if font_list is None:
        font_list = Font()
        font_list.init_none()

    global surfaces
    # 函数创建另一个等值面，并设置等值面的轮廓值为 s.max() - 0.1 * s.ptp()，透明度默认为 0.5，并将其添加到场景中
    surfaces = mlab.pipeline.iso_surface(source, contours=contours, opacity=opacity, colormap=colormap)

    # 函数创建三维等高线，并设置轮廓数为400，透明度为True，颜色映射为'jet'，并将其添加到场景中。
    #mlab.contour3d(data, contours=contours, transparent=True, colormap=colormap, opacity=opacity, vmin=colorbar_min, vmax=colorbar_max)
    # 添加色棒
    cb = mlab.colorbar(title=colorbar_list.title, orientation=colorbar_list.orientation,
                       nb_labels=colorbar_list.nb_labels, label_fmt=colorbar_list.label_fmt)
    cb.label_text_property.font_family = font_list.font_family
    cb.title_text_property.trait_set(font_size=font_list.font_title_size)
    cb.label_text_property.trait_set(font_size=font_list.font_label_size)

    # mlab.outline()
    #mlab.gcf().scene.show_toolbar = True
    mlab.show()


if __name__ == "__main__":
    # 进行测试
    print("iso_surface_renser")
    data = np.load("D:/segy/bin_data/modelSlow_iter37_bin2npy.npy")
    surface_render(data, [2000, 3000])


