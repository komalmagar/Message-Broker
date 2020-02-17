import socket
cs1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 8080

cs1.connect((host, port))                               

cnd=input("Do you want to send data Yes or No?")
if(cnd=="Yes"):
    mg="Client1"    
    cs1.send(mg.encode("ascii"))
    
    file = open("c2.txt", "r")
    mg2=file.read()    
    cs1.send(mg2.encode("ascii"))
elif(cnd=="No"):
    mg="Client2"
    cs1.send(mg.encode("ascii"))
    msg = cs1.recv(1024)    
    print(msg.decode())
    
cs1.close()

