from netcat import Netcat
import socket
import sys

"""

from netcat import Netcat

# start a new Netcat() instance
nc = Netcat('127.0.0.1', 53121)

# get to the prompt
nc.read_until('>')

# start a new note
nc.write('new' + '\n')
nc.read_until('>')

# set note 0 with the payload
nc.write('set' + '\n')
nc.read_until('id:')

"""

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
	nc = Netcat('crypto.chal.csaw.io', 8040)
	nc.write('                    ' + '\n')
	nc.read_until('Encrypting service')



nc = Netcat('crypto.chal.csaw.io', 8040)
  

msg=nc.socket.recv(2048)
print msg
for i in range(20):
	nc.socket.sendall('                    ' + "\n")
	data2 = nc.socket.recv(2048)
	print data2
		

