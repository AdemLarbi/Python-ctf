from netcat import Netcat
import socket
import sys


def encrypt(grammer ,msg ,key):
	crypted=""
	i=0
	for char in msg:
		if char in grammer:
			pos=(grammer.find(char)+grammer.find(key[i]))%len(grammer)
			crypted+=grammer[pos]

		else: crypted+=char
		i+=1

	print "\n ### Crypted Message ###"
	print crypted + "\n"
	return crypted
def decrypt(grammer ,msg ,key):
	decrypted=""
	i=0
	for char in msg:
		if char in grammer:
			
			
			pos=(grammer.find(char)-grammer.find(key[i]))%len(grammer)
			decrypted+=grammer[pos]

		else: decrypted+=char
		i+=1

	print "\n ### Decrypted Message ###"
	print decrypted + "\n"
	return decrypted

Grammmer="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}"
key=   "jxalalmecalmecalmecalmecalmevxcyu"
cipher="WfTSmCdlMSRRRAlQaitXo}qzlwsPZkiey"

print key
decrypt(Grammmer,cipher,key)
