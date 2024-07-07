import numpy as np
from mayavi import mlab
from tools import Colorbar, Font

def surface_rendering(data, colormap='jet', colorbar_list=None,
                      colorbar_min=None, colorbar_max=None, font_list=None):
    """体绘制的方法（严格来说这里是一个曲面绘制）

    Args:
        data (numpy.ndarray): 三维npy数组数据
        colormap (str, optional): 色棒映射. 默认为 'jet'.
        colorbar_list (Colorbar, optional): 色棒参数列表. 默认为 None.
        colorbar_min (float, optional): 色棒最小值. 默认为 None.
        colorbar_max (float, optional): 色棒最大值. 默认为 None.
        font_list (Font, optional): 字体参数列表. 默认为 None.

    Returns:
        mlab: mayavi mlab对象
    """
    colorbar_list = colorbar_list or Colorbar()
    colorbar_list.init_vertical()

    colorbar_min = colorbar_min or data.min()
    colorbar_max = colorbar_max or data.max()

    font_list = font_list or Font()
    font_list.init_none()

    src = mlab.pipeline.scalar_field(data)
    src.spacing = [1, 1, -1]
    mlab.pipeline.surface(src, colormap=colormap, vmin=colorbar_min, vmax=colorbar_max)

    cb = mlab.colorbar(title=colorbar_list.title, orientation=colorbar_list.orientation,
                       nb_labels=colorbar_list.nb_labels, label_fmt=colorbar_list.label_fmt)
    cb.label_text_property.font_family = font_list.font_family
    cb.title_text_property.trait_set(font_size=font_list.font_title_size)
    cb.label_text_property.trait_set(font_size=font_list.font_label_size)

    mlab.outline()

    return mlab

def contour3d_rendering(data, contours=20, opacity=0.5, colormap='jet',
                        colorbar_list=None, colorbar_min=None, colorbar_max=None, font_list=None):
    """等值面的绘制（等值面数目给的足够多的时候，可以完成含有透明度的体绘制）

    Args:
        data (numpy.ndarray): 三维npy数组数据
        contours (int, optional): 等值面数目. 默认为 20.
        opacity (float, optional): 透明度 (0.0 - 1.0). 默认为 0.5.
        colormap (str, optional): 色棒映射. 默认为 'jet'.
        colorbar_list (Colorbar, optional): 色棒参数列表. 默认为 None.
        colorbar_min (float, optional): 色棒最小值. 默认为 None.
        colorbar_max (float, optional): 色棒最大值. 默认为 None.
        font_list (Font, optional): 字体参数列表. 默认为 None.
    """
    colorbar_list = colorbar_list or Colorbar()
    colorbar_list.init_vertical()

    colorbar_min = colorbar_min or data.min()
    colorbar_max = colorbar_max or data.max()

    font_list = font_list or Font()
    font_list.init_none()

    mlab.contour3d(data, contours=contours, transparent=True, colormap=colormap,
                   opacity=opacity, vmin=colorbar_min, vmax=colorbar_max)

    cb = mlab.colorbar(title=colorbar_list.title, orientation=colorbar_list.orientation,
                       nb_labels=colorbar_list.nb_labels, label_fmt=colorbar_list.label_fmt)
    cb.label_text_property.font_family = font_list.font_family
    cb.title_text_property.trait_set(font_size=font_list.font_title_size)
    cb.label_text_property.trait_set(font_size=font_list.font_label_size)

    mlab.outline()
    mlab.show()


if __name__ == "__main__":

    file_path = "D:/data/bin_data/Overthrust/SEG_EAGE_3DOverthrust_94x401x401_50m_bin2npy.npy"
    data = np.load(file_path)
    data_flipped = np.flip(data, axis=2)

    # 1.测试函数surface_rendering()
    mlab = surface_rendering(data)
    mlab.show()

    # 2. 测试函数contour3d_rendering()
    # contour3d_rendering(data_flipped, contours=100, opacity=0.99, colormap='jet')

