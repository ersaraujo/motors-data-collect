from socket import socket, AF_INET, SOCK_DGRAM
import CommTypes_pb2 as pb
import time

server = "199.0.1.1"
port = 9600

msg = pb.protoPositionSSL()
conn = socket(AF_INET, SOCK_DGRAM)

msg.x = 0
msg.y = 0
msg.w = 0
msg.posType = pb.protoPositionSSL.source
conn.sendto(msg.SerializeToString(), (server, port))

start = time.time()
msg_times = 5
execution_time = 5

feedbackMsg = pb.protoOdometry()
feedbackMsg.x = 1
feedbackMsg.y = 0
feedbackMsg.w = 0

while True:
    msg.x = 1
    msg.y = 0
    msg.w = 0
    msg.max_speed = 2
    elapsed_time = time.time() - start
    time.sleep(0.033)
    if elapsed_time > execution_time:
        msg.posType = pb.protoPositionSSL.stop
        msg.resetOdometry = False
    else:
        msg.posType = pb.protoPositionSSL.driveToTarget
    
    for i in range(0, msg_times):
        print(msg.SerializeToString())
        conn.sendto(msg.SerializeToString(), (server, port))

    # stringMsg = feedbackMsg.SerializeToString()
    # print(stringMsg)
    # feedbackMsg.ParseFromString(stringMsg)
    # print(feedbackMsg.x)
    # print(elapsed_time)

    if elapsed_time > execution_time:
        print("finish")
        break   