import numpy as np
from tvtk.api import tvtk, write_data
import segyio

# 格式转化函数
# segy2npy
def sgy2npy(segyfile, npyfile):
    """
    :param segyfile: 要输入的segy文件
    :param npyfile: 要输出的npyfile文件
    :return: 返回0表示函数成功执行
    """
    try:
        seismic = segyio.tools.cube(segyfile)
        print(type(seismic))
        print(seismic.shape)
        np.save(npyfile, seismic)
    except Exception as e:
        print("读取segy文件时，出现异常:" + e)
    return 0


# bin2npy
def bin2npy(binfile, npyfile, x, y, z):
    """
    :param binfile: 要传入的二进制文件
    :param npyfile: 要保存的npy文件
    :param x: x方向的维度
    :param y: y方向的维度
    :param z: z方向的维度
    :return:
    """
    with open(binfile, "rb") as f:
        rectype = np.dtype(np.float32)
        bdata = np.fromfile(f, dtype=rectype)

    data = bdata.reshape(x, y, z)
    np.save(npyfile, data)


# npy2vtk
def npy2vtk(npydata_inpath, vtkdata_outpath, x=None, y=None, z=None):
    """
    :param npydata_inpath: npy数据的文件名，输入的NumPy数据文件路径
    :param vtkdata_outpath: vtk数据的保存路径+文件名，输出的VTK数据文件路径
    :param x, y, z: vtk的维度即三维的维度，VTK数据的三维维度
    :return: 返回0表示成功输出了vtk数据，返回0表示函数执行成功
    """
    # Load NumPy data from the input file path
    data = np.load(npydata_inpath)

    if x is None:
        x = data.shape[0]
    if y is None:
        y = data.shape[1]
    if z is None:
        z = data.shape[2]

    print(data.shape, x, y, z)

    # Create an ImageData object with specified spacing, origin, and dimensions
    # 创建一个具有指定间距、原点和维度的ImageData对象
    grid = tvtk.ImageData(spacing=(1, 1, -1), origin=(x, y, z),
                          dimensions=data.shape)

    # Set the scalar values of the ImageData object to the flattened data array
    # from the NumPy data
    # 将ImageData对象的标量值设置为来自NumPy数据的展平数据数组
    grid.point_data.scalars = data.ravel(order='F')

    # Set the name of the scalar data
    # 设置标量数据的名称
    grid.point_data.scalars.name = 'vtk_vv Data'

    # Write the ImageData object to a VTK file at the specified output path
    # 使用指定的输出路径将ImageData对象写入VTK文件
    write_data(grid, vtkdata_outpath)
    return 0



