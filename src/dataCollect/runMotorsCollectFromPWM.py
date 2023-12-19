from socket import socket, AF_INET, SOCK_DGRAM
import proto.CommTypes_pb2 as pb
import time
import datetime
import numpy as np
import utils.utilslib as ul

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
    pwms = ul.loadPWMValues(f'/home/elisson/Documents/motors-data-collect/src/utils/random_pwm_values_with_seed_42.txt')
    # pwms = [15, -15, 0]
    
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
            has_msg, current_speeds, pwms, desired_speeds, timestamp = ul.recvSSLMessage(conn)
            if has_msg:
                log_msg = ul.serializeMsgToLog(current_speeds, pwms, desired_speeds, timestamp)
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
        path = ul.getResultsPath() + '/logs/motor_logs_' + formatted_datetime + '.csv'

        print(f"Saving motors log: {len(log)}")
        names = 'CURRENT_M1, CURRENT_M2, CURRENT_M3, CURRENT_M4, PWM_M1, PWM_M2, PWM_M3, PWM_M4, DESIRED_M1, DESIRED_M2, DESIRED_M3, DESIRED_M4, TIMESTAMP'
        np.savetxt(path, \
                   log,
                   delimiter=',',
                   header=names)
    else:
        print("Empty log!")
    
    print("Finish")
