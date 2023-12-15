from socket import socket, AF_INET, SOCK_DGRAM
import CommTypes_pb2 as pb
import time
import datetime
import numpy as np
import utils.utilslib as ul

if __name__ ==  "__main__":
    server = "199.0.1.1"
    pc2robot_port = 9600
    robot2pc_port = 9601
    
    msg = pb.protoMotorsPWMSSL()
    conn = socket(AF_INET, SOCK_DGRAM)
    conn.bind(('', robot2pc_port))
    conn.settimeout(0)

    # CHANGE LIST TO PSEUDO-RANDOM VALUES GENERATED BY VICTOR
    sleep_between_iterations_ms = 0.25
    maximum_time_without_messages_s = 2
    
    log = []
    
    # START MSG TIME COUNTER
    start = time.time()
    msgTimeout = time.time()
    received_first_msg = False
    time_offset = 0
    last_timestamp = 0

    while True:
        # SLEEP
        time.sleep(sleep_between_iterations_ms/1000)

        # RECV MESSAGE
        has_msg, current_speeds, pwms, desired_speeds, timestamp_data = ul.recvSSLMessage(conn)
        if has_msg:
            if timestamp_data - last_timestamp < 0:
                time_offset += last_timestamp
            last_timestamp = timestamp_data
            log_msg = ul.serializeMsgToLog(current_speeds, pwms, desired_speeds, timestamp_data+time_offset)
            log.append(log_msg)
            received_first_msg = True
            msgTimeout = time.time()
        elif ((time.time() - msgTimeout) > maximum_time_without_messages_s) and received_first_msg:
            break

        # COUNT TIME
        elapsed_time = time.time() - start
        if (elapsed_time > 120) and received_first_msg:
            break

        #print(f'Elapsed msgTimeout: {time.time() - msgTimeout:.3f} | First Msg: {received_first_msg}')

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
