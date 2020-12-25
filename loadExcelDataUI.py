import sys

# from PyQt5.uic.properties import QtWidgets ## Error import
import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from loadExcelData import Ui_MainWindow
from plotTimeFrequencyDomain import plotTimeFrequencyDomain


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loadExcelBefore_button.clicked.connect(self.buttonClicked1)
        self.ui.loadExcelAfter_button.clicked.connect(self.buttonClicked2)

    def buttonClicked1(self):
        global beforeMedianFrequency
        filename = self.openFileNameDialog()
        print(filename)
        self.show()
        # plotTimeFrequencyDomain()
        data = pd.read_csv(filename, skiprows=4, usecols=[3, 5])
        LRec = data.iloc[:, 1]
        beforeMedianFrequency = plotTimeFrequencyDomain(LRec)
        beforeMedianFrequency = round(float(beforeMedianFrequency), 4)


        # self.ui.textBrowser.setText(str(data))

    def buttonClicked2(self):
        global afterMedianFrequency
        filename = self.openFileNameDialog()
        print(filename)
        self.show()
        # plotTimeFrequencyDomain()
        data = pd.read_csv(filename, skiprows=4, usecols=[3, 5])
        LRec = data.iloc[:, 1]
        afterMedianFrequency = plotTimeFrequencyDomain(LRec)
        afterMedianFrequency = round(float(afterMedianFrequency), 4)
        print("beforeMedianFrequency" ,  beforeMedianFrequency)
        print("afterMedianFrequency" ,  afterMedianFrequency)
        fatigueIndex = ((beforeMedianFrequency - afterMedianFrequency) / beforeMedianFrequency) * 100
        print("fatigueIndex = ", fatigueIndex)




    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;csv Files (*.csv)", options=options)
        if fileName:
            # print(fileName)
            return fileName


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    # pip install numpy==1.19.3
