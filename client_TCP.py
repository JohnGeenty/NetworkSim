from socket import *

#Set up the TCP stream socket
client_s = socket(AF_INET,SOCK_STREAM)
#Declare both the server IP and the port number
SERVER = '127.0.0.1'
PORT = 40404

#Connect the client to the server on port 'PORT'
client_s.connect((SERVER,PORT))

#Begin the while loop
while True:
#    output = client_s.recv(1024).decode()
#   Request input from the user
    print "Please give me a mathmatical equation in the form (0-9) (+,-,*,/) (1-9)\n"
    message = raw_input(">")
#   If the user wants to quit, exit the while loop
    if 'Q' in message:
        client_s.send("Q".encode())
        # client_s.close()
        break
#   Send the message the server and receive feedback
    client_s.send(message)
    result = client_s.recv(2048).decode()
    if '200' in result:#If the input was valid, we will get a code 200 OK message
        print result
        continue
    if '300' in result:#If the input was not valid, we will get a code 300 and a descriptive message
        print result
        continue

client_s.close()# If we exit the loop, we will immediately close the connection
