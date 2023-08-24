from socket import socket, AF_INET, SOCK_DGRAM
import CommTypes_pb2 as pb

UDP_PORT = 9601

scktReceiver = socket(AF_INET, SOCK_DGRAM)
scktReceiver.bind(('',UDP_PORT))

feedbackMsg = pb.protoOdometry()

while True:
    message, clientAddress = scktReceiver.recvfrom(1024)
    feedbackMsg.ParseFromString(message)
    print(f"X: {feedbackMsg.x} | Y: {feedbackMsg.y} | W: {feedbackMsg.w} | ball: {feedbackMsg.hasBall} | batt: {feedbackMsg.battery}")
    