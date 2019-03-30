import socket

HOST = "http://ec2-52-69-255-179.ap-northeast-1.compute.amazonaws.com:5000"
PORT = 5000
data = "Hello"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST,PORT))
s.sendto(data,(HOST,PORT))
print "send: "+ data