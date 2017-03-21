from socket import *
import random
import time

#Prepare the socket as a datagram socket
client_s = socket(AF_INET,SOCK_DGRAM)
SERVER = '127.0.0.1'
PORT = 44711

addr = (SERVER,PORT)

d = 0.1 # Timeout value
while True:
    #Recieve input from the user
    client_s.settimeout(d)
    print "Please give me a mathmatical equation in the form (0-9) (+,-,*,/) (1-9)\n"
    message = raw_input(">")

    if 'Q' in message:
        break

    try:
        #Send the input to the server
        client_s.sendto(message.encode(),addr)
        result_init,addr = client_s.recvfrom(1024)
        result = result_init.decode()
        #Recieve the result back from the server and the status code
        if '200' in result:
            print result
            continue
        if '300' in result:
            print result
            continue
    except timeout:
        #This will be executed if the server drops a packet. This happens with probabilty 0.5
        d = 2*d
        if d > 2:#This indicates that the server is dead and cannot recieve a clear conneciton, so we close our datagram socket
            print "DEAD SERVER!\n"
            break
        continue

client_s.close()
