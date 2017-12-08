# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
        # 啟動時, 等待輸入運算數
        self.waitingForOperand = True
        
        # 顯示幕起始
        self.display.setText('0')
        
        # clear 按鍵 slot 設定 
        self.clearButton.clicked.connect(self.clear)
        
        digits = [self.one,  self.two,  self.three, \
            self.four,  self.five,  self.six, \
            self.seven,  self.eight,  self.nine,  self.zero]
            
        for i in digits:
            i.clicked.connect(self.digitClicked)
        #self.one.clicked.connect(self.digitClicked)
        
    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
        
        # 處理顯示幕為 0 或輸入 0.0 時
        if self.display.text() == '0' and digitValue == 0.0:
            return
            
        # 切換是否等待輸入運算數狀態, 一開始等待運算數, 一有輸入值, 則刷新顯示幕
        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False
            
        self.display.setText(self.display.text() + str(digitValue))
        
    def clear(self):
        # 清除顯示幕, 回復到原始顯示 0
        self.display.setText('0')
        # 重置判斷是否等待輸入運算數狀態
        self.waitingForOperand = True
