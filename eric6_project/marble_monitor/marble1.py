from remoteapi import vrep
import math
import sys

# child threaded script: 
#simExtRemoteApiStart(19999)
#
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

#啟動模擬
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

 
errorCode1,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint',vrep.simx_opmode_oneshot_wait)
errorCode2,sensorHandle=vrep.simxGetObjectHandle(clientID,'Finish',vrep.simx_opmode_oneshot_wait)

deg = math.pi/180

count = 0
count1 = 0

if errorCode1 == -1:
    print('Can not find left or right motor')
    sys.exit()
    
while vrep.simxGetConnectionId(clientID) != -1:
    (errorCode3, detectionState1, detectedPoint1, detectedObjectHandle1, detectedSurfaceNormalVector1) = vrep.simxReadProximitySensor(clientID, sensorHandle, vrep.simx_opmode_streaming)
    if errorCode3 == vrep.simx_return_ok:
        if detectionState1:
            count += 1
            print("通過球總數:", count)
     
     
    errorCode4=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint_handle,0.5, vrep.simx_opmode_oneshot_wait)
    
    
    '''
    def setJointPosition(incAngle, steps):
        for i  in range(steps):
            errorCode4=vrep.simxSetJointPosition(clientID, Revolute_joint_handle, i*incAngle*deg, vrep.simx_opmode_oneshot_wait)
        #終止模擬
        vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
     
    # 每步 10 度, 轉兩圈
    setJointPosition(10, 720)
    '''

    #print("通過球總數:", count)
