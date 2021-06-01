#!usr/bin/python
import socket

"""This is a simple port scanner, where you make a input of a hostname www.example.com and then 
the port you want to analyze and see if it's open."""

#Target host, www.example.com
t_host = str(input("Enter the host to be scanned: "))
#Resolve t_host ipv4 address
t_ip = socket.gethostbyname(t_host)
#Print the ipv4 address
print(t_ip)

while 1:
    #Enter the port to be scanned
    t_port = int(input("Enter the port: "))
    try:
        sock = socket.socket()
        res = sock.connect((t_ip, t_port))
        print("port {} is open: ".format(t_port))

        sock.close()
    except:
        print("Port {} is closed: ".format(t_port))
print("Port scanning complete")
