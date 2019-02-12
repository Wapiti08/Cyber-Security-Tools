#this is an example for nmap’s TCP SYN
'''
This is the demonstration
PORT    STATE    SERVICE
22/tcp  open     ssh
113/tcp closed   auth
139/tcp filtered netbios-ssn

based on https://xael.org/pages/python-nmap-en.html
'''

'''
Run $ python 100889405-syn.py 
Please input the scan host and ports: 8.8.8.8 20-80
'''

import nmap
from socket import *
import sys

port_type='tcp'
#get the input from terminal 
scan_row=[]
input_data=input("Please input the scan host and ports:")

scan_row=input_data.split(' ')
if len(scan_row)!=2:
    print("Input error, example like '192.168.10.10 20-80'")
    sys.exit(0)

#extract the Host and Port from the input
tgtHost=scan_row[0]
tgtPort=scan_row[1]
    
#use namp library to scan 
def synScan(tgtHost,tgtPort):
    try:
        #build an example
        Scanner=nmap.PortScanner()
        #call the scan function
        #in fact, there is no need to set arguments, it is -sS by default
        Scanner.scan(hosts=tgtHost,ports=tgtPort,arguments='-sS')
    except Exception as e:
        print(e)
    finally:
        #everytime you need to close socket connect to avoid resource abuse
        for host in Scanner.all_hosts():
            print('----------------------------------------------------')
            # will show the hostname
            print('Host : %s (%s)' % (host, Scanner[host].hostname()))
            # will show up or down
            print('State : %s' % Scanner[host].state())
            for proto in Scanner[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                # output the state of Ports
                lport = Scanner[host][proto].keys()
                # lport.sort()
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, Scanner[host][proto][port]['state']))

synScan(str(tgtHost),tgtPort)


