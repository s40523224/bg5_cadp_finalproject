# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\github\scrum_cadp_final\eric6_project\marble_monitor\ui\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(273, 273)
        Dialog.setMinimumSize(QtCore.QSize(273, 273))
        Dialog.setMaximumSize(QtCore.QSize(273, 273))
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setMinimumSize(QtCore.QSize(50, 50))
        self.stop.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 1, 0, 2, 2)
        self.pause = QtWidgets.QPushButton(Dialog)
        self.pause.setMinimumSize(QtCore.QSize(100, 50))
        self.pause.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pause.setFont(font)
        self.pause.setObjectName("pause")
        self.gridLayout.addWidget(self.pause, 1, 2, 2, 1)
        self.display = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.display.setFont(font)
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setMinimumSize(QtCore.QSize(0, 50))
        self.start.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "鋼球運動系統控制板"))
        self.stop.setText(_translate("Dialog", "停止"))
        self.pause.setText(_translate("Dialog", "暫停"))
        self.label.setText(_translate("Dialog", "通過球數"))
        self.start.setText(_translate("Dialog", "啟動"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

