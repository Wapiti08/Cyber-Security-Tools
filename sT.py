# This is the nmap’s TCP connect() strategy program made by Python
''' 
This is the demonstration
PORT    STATE  SERVICE
22/tcp  open   ssh
25/tcp  closed smtp
53/tcp  open   domain
70/tcp  closed gopher
80/tcp  open   http
113/tcp closed auth
'''

from threading import *
import threading
from socket import *
import optparse

port_type='tcp'

#this part is used to scan multi ips
def connScan(tgtHost,tgtPort):
    try:
        #stream is used for TCP package,build a socket example
        sockdf=socket(AF_INET,SOCK_STREAM)
        Address=(tgtHost,tgtPort)
        sockdf.connect(Address)
        #send a message, 'b' means the bits
        sockdf.send(b'hello\r\n')
        #get the response, check whether the host is active.
        #100 limits the size of reveived message
        results=sockdf.recv(100)

        print("[+]%d/tcp open %s"%(tgtPort,getservbyport(tgtPort,port_type)))
        print('[+]'+str(results))

    except:
        print('[-]%d/tcp close'%tgtPort)
    finally:
        #everytime you need to close socket connect to avoid resource abuse
        sockdf.close()



#this part is used to scan single ip address
def portScan(tgtHost,tgtHosts):
    try:
        #get the IP address from hostname using gethostbyname()
        tgtIP=gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host"%tgtHost)
        #jump out of the process
        return 
    try:
        #get the hostname,alias list,ip address from host
        tgtName=gethostbyaddr(tgtIP)
        print('[+]Scan Results for:',tgtName[0])
    except:
        print('[+]Scan Results for:',tgtIP)
    #scan ports for a single host
    for tgtPort in tgtHosts:
        #threading will be used in order to run multi processes in the same time
        P=threading.Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        P.start()
        P.join()

def main():
    #in order to use the command line, call the optparse library
    #set the output formaiton, set a parse example
    parser=optparse.OptionParser("usage %prog -H <target host> -p <target port>")
    #set the parameter
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtPort',type="string",help='specify target port[s] separated by comma')
    #parses arguments through the parse_args() method,options are the set of response
    (options,args)=parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts=str(options.tgtPort).split(',')
    #check the results
    if(tgtHost==None)|(tgtPorts[0]==None):
        print('[-]You must sepcify a target host and port[s].')
        exit(0)
    portScan(tgtHost,tgtPorts)
    
if __name__=='__main__':
    main()


