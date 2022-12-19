from netcat import Netcat
import socket
import sys
from sympy.solvers import solve
from sympy import Symbol



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
	
	nc.socket.sendall('50' + "\n")
	 
	data2 = nc.socket.recv(2048)
	print data2



nc = Netcat('misc.chal.csaw.io', 9002)
data=nc.socket.recv(2048)
print data


data=nc.socket.recv(2048)
print data

func=data.split(" ")
a=func[0]
b=func[2]
op=func[1]
res=float(func[4].split("\n")[0])
x=0
if op=="+":
	if a =="X":
		x=res-float(b)
	else: x=res-float(a)
if op=="-":
	if a =="X":
		x=res+float(b)
	else: x=res+float(a)
if op=="*":
	if a =="X":
		x=res/float(b)
	else: x=res/float(a)



print x
print str(x)
X=str(x)
nc.socket.sendall(X)
nc.socket.sendall("\n")
data=nc.socket.recv(2048)
print data
  




for i in range(5000):
	func=data.split("\n")
	xD=func[1].replace("=", "-")
	d = Symbol('X')
	X=solve(xD, d)
	print X
	end0=str(X[0]).split("/")
	if len(end0)>1 : end=float(end0[0])/float(end0[1])
	else : end=end0[0]
	nc.socket.sendall(str(end))
	nc.socket.sendall("\n")
	data=nc.socket.recv(2048)
	print data



	flag{y0u_s0_60od_aT_tH3_qU1cK_M4tH5}
