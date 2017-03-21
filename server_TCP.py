from socket import *
import sys

# Try to run the server, and if you want to quit, send a SIGINT (^C) and the server will stop running

try:
    #Create the stream socket and set the port number to listen on
    sock = socket(AF_INET,SOCK_STREAM)
    port = 40404

    #Bind the socket to localhost and the port number previsouly defined
    sock.bind(('127.0.0.1',port))

    #Listen on the socket
    sock.listen(6)

    while True:
        #Accept an incoming connection
        conn,addr = sock.accept()
        while True:
            try:
                #Recieve a new 'query'
                mess = conn.recv(1024).decode()

                #Parse the input and send the corresponding 200 code or 300 code depending on the input from the user
                if "+" in mess:
                    left_op = int(mess.split("+")[0],10)
                    right_op = int(mess.split("+")[1].replace('\n','').replace(' ',''),10)
                    result = str(left_op + right_op)
         #           conn.send("Now that's something I can do!\n".encode())
                    conn.send("200\n"+result+"\n".encode())
                    continue
                elif "-" in mess:
                    left_op = int(mess.split("-")[0],10)
                    right_op = int(mess.split("-")[1].replace('\n','').replace(' ',''),10)
                    result = str(left_op - right_op)
          #          conn.send("Now that's something I can do!\n".encode())
                    conn.send("200\n"+result+"\n".encode())
                    continue
                elif "*" in mess:
                    left_op = int(mess.split("*")[0],10)
                    right_op = int(mess.split("*")[1].replace('\n','').replace(' ',''),10)
                    result = str(left_op * right_op)
           #         conn.send("Now that's something I can do!\n".encode())
                    conn.send("200\n"+result+"\n".encode())
                    continue

                elif "/" in mess:
                    left_op = int(mess.split("/")[0],10)
                    right_op = int(mess.split("/")[1].replace('\n','').replace(' ',''),10)
                    if right_op == 0:
                        conn.send("300\n\n\n\n\nYou tried to divide by zero......That's an error(-1)".encode())
            #            conn.send("\nTry again\n".encode())
                        continue
                    result = str(left_op / right_op)
             #       conn.send("Now that's something I can do!\n".encode())
                    conn.send("200\n"+result+"\n".encode())
                    continue
                elif "Q" in mess:
                    conn.close()
                    break
                else:
                    conn.send("300\n\n\n\n\nThat's not something I can do......That's an error(-1)\n".encode())
             #       conn.send("Try again\n".encode())
                    continue
            except ValueError:
                conn.send("300\n\n\n\n\nYou didn't give me an int!......That's an error(-1)\n".encode())
            #            conn.send("\nTry again\n".encode())
                continue
            except KeyboardInterrupt:
                break
    conn.close()
except KeyboardInterrupt:
    print "\n\nGood bye!"
    exit(-1)
