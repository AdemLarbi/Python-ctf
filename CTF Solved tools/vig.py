

def findkey(grammer ,plain ,cipher):
	key=""
	i=0
	for char in plain:
		if char in grammer:
			pos=(grammer.find(cipher[i])-grammer.find(char))%len(grammer)
			key+=grammer[pos]
		else:key+=char
		i+=1
	print "\n ### The key is ###"
	print key + "\n"
	return key

def encrypt(grammer ,cipher ,key):
	crypted=""
	i=0
	for char in cipher:
		if char in grammer:
			pos=(grammer.find(char)+grammer.find(key[i]))%len(grammer)
			crypted+=grammer[pos]
			i=(i+1)%len(key)
		else:
			crypted+=char
			i=(i+1)%len(key) #les espaces !! remove commnt

	print "\n ### Cipher text ###"
	print crypted + "\n"
	return crypted

def decrypt(grammer ,cipher ,key):
	decrypted=""
	i=0
	for char in cipher:
		if char in grammer:
			pos=(grammer.find(char)-grammer.find(key[i]))%len(grammer)
			decrypted+=grammer[pos]

		else: decrypted+=char
		i=(i+1)%len(key)

	print "\n ### Plain text ###"
	print decrypted + "\n"
	return decrypted



grammer="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ29	"
grammer="A1B2C3D4E5F6G7H8I9J0KLMNOPQRSTUVWXYZ"
#grammer="a1b2c3d4e5f6g7h8i9j0klmnopqrstuvwxyz"

cipher="IDDKDC5GK4CK2356M47D5IG5IE54DJJD"
plain=""
key="B"

encrypt(grammer ,cipher ,key)





