'''
This is the advanced version that introduces the thread 
'''
import optparse
#the libirary above is used to analyse the 
#command at the terminal
import socket
from socket import *
from threading import *
#use the semaphore to control the printing process of program
screenLock=Semaphore(value=1)
#define the connection scan
def connScan(tgtHost,tgtPort):
    try:
        #change the ip into ipv4
        sockfd=socket(AF_INET,SOCK_STREAM)
        sockfd.settimeout(1)
        Address=(tgtHost,tgtPort)
        sockfd.connect(Address)
        # s.sendall(b'hello\r\n\r\n')
        # results = s.recv(100)
        sockfd.send(b'ViolentPython\r\n')
        # #set the timeout
        results=sockfd.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open'%tgtPort)
        print('[+]'+str(results))
        # print('[+]%s的%3s端口:打开' % (tgtHost,tgtPort)) #若可以建立连接，表示此端口是打开的
        
    except:
        screenLock.acquire()
        print('[-]%d/tcp closed',tgtPort)
    finally:
        screenLock.release()
        sockfd.close()

#get the ip and the list of port
def portScan(tgtHost,tgtPorts):
    try:
        #get the ip of the host
        tgtIP=gethostbyname(tgtHost)   
    except:
        print("[-] Cannot resolve '%s':Unknown host"%tgtHost)
        return
    try:
        #get the list of hostname,address,alien name
        tgtName=gethostbyaddr(tgtIP)
        
        print('\n[+] Scan Results for:'+tgtName[0])
    except:
        print('\n[+] Scan Results for:'+tgtIP)
    setdefaulttimeout(5)
    for tgtPort in tgtPorts:
        P=Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        P.start()
        P.join()

#the first step:create the list for IP,PORT,get from the host
def main():
    #create the paramatar analysis example
    #optparse.OptionParser([usage message])
    parser=optparse.OptionParser('usage %prog -H'+'<target host> -p <target port>')
    #hostname equals to the ip address
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    #port
    parser.add_option('-p',dest='tgtPort',type='string',help='specify target port[s] separated by comma')
    (options,args)=parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts=str(options.tgtPort).split(',')
    if(tgtHost==None)|(tgtPorts[0]==None):
        print('[-]You must specify a target host and port[s].')
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__=='__main__':
    main()

