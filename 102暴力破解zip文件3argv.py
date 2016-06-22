import zipfile
import optparse
from threading import Thread	##

# python pyfile.py  -d 101dictionary.txt -f 102evil.txt.zip

def extractFile(zFile,password):
	try:
		zFile.extractall(pwd=password)
		print '[+] Password = '+password+"\n"
	except:
		return
	
def main():
	parser=optparse.OptionParser("Usage %prog -f <zipfile> -d <dictionary>");
	parser.add_option('-f',dest='zname',type='string',help='specity zip file');
	parser.add_option('-d',dest='dname',type='string',help='specity dictionary file');
	(options,args)=parser.parse_args()
	if(options.zname==None)|(options.dname==None):
		print parser.usage
		exit(0)
	else:
		zname=options.zname
		dname=options.dname
	zFile=zipfile.ZipFile(zname)
	passFile=open(dname)
	for line in passFile.readlines():
		password=line.strip("\n")
		##Thread
		t=Thread(target=extractFile,args=(zFile,password))
		t.start()		
		
if __name__=="__main__":
	main()
