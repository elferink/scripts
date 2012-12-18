import socket
senddata= "\x38\x01\x00\x00\x00\x00\x00\x00\x00"

def checkserver(ip,port):
   print('Checking %s:%s' %(ip,port)) 
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.settimeout(5) # in seconds
   sock.connect((ip, port))
   print("Sending request...")
   sock.send(senddata)
   try:
      dta=sock.recv(100)
      print("Server reply: %s" %(dta))
   except:
      print("Server not responding")
   sock.close()

def main():
   checkserver("wodan.kicks-ass.org",1194)

if __name__ == "__main__":
   main()
