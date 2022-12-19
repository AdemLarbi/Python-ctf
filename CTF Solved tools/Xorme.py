import binascii 
crypted='.*82(?-0)#2?#%;,-,3%1;"(?://)>/ 86'

flag=""
for i in xrange(1,255):
	flag=""
	for c in crypted:
		cryptedhex=binascii.hexlify(c)
		flag+=chr(ord(c)^i)
	print(flag,"\n")
