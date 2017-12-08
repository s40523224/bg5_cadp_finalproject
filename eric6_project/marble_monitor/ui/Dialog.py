# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
# 從 PyQt5.QtWidgets 模組中導入 QDialog 類別
from PyQt5.QtWidgets import QDialog
# 從同目錄中的 Ui_Dialog.py 模組導入 Ui_Dialog 類別
from .Ui_Dialog import Ui_Dialog

# for V-rep
# 從 remoteapi 目錄中導入 vrep.py 模組
from remoteapi import vrep
import sys
# 導入 threading, 用於建立執行緒
import threading
import time


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
        # count, clientID, very_beginning, make 與 pill2kill 都是類別的成員屬性
        self.count = 0
        self.clientID = 0
        self.very_beginning = True
        # 以 self.start_thread 為標的, 建立執行緒
        self.make = threading.Thread(target=self.start_thread)
        self.pill2kill = threading.Event()
        # 從 Ui_Dialog 繼承而來的成員物件
        self.display.setText(str(self.count))
        # 為三個 press button 建立 signals 與 slots 對應
        self.start.clicked.connect(self.start_motor)
        self.stop.clicked.connect(self.stop_motor)
        self.pause.clicked.connect(self.pause_motor)
        
    # 啟動轉動馬達的 slot, 也就是按下 self.start 按鈕後將執行的對應方法
    def start_motor(self):
        # 利用執行緒執行 start, 執行緒只能啟動一次的判斷成員變數 self.very_beginning
        if self.very_beginning:
            # 啟動執行緒
            self.make.start()
            self.very_beginning = False
        else:
            # 暫停後, 重啟執行緒
            self.pill2kill.set
            #啟動模擬
            vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_oneshot)
     
     # 停止馬達執行方法
    def stop_motor(self):
        # 按下停止鍵, 將會停止模擬, 重新回到原始設定畫面
        vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)
    
    # 暫停執行處理方法
    def pause_motor(self):
        # 暫停執行緒, 暫停模擬
        #time.sleep(2)
        # 暫停執行緒
        self.pill2kill.clear()
        # 暫停模擬
        vrep.simxPauseSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)
    
    # 啟動執行緒的對應方法
    def start_thread(self):
        # child threaded script: 
        # 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
        #simExtRemoteApiStart(19999)
         
        vrep.simxFinish(-1)
         
        self.clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
        
        #啟動模擬
        vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_oneshot)
        
        if self.clientID!= -1:
            print("Connected to remote server")
        else:
            print('Connection not successful')
            sys.exit('Could not connect')
         
        errorCode1, Revolute_joint_handle = vrep.simxGetObjectHandle(self.clientID,'Revolute_joint',vrep.simx_opmode_oneshot_wait)
        errorCode2, sensorHandle = vrep.simxGetObjectHandle(self.clientID,'Finish',vrep.simx_opmode_oneshot_wait)
        
        if errorCode1 == -1:
            print('Can not find left or right motor')
            sys.exit()
            
        while vrep.simxGetConnectionId(self.clientID) != -1:
            (errorCode3, detectionState1, detectedPoint1, detectedObjectHandle1, detectedSurfaceNormalVector1) = vrep.simxReadProximitySensor(self.clientID, sensorHandle, vrep.simx_opmode_streaming)
            if errorCode3 == vrep.simx_return_ok:
                if detectionState1:
                    self.count += 1
                    print("通過球總數:", self.count)

            # 將 self.count 顯示在 display
            self.display.setText(str(self.count))
            # 設定馬達的轉速
            vrep.simxSetJointTargetVelocity(self.clientID, Revolute_joint_handle, 0.5, vrep.simx_opmode_oneshot_wait)
    
        #終止模擬
        vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)
