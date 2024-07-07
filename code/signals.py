from PySide2.QtCore import QObject, Signal

# 从slice中发出信号，app_main中进行接收信号（用来进行更新滑动条的值）
# 创建共享的信号对象
class SignalObject(QObject):
    signal_sliceXYZ = Signal(str, int)

signal_object_slice = SignalObject()
signal_sliceXYZ = signal_object_slice.signal_sliceXYZ


