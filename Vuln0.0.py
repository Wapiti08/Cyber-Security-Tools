import socket
def retBanner(ip,port):
    socket.setdefaulttimeout(2)
    s=socket.socket()
    try:
        s.connect((ip,port))
        con=s.recv(1024)
        return con
    except:
        return 

def checkVulns(con):
    if 'FreeFloat Ftp Server (Version 1.00)' in con:
        print('[+] FreeFloat FTP Server is vulnerable.')
    elif '3Com 3Daemon FTP Server Version 2.0' in con:
        print('[+] 3Com 3CDaemon FTP Server is vulerable.')
    elif 'Ability Server 2.34' in con:
        print('[+] Ability FTP Server is vulerable.')
    else:
        print('[-] FTP Server is not vulnerable.')
    return 

def main():
    ip1='192.168.43.128'
    ip2='192.168.43.198'
    port=22
    Banner1=retBanner(ip1,port)
    if Banner1:
        print('[+]'+ip1+':'+str(Banner1).strip('\n'))
        checkVulns(str(Banner1))
    Banner2=retBanner(ip2,port)
    if Banner2:
        print('[+]'+ip2+':'+str(Banner2).strip('\n'))
        checkVulns(str(Banner2))

if __name__=="__main__":
    main()
