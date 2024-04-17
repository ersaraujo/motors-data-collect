import os
import time
import random
import datetime
import numpy as np
import proto.CommTypes_pb2 as pb
from socket import socket, AF_INET, SOCK_DGRAM

class Utils:
    def getLogsPath():
        return getFolderPath('results/logs')

    def getPlotsPath():
        return getFolderPath('results/plots')

    def getResultsPath():
        return getFolderPath('results')

    def getPWMPath():
        return Utils.getFolderPath('pwm_inputs')

    def getSpeedPath():
        return Utils.getFolderPath('speed_inputs')

    def getFolderPath(subfolder):
        cur_path = os.getcwd()
        proj_path = os.path.abspath(os.path.join(cur_path, os.pardir))
        path = os.path.join(proj_path, subfolder)
        return path

    def generateRandomValues(start, end, count, seed):
        random.seed(seed)
        random_values = [round(random.uniform(start, end), 1) for _ in range(count)]
        # TODO: Save values to file
        return random_values
    
    def loadPWMValues(file):
        # TODO: Check if file exists
        if not os.path.exists(file):
            print('No PWM values found')
            seed = int(input('Define seed and press enter to generate new values: '))
            pwms = Utils.generateRandomValues(-25, 25, 30, seed)
            Utils.savePWMValues(seed, pwms)
        else:
            pwms = np.loadtxt(file)
            
        return pwms

    def savePWMValues(seed, values):
        path = Utils.getPWMPath() + f'/pwm_values_{seed}.txt'
        np.savetxt(path, values)

    def getPWMValues(seed = 42):
        file = Utils.getPWMPath() + f'/pwm_values_{seed}.txt'
        return Utils.loadPWMValues(file)

class Comm:
    def __init__(self, server, pc_port, robot_port):
        self.server = server
        self.portPC = pc_port
        self.portRobot = robot_port

        self.conn = socket(AF_INET, SOCK_DGRAM)
        self.conn.bind(('', self.portRobot))
        self.conn.settimeout(0)

        self.msg = pb.protoRobotSpeed()

    def __send(): 
        self.conn.sendto(self.msg.SerializeToString(), (self.server, self.portPC))
    
    def sendCommand(self, repeats=3, interval=1, sleep=0.25, values=[]):
        log = []
        for value in values:
            self.msg.vx = value
            self.msg.vy = 0
            self.msg.w = 0

            start = time.time()
            while True:
                time.sleep(sleep/1000)

                has_msg, current_speeds, pwms, desired_speeds, timestamp = self.recvSSLMessage()
                if has_msg:
                    log_msg = self.serializeMsgToLog(current_speeds, pwms, desired_speeds, timestamp)
                    log.append(log_msg)
                    print(pwms)

            elapsed_time = time.time() - start

            if elapsed_time > interval:
                for i in range(repeats):
                    self.__send()
                    print(f'Sent command {i+1}/{repeats}')
                print(f'Current msg elapsed time: {elapsed_time:.3f}')
                print(f'{msg}')
                break

        if len(log) > 0:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            path = Utils.getLogsPath() + '/motor_logs_' + formatted_datetime + '.csv'
            print(f"Saving motors log: {len(log)}")
            names = 'CURRENT_M1, CURRENT_M2, CURRENT_M3, CURRENT_M4, PWM_M1, PWM_M2, PWM_M3, PWM_M4, DESIRED_M1, DESIRED_M2, DESIRED_M3, DESIRED_M4, TIMESTAMP'
            np.savetxt(path, log, delimiter=',', fmt='%s', header=names)
        else:
            print('No logs to save')

        print('Finished sending commands')

    def serializeMsgToLog(current_speeds, pwms, desired_speeds, timestamp):
        return current_speeds[0], current_speeds[1], current_speeds[2], current_speeds[3], \
                pwms[0], pwms[1], pwms[2], pwms[3], \
                desired_speeds[0], desired_speeds[1], desired_speeds[2], desired_speeds[3], \
                timestamp

    def recvSSLMessage(self):
        has_msg = False
        msg = pb.protoMotorsDataSSL()

        while True:
            try:
                data, addr = self.conn.recvfrom(1024)
                msg.ParseFromString(data)
                has_msg = True
            except:
                break
                
        current_speeds = [msg.current_m1, msg.current_m2, msg.current_m3, msg.current_m4]
        pwms = [msg.pwm_m1, msg.pwm_m2, msg.pwm_m3, msg.pwm_m4]
        desired_speeds = [msg.desired_m1, msg.desired_m2, msg.desired_m3, msg.desired_m4]
        timestamp = msg.msgTime
        
        return has_msg, current_speeds, pwms, desired_speeds, timestamp
