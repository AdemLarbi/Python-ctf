from netcat import Netcat
import socket
import sys


def encrypt(grammer ,msg ,key):
	crypted=""
	for char in msg:
		if char in grammer:
			pos=(grammer.find(char)+key)%len(grammer)
			crypted+=grammer[pos]

		else: crypted+=char

	print "\n ### Crypted Message ###"
	print crypted + "\n"
	return crypted
def decrypt(grammer ,msg ,key):
	decrypted=""
	for char in msg:
		if char in grammer:
			pos=(grammer.find(char)-key)%len(grammer)
			decrypted+=grammer[pos]

		else: decrypted+=char

	print "\n ### Decrypted Message ###"
	print decrypted + "\n"
	return decrypted
def send():
	#input = raw_input("CMD> ")
	nc.socket.sendall('a' + "\n")
	 
	data2 = nc.socket.recv(2048)
	print data2

	i=0
	j=0
	l=8
	for ist in data2.split(" "):
	 	if i==5:
	 		msg2=ist
		if i==(l-2):
		 	if len(data2.split(" "))>=l:
		 		l+=1
		 		msg2+=" "+ist
		i+=1
	print msg2+ "                 ==> the decrypted Message"
	Message=msg2
	for ist in data2.split(" "):
	 if j==3:
	  		  
	  print ist[0]+"                            ==> the Back indice "
	  back=ist[0]

	  j+=1
	 else: 
	  j+=1


	test='a'
	key2=(Grammmer.find(back)-Grammmer.find(test))%len(Grammmer)

	print key2

	nc.socket.sendall(decrypt(Grammmer,Message,key2))
	nc.socket.sendall("\n")
	data2 = nc.socket.recv(2048)
	print data2


Grammmer=" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


nc = Netcat('web.angstromctf.com', 1350)


msg=nc.socket.recv(2048)
print msg

	

