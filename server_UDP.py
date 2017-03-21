from socket import *
import random
import time
import math
import sys

try:
        sock = socket(AF_INET,SOCK_DGRAM)
        port = 44711

        sock.bind(('',port))
        #sock.listen(6)

        def check_int(check):
                if isinstance(check,int):
                        return True
                else:
                        return False

        while True:
           rando = random.random() #generates a random number to simulate the unreliable environment
           mess_init,addr = sock.recvfrom(4096)
           mess = mess_init.decode()

           if rando < 0.9:
               print "Dropped packet from addres: "+str(addr)
               continue
           else:
              #mess = sock.recv(1024).decode()
                try:
                      if "+" in mess:
                         left_op = int(mess.split("+")[0],10)
                         right_op = int(mess.split("+")[1].replace('\n','').replace(' ',''),10)

                         result = str(left_op + right_op)
                 #        sock.send("Now that's something I can do!\n".encode())
                         sock.sendto("200\n"+result+"\n".encode(),addr)
                         continue
                      elif "-" in mess:
                         left_op = int(mess.split("-")[0],10)
                         right_op = int(mess.split("-")[1].replace('\n','').replace(' ',''),10)
                         result = str(left_op - right_op)
                  #          sock.send("Now that's something I can do!\n".encode())
                         sock.sendto("200\n"+result+"\n".encode(),addr)
                         continue
                      elif "*" in mess:
                         left_op = int(mess.split("*")[0],10)
                         right_op = int(mess.split("*")[1].replace('\n','').replace(' ',''),10)
                         result = str(left_op * right_op)
                   #         sock.send("Now that's something I can do!\n".encode())
                         sock.sendto("200\n"+result+"\n".encode(),addr)
                         continue

                      elif "/" in mess:
                         left_op = int(mess.split("/")[0],10)
                         right_op = int(mess.split("/")[1].replace('\n','').replace(' ',''),10)
                         if right_op == 0:
                            sock.sendto("300\n\n\n\n\nYou tried to divide by zero......That's an error(-1)\n".encode(),addr)
                    #            sock.send("\nTry again\n".encode())
                            continue
                         result = str(left_op / right_op)
                     #       sock.send("Now that's something I can do!\n".encode())
                         sock.sendto("200\n"+result+"\n".encode(),addr)
                         continue
                      # elif "Q" in mess:
                         # sock.close()
                         # break
                      else:
                         sock.sendto("300\n\n\n\n\nThat's not something I can do......That's an error(-1)\n".encode(),addr)
                     #       sock.send("Try again\n".encode())
                         continue
                except ValueError:#If the client sends a value that is not an integer, send a 300 and (-1) code back
                        sock.sendto("300\n\n\n\n\nYou didn't give me an int!.....That's an error(-1)\n".encode(),addr)
                    #            sock.send("\nTry again\n".encode())
                        continue
except KeyboardInterrupt:
        print "\n\nGood bye!\n"
        exit(-1)

