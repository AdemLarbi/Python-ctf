from random import *
def premier(nombre):
	premier=True;
	i=2;
	while(i<(nombre-1) and i<(nombre/2)):
		if(nombre%i==0):
			premier=False;
		i=i+1;
	return premier;
def pgcd(a, b):
	while (b > 0):
		r = a%b
		a, b = b, r
	return a
def premier_entre (p, q):
	if pgcd(p,q)==1 :
		return True;
	else :
		return False;
def generer_n_p():
	a = random()
	while (premier(a)==False):
		a = random()
	return a

def generer_pq_premier(nom):
	p = generer_n_p()
	q = generer_n_p()
	while (premier_entre (p, q)==False) and (p*q!=nom):
		p = generer_n_p()
		q = generer_n_p()
	print "p = "+p
	print "q = "+q

nom=7515
generer_pq_premier(nom)
