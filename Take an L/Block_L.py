from netcat import Netcat
import socket
import sys
#from sympy.solvers import solve
#from sympy import Symbol
from numpy import * 

import time
 
# Wait for 5 seconds

n=64 
m=64
matrix = [0] * n
for i in range(n): matrix[i] = [0] * m
nc = Netcat('misc.chal.csaw.io', 9000)
data=nc.socket.recv(4096)
print (data)
data=nc.socket.recv(2048)
print (data)
Block_data=(((((data.split(":"))[1]).replace(","," ")).replace("("," ")).replace(")"," ")).split(" ")
print (Block_data)
x=int(Block_data[2])
y=int(Block_data[4])
red=[x,y];
print (red)
matrix[red[0]][red[1]]=1
for i in matrix : print(i)
"""
nc.socket.sendall(X)

nc.socket.sendall("\n")

data=nc.socket.recv(2048)

print data

 """