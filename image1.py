import urllib
import optparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from os.path import basename
from PIL import Image
from PIL.ExifTags import TAGS
def findImages(url):
    print("[+] Finding image on "+url)
    urlContent=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(urlContent,'lxml')
    imgTags=soup.findAll('img')
    return imgTags

def downloadImage(imgTag):
    try:
        print("[+] Dowloading image ...")
        imgSrc=imgTag['src']
        imgContent=urllib.request.urlopen(imgSrc).read()
        #imgFileName=urlparse(imgSrc).path.split('/')[-1:]
        imgFileName=basename(urlparse(imgSrc).path)
        imgFile=open(imgFileName,'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''

#set a new dict,TAGS will mutiplate the dict
def testForExif(imgFileName):
    try:
        exifData={}
        image=Image.open(imgFileName)
        info=image._getexif()
        if info:
            for (tag,value) in info.items():
                #get(tag,default=tag)
                decoded=TAGS.get(tag,tag)
                exifData[decoded]=value
            exifGPS=exifData['GPSInfo']
            if exifGPS:
                print('[*] '+imgFileName+'contains GPS MetaData')
    except:
        pass

def main():
    parser=optparse.OptionParser("usage %prog -U "+'<target url>')
    parser.add_option('-U',dest='tgtUrl',type='string',help='specify target url')
    (options,args)=parser.parse_args()
    tgtUrl=options.tgtUrl
    if tgtUrl==None:
        print(parser.usage)
        exit(0)
    else:
        #imgTags is a list
        imgTags=findImages(tgtUrl)
        for imgTag in imgTags:
            imgFileName=downloadImage(imgTag)
            testForExif(imgFileName)
        
if __name__=="__main__":
    main()

