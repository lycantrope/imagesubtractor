# -*- coding: utf-8 -*-

"""
Created on Tue Dec  5 09:58:05 2017
Copyright (c) 2018, Taizo kawano

1 Run this script
2 Click the open button and select image files directory
3 Choose a roi col x row from drop down list or manually
4 Adjust xy position and interval of roi by sliders
5 Click start and wait for about 40 min
6 Click save to save csv file in the image directory.
the csv file will be used later processing part.



Refactored on Thu Jun 17 12:43:46 2020
@author: Kuan
"""

import os
import sys
from pathlib import Path

import PySide2

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.fspath(
    Path(PySide2.__file__).resolve().parent / "Qt" / "plugins"
)
from PySide2 import QApplication
import cv2

from .mainwindow import MainWindow


def main(argv):
    try:
        app = QApplication(argv)
        appUI = MainWindow()
        appUI.show()
        appUI.raise_()
        app.exec_()
    finally:
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


if __name__ == "__main__":
    main(sys.argv[1:])