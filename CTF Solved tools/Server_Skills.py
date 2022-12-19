#!/usr/bin/env python
 
import SocketServer
import time
import threading
from random import randint

 
class Service(SocketServer.BaseRequestHandler):


    def handle(self ):
    	done=0
    	grammer="abcdefghijklmnopqrstuvwxyz!?FPXYCDGUVWLMNEJKBHQAOZIRST" # khalota te3 Grammer !
    	keys=["C",'D',"j","F","g","K","I","Q","l","m","d","f","g","h","Z","l","!"]
    	hint=["HeyYouThere","ThereIsNoSpoon","TryHard",'JustDontTry',"TryAgain","MortalityIsGift","youWantplayToo?","ByMyWill","EverybodyDie","TimeToTroll","MagicTrick","WinterIsHere","Knock!WhosThere"]
    	flag="WTH{SKILLS_MUST_BE_TESTED!}"
    	##########################################################################
        rand=randint(1,1000)
        key=keys[rand%len(keys)]
        fordecrypt=self.encrypt(grammer,hint[rand%len(hint)],key)
        
        ##########################################################################
        print "Someone Connected "
        self.send("Welcome to WTH ! \nmax char is 15 xD ", newline = False )
        entered=self.receive()
        crypted=self.encrypt(grammer,entered,key)
        self.send("The encrypted of "+entered+" is "+crypted+"\n"+
        	      "decrypt > "+fordecrypt)
        entered=self.receive()
        ##########################################################################
        if entered!=self.decrypt(grammer,fordecrypt,key):self.send("Really !? \n")
        else:
        	
        	for x in xrange(2,51):
        		rand=randint(1,1000)
        		key=keys[rand%len(keys)]
        		fordecrypt=self.encrypt(grammer,hint[rand%len(hint)],key)
        		##########################################################################
        		self.send(" Another One ..."+str(x)+"...:D")
        		entered=self.receive()
        		crypted=self.encrypt(grammer,entered,key)
        		self.send("The encrypted of "+entered+" is "+crypted+"\n"+
        	      "decrypt > "+fordecrypt)
        		start = time.time()
        		entered=self.receive()
        		end = time.time()
        		if (end - start)>3:
        			self.send(" Too Slow  :3 ")
        			self.end()
        		##########################################################################
        		if entered!=self.decrypt(grammer,fordecrypt,key):
        			self.send(" >< So Wrong ! ")
        			self.end()
        		if (x==49):done=1

        if (done==1):self.send("There is the flag : "+self.encrypt(grammer,flag,key)+"\nNot Again xD")

       
 
    def send( self, string, newline = True ):
        if newline: string = string + "\n"
        self.request.sendall(string) 

    def receive( self, prompt = "\n > " ):
        self.send( prompt, newline = False )
        rang=self.request.recv( 4096 ).strip()
        if len(rang)<16 and len(rang)>0:return rang
        else: 
        	self.send("You Are Out Of Rang >< ! \n### BUSTED ! ###")
        	self.end()

    def encrypt(self,grammer ,cipher ,key):
    	crypted=""
    	i=0
    	for char in cipher:
			if char in grammer:
				pos=(grammer.find(char)+grammer.find(key[i]))%len(grammer)
				crypted+=grammer[pos]
				i=(i+1)%len(key)
			else:
				crypted+=char
				i=(i+1)%len(key) #les espaces !!
        return crypted



    def decrypt(self,grammer ,cipher ,key):
        decrypted=""
        i=0
        for char in cipher:
        	if char in grammer:
        		pos=(grammer.find(char)-grammer.find(key[i]))%len(grammer)
        		decrypted+=grammer[pos]
        		i=(i+1)%len(key)
        	else:
				decrypted+=char
				i=(i+1)%len(key)
        return decrypted

 
class ThreadedService( SocketServer.ThreadingMixIn, SocketServer.TCPServer, SocketServer.DatagramRequestHandler ):
    pass
 
def main():
 
    port = 9999       
    host = '127.0.0.1' 
 
    service = Service 
   
  
    server = ThreadedService( ( host, port ), service )
    server.allow_reuse_address = True
 
    server_thread = threading.Thread( target = server.serve_forever )
 
    server_thread.daemon = True
    server_thread.start()
 
    print "Server started on port", port
 

    while ( True ): time.sleep(60)
 
 
if ( __name__ == "__main__" ):
    main()































    												                                         ##### Challenge Author : AdamLarbi