import CommTypes_pb2 as pb
import numpy as np
import os

def recvSSLMessage(udp_sock):
    msg = pb.protoMotorsDataSSL()
    hasMsg = False

    while True:
        try:
            data, _ = udp_sock.recvfrom(1024)
            msg.ParseFromString(data)
            hasMsg = True
        except:
            break
    
    current_speeds = [msg.current_m1, msg.current_m2, msg.current_m3, msg.current_m4]
    pwms = [msg.pwm_m1, msg.pwm_m2, msg.pwm_m3, msg.pwm_m4]
    desired_speeds = [msg.desired_m1, msg.desired_m2, msg.desired_m3, msg.desired_m4]
    timestamp = msg.msgTime

    return hasMsg, current_speeds, pwms, desired_speeds, timestamp

def serializeMsgToLog(current_speeds, pwms, desired_speeds, timestamp):
    return current_speeds[0], current_speeds[1], current_speeds[2], current_speeds[3], \
        pwms[0], pwms[1], pwms[2], pwms[3], \
        desired_speeds[0], desired_speeds[1], desired_speeds[2], desired_speeds[3], \
        timestamp

def loadPWMValues(file):
    pwms = np.loadtxt(file)
    return pwms

def getResultsPath(dir = '/results'):
    _path = os.getcwd()
    _path = _path.split('/')
    _path = '/'.join(_path[:-2])
    path = _path + dir
    return path