import socket
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="komal"
)

mycursor = mydb.cursor()


serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 8080                                          
serversocket.bind((host, port))                                  
serversocket.listen(5)
m=""
while True:
   clientsocket,addr = serversocket.accept()
   print("Got a connection from %s" % str(addr))
   if m=="":
      Dest=clientsocket.recv(1024).decode()            
      cMsg=clientsocket.recv(1024).decode()
      print("Dest:",Dest)
      print("Client msg:",cMsg)
      
      if(Dest=="Client1"):
         mycursor.execute("SELECT * FROM tblMsgFormats where vCompName ='Client1'")
         myresult = mycursor.fetchall()

         for x in myresult:
            print(x)
            if (x[2]=='colon'):
               cMsg=cMsg.replace(",",":")
            if (x[3]=='double'):
               cMsg=cMsg.replace(" ","  ")
            if (x[1]=='upper'):
               cMsg=cMsg.upper()


      elif(Dest=="Client2"):
         mycursor.execute("SELECT * FROM tblMsgFormats where vCompName ='Client2'")
         myresult = mycursor.fetchall()

         for x in myresult:
            print(x)
            
            if (x[2]=='comma'):
               cMsg=cMsg.replace(":",",")
            if (x[3]=='single'):
               cMsg=cMsg.replace("  "," ")
            if (x[1]=='lower'):
               cMsg=cMsg.lower()

         
      m=cMsg
      clientsocket.close()

   else:
      ds=clientsocket.recv(1024).decode()
      if(ds==Dest):
         print("msg sent to :",ds)
         clientsocket.send(m.encode("ascii"))
         break
      else:
         clientsocket.close()
         
   
