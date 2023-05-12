from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QToolButton, QWidget

class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # 创建一个水平布局
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        # 创建一个最小化按钮
        self.minimize_button = QToolButton()
        self.minimize_button.setIcon(QIcon('minimize.png'))
        self.minimize_button.setToolTip('最小化')
        self.minimize_button.clicked.connect(parent.showMinimized)
        layout.addWidget(self.minimize_button)

        # 创建一个最大化/还原按钮
        self.maximize_button = QToolButton()
        self.maximize_button.setIcon(QIcon('maximize.png'))
        self.maximize_button.setToolTip('最大化')
        self.maximize_button.clicked.connect(self.toggleMaximized)
        layout.addWidget(self.maximize_button)

        # 创建一个关闭按钮
        self.close_button = QToolButton()
        self.close_button.setIcon(QIcon('close.png'))
        self.close_button.setToolTip('关闭')
        self.close_button.clicked.connect(parent.close)
        layout.addWidget(self.close_button)

    def toggleMaximized(self):
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()
