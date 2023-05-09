from PySide6.QtCore import Signal, QObject

class MySignal(QObject):
    # # 这个是为Result对象自定义的信号，包含一个str变量
    # setResult = Signal(str)
    # # 这个是为ProgressBar对象定义的信号，包含一个int变量
    # setProgressBar = Signal(int)
    pass

my_signal = MySignal()