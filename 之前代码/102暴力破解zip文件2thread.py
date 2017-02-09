import zipfile
from threading import Thread	##
def extractFile(zFile,password):
	try:
		zFile.extractall(pwd=password)
		print '[+] Password = '+password+"\n"
	except:
		return
	
def main():
	zFile=zipfile.ZipFile("102evil.txt.zip")
	passFile=open('101dictionary.txt')
	for line in passFile.readlines():
		password=line.strip("\n")
		
		##Thread
		t=Thread(target=extractFile,args=(zFile,password))
		t.start()		
		
if __name__=="__main__":
	main()
