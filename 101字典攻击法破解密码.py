import crypt

def testPass(cryptPass):
	salt=cryptPass[0:2]	#sub string [0,2) to get char from 0 to 1
	dictFile=open('101dictionary.txt','r')
	for word in dictFile.readlines():
		word=word.strip('\n')
		cryptWord=crypt.crypt(word,salt)	#
		if(cryptWord==cryptPass):
			print "[+] Found Password: "+word+"\n"
			return
	print "[-] Password Not Found.\n"
	return

def main():
	passFile=open('101passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user=line.split(':')[0]
			cryptPass=line.split(':')[1].strip(' ')
			print "[*] Cracking Password For: "+user
			testPass(cryptPass)

if __name__=="__main__":
	main()
			
