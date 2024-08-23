import socket
import threading

# initiating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),5454))
print(socket.gethostname(), 5454)

# list of all client socket
All_client =[]

# start funtion where it all start
def Connection():
    global All_client
    # listening for client
    s.listen(5)

    while True:
        # getting a client
        clientsocket, adrres = s.accept()

        # Adding Client Socket to list of socket client for brodcast
        All_client.append(clientsocket)
    
        # start the handel conection 
        # remember this is a thred not just calling a funtion
        thread = threading.Thread(target=handel_conection,args = [clientsocket])
        thread.start()

# run when get a conection
def handel_conection(clientsocket):
    # get username

    print("SOMEONE MAKE CONECTION")
    username = clientsocket.recv(1028).decode("utf-8")
    print(f"[SERVER]{username} is conected")

    # recving and brodcasting masage until disconect
    while True:

        # recving massage
        msg = clientsocket.recv(1028).decode('utf-8')

        #check for disconect
        if msg == "DISCONECT":
            # Send a massage to make them know that someone is this connect
            # make sure send so someone who disconected get the massage,so the recving thread could check if Conected is True (in line 24 in client)
            Brodcast("["+username+"]DISCONECTED")

            # remove client from all client list
            All_client.remove(clientsocket)

            # close conection
            clientsocket.close()

            # out of the loop
            break        
        else:
            # if not disconect
            Brodcast(msg)
    
    # handel_conection doesnot have a send because every send is automaticly brodcast

# brodcast function
def Brodcast(msg,byt = False):
    global All_client
    #send masage to all conected client
    for clientsocket in All_client:
        # if the masage is alredy in bytes
        if byt:
            clientsocket.send(msg)
        # if the masage is not in bytes
        else:
            clientsocket.send(bytes(msg,"utf-8"))
    # print the send massage on the server
    print(msg)

# start the program
Connection()
