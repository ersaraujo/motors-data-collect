from socket import socket, AF_INET, SOCK_DGRAM
import CommTypes_pb2 as pb
import time
import datetime
import numpy as np

def recvSSLMessage(udp_sock):
        msg = pb.protoMotorsDataSSL()
        # multiple messages are received and accumulated on buffer during vision processing
        # so read until buffer socket are no longer available
        has_msg = False
        while True:
            try:
                data, _ = udp_sock.recvfrom(1024)
                msg.ParseFromString(data)
                has_msg = True
            except:
                break 
        motors = [msg.m1, msg.m2, msg.m3, msg.m4]
        inputs = [msg.pwm1, msg.pwm2, msg.pwm3, msg.pwm4]
        timestamp = msg.msgTime
        
        return has_msg, motors, inputs, timestamp

def serializeMsgToLog(motors, inputs, timestamp):
    return motors[0], motors[1], motors[2], motors[3], inputs[0], inputs[1], inputs[2], inputs[3], timestamp

def load_pwm_values(file):
    pwms = np.loadtxt(file)
    return pwms

if __name__ ==  "__main__":
    # CONFIGURE UDP CONNECTION
    server = "199.0.1.1"
    pc2robot_port = 9600
    robot2pc_port = 9601
    msg = pb.protoMotorsPWMSSL()
    conn = socket(AF_INET, SOCK_DGRAM)
    conn.bind(('', robot2pc_port))
    conn.settimeout(0)

    # CHOOSE FILE FOR PWM VALUES
    seed = 42
    pwms = load_pwm_values(f'./pwm_inputs/random_pwm_values_with_seed_{seed}.txt')
    
    # CONFIGURE TIME BETWEEN MESSAGES
    msg_times = 3                       # REPEATS EACH MESSAGE 3 TIMES FOR RELIABILITY
    time_between_msgs = 3               # EXECUTES EACH COMMAND FOR 3 SECONDS
    sleep_between_iterations_ms = 0.5   # SLEEPS FOR 0.5 SECONDS AT EACH ITERATION
    
    log = []

    for pwm in pwms:
        msg.m1 = pwm
        msg.m2 = pwm
        msg.m3 = pwm
        msg.m4 = pwm
    
        # START MSG TIME COUNTER
        start = time.time()
        while True:
            # SLEEP
            time.sleep(sleep_between_iterations_ms/1000)

            # RECV MESSAGE
            has_msg, motors, inputs, timestamp = recvSSLMessage(conn)
            if has_msg:
                log_msg = serializeMsgToLog(motors, inputs, timestamp)
                log.append(log_msg)

            # COUNT TIME
            elapsed_time = time.time() - start

            # CHECK MSG SEND TIME
            if elapsed_time > time_between_msgs:
                # SEND AND PRINT MSG
                for i in range(msg_times):
                    conn.sendto(msg.SerializeToString(), (server, pc2robot_port))
                print(f'Current msg elapsed time: {elapsed_time:.3f}')
                print(f'{msg}')
                break

    if len(log)>0:
        # Get the current date and time
        current_datetime = datetime.datetime.now()
        
        # Format the date and time as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

        print(f"Saving motors log: {len(log)}")
        names = 'M1, M2, M3, M4, PWM1, PWM2, PWM3, PWM4, TIMESTAMP'
        np.savetxt(f'./results/motor_log_{formatted_datetime}.csv', \
                   log,
                   delimiter=',',
                   header=names)
    else:
        print("Empty log!")
    
    print("Finish")
