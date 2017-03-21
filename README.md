#NetworkSim

##synopsis

This is a client/server interaction written in python. Implementing both datagram (UDP) and stream (TCP) sockets. Each type of socket has a client and a corressponding server.

## Running the program

Open a terminal window and type:
```
python server_TCP.py
```

Then open another terminal window and type:
```
python client_TCP.py
```

NOTE: If you wanted to use the UDP version, just replace TCP with UDP

After you run the previous command, you will prompted with:

```
Please give me a mathmatical equation in the form (0-9) (+,-,*,/) (1-9)

>
```

At this point, you have to enter a mathmatical equation, for example:

```
>5+5
```

Will Return

```
200
10
```

If you input any other type of character, you will get a code 300 message:

```
300




That's not something I can do......That's an error(-1)
```
OR

```
300




You didn't give me an int!......That's an error(-1)
```

The UDP works the same way except for when you lose a packet. When you lost a packet, the client terminal window will look like:

```
Please give me a mathmatical equation in the form (0-9) (+,-,*,/) (1-9)

>5+5
Please give me a mathmatical equation in the form (0-9) (+,-,*,/) (1-9)

>
```

The server will output on its terminal window:

```
Dropped packet from addres: ('127.0.0.1', 53192)
```

The client will render the server dead if there are 5 packet drops. The UDP client implements exponential backoff. The timeout will increase by 2 with each time that there is a packet dropped. When the timout value on the client gets to 2, the client prints:

```
DEAD SERVER!
```
And closes the datagram socket

In either client, if you want to quit, simply type "Q". MUST BE CAPITAL. To stop the server, send a SIGINT to the process by typing ^C (Control-C)

## Tests

I have tested this with all types of input ranging from numbers and valid operational codes, to invalid operational codes all within the ASCII ranges. All tests return proper behavior as descibed above.

## Contributors

John C Geenty III (March 20, 2017)

## License

Feel free to use my code. All I ask is that you leave me a comment so that I know you are using my code :).
