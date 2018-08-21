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

def checkVulns(banner):
    f=open('vuln_banners.txt','r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('[+] Server is vulnerable:'+banner.strip('\n'))


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
