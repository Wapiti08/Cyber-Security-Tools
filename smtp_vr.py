import socket
import sys

# check the length of parameters
if len(sys.argv) != 2:
    print("Usage: python3 vrfy.py <username>")
    sys.exit(0)

# create a socket and connect to the server
# choose stream data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# give ip and port for the connection
connect = s.connect(('xxx',25))

# receive the banner
# define the size of packet
banner=s.recv(1024)
print(banner)
print(sys.argv[1])
# verify a user and read the first after the script
s.send(('VRFY ' + sys.argv[1] + '\r\n').encode())
result = s.recv(1024)

# close the socket
print(result)
s.close()
