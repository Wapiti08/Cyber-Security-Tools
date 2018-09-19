import sqlite3
import optparse
import os

def printProfile(skypeDB):
    conn=sqlite3.connect(skypeDB)
    c=conn.cursor()
    c.execute("SELECT fullname,skypename,city,country,datetime(profile_timestamp,'unixepoch') FROM Accounts;")
    for row in c:
        print(row)
        print("[*] -- Found Account --")
        print("[+] User:"+str(row[0]))
        print("[+] Skype Username:"+str(row[1]))
        print("[+] Location: "+str(row[2])+','+str(row[3]))
        print("[+] Profile Data: "+str(row[4]))
    
def printContracts(skypeDB):
    conn=sqlite3.connect(skypeDB)
    c=conn.cursor()
    c.execute("SELECT displayname,skypename,city,country,phone_mobile,birthday FROM Contacts;")
    for row in c:
        print("\n[*] -- Found Contracts --")
        print("[+] User: "+str(row[0]))
        print("[+] Skype Username: "+str(row[1]))
        #The None here is a string
        if str(row[2])!='' and str(row[3])!='None':
            print("[+] Location: "+str(row[2])+str(row[3]))
        if str(row[4])!='None':
            print("[+] Mobile Phone: "+str(row[4]))
        if str(row[5])!='None':
            print("[+] Birthday:"+str(row[5]))

def printCallLog(skypeDB):
    conn=sqlite3.connect(skypeDB)
    c=conn.cursor()
    c.execute("SELECT datatime(begin_timestamp,'unixepoch'),identity \
    FROM calls,conversations WHERE call.conv_dbib=conversations.id;")
    print("\n[*] -- Found Calls --")
    for row in c:
        print("[+] Times:"+str(row[0])+"[+] Partner:"+str(row[1]))

def printMessage(skypeDB):
    conn=sqlite3.connect(skypeDB)
    c=conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'),dialog_partner,author,body_xml FROM Messages")
    print("\n[*] -- Found Messages --")
    for row in c:
        try:
            if 'partlist' not in str(row[3]):
                if str(row[1])!=str(row[2]):
                    msgDirection='To: '+str(row[1])+": "
            else:
                msgDirection='From: '+str(row[2])+': '
            print("Time: "+str(row[0])+msgDirection+str(row[3]))
        except:
            pass
 
def main():
    parser=optparse.OptionParser("usage %prog -p"+'<skype profile path>')
    parser.add_option("-p",dest="pathName",type='string',help="Specify the pathName of skype path")
    (options,args)=parser.parse_args()
    pathName=options.pathName
    if os.path.isdir(pathName)==None:
        print(parser.usage)
        exit(0)
    elif os.path.isdir(pathName)==False:
        print("[!] Path is wrong."+pathName)
        exit(0)
    else:
        skypeDB=os.path.join(pathName,"main.db")
        if os.path.isfile(skypeDB):
            printProfile(skypeDB)
            printContracts(skypeDB)
            printCallLog(skypeDB)
            printMessage(skypeDB)
        else:
            print("[!] Skype Database"+"does not exist:"+skypeDB)

if __name__=="__main__":
    main()