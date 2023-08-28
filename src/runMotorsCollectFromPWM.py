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
        current_speeds = [msg.current_m1, msg.current_m2, msg.current_m3, msg.current_m4]
        pwms = [msg.pwm_m1, msg.pwm_m2, msg.pwm_m3, msg.pwm_m4]
        desired_speeds = [msg.desired_m1, msg.desired_m2, msg.desired_m3, msg.desired_m4]
        timestamp = msg.msgTime
        
        return has_msg, current_speeds, pwms, desired_speeds, timestamp

def serializeMsgToLog(current_speeds, pwms, desired_speeds, timestamp):
    return current_speeds[0], current_speeds[1], current_speeds[2], current_speeds[3], \
        pwms[0], pwms[1], pwms[2], pwms[3], \
        desired_speeds[0], desired_speeds[1], desired_speeds[2], desired_speeds[3], \
        timestamp

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
    # pwms = load_pwm_values(f'./pwm_inputs/random_pwm_values_with_seed_{seed}.txt')
    pwms = [15, -15, 0]
    
    # CONFIGURE TIME BETWEEN MESSAGES
    msg_times = 3                        # REPEATS EACH MESSAGE 3 TIMES FOR RELIABILITY
    time_between_msgs = 1                # EXECUTES EACH COMMAND FOR 1 SECONDS
    sleep_between_iterations_ms = 0.25   # SLEEPS FOR 0.25 SECONDS AT EACH ITERATION
    
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
            has_msg, current_speeds, pwms, desired_speeds, timestamp = recvSSLMessage(conn)
            if has_msg:
                log_msg = serializeMsgToLog(current_speeds, pwms, desired_speeds, timestamp)
                log.append(log_msg)
                print(pwms)

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
        names = 'CURRENT_M1, CURRENT_M2, CURRENT_M3, CURRENT_M4, PWM_M1, PWM_M2, PWM_M3, PWM_M4, DESIRED_M1, DESIRED_M2, DESIRED_M3, DESIRED_M4, TIMESTAMP'
        np.savetxt(f'./results/motor_log_{formatted_datetime}.csv', \
                   log,
                   delimiter=',',
                   header=names)
    else:
        print("Empty log!")
    
    print("Finish")
