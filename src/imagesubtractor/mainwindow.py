from PySide2.QtWidgets import QMainWindow

from .mainwindowUI import MainWindowUI


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.ims = None
        self.outputdata = None
        self.roijsonfile = None
        self.roicol = None
