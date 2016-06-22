import zipfile

zFile=zipfile.ZipFile("102evil.txt.zip")
passFile=open('101dictionary.txt')
for line in passFile.readlines():
	password=line.strip("\n")
	try:
		zFile.extractall(pwd=password)
		print '[+] Password = '+password+"\n"
		exit(0)
	except Exception,e:
		pass
