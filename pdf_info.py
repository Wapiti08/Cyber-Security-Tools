import PyPDF2
import optparse
#to search the specific data
from PyPDF2 import PdfFileReader

def printMeta(filename):
    #the result is the tuple
    pdfFile=PdfFileReader(filename,'rb')
    docInfo=pdfFile.getDocumentInfo()
    print("[*] PDF MetaData For:"+str(filename))
    for metaItem in docInfo:
        print("[+] "+metaItem+":"+docInfo[metaItem])

def main():
    parser=optparse.OptionParser("usage %prog"+"-F <PDF file name>")
    parser.add_option("-F",dest="Filename",type="string",help="Specify the filename")
    (options,args)=parser.parse_args()
    filename=options.Filename
    if filename==None:
        print(parser.usage)
        exit(0)
    else:
        printMeta(filename)

if __name__=="__main__":
    main()
