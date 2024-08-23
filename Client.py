import socket
import threading
import easygui

# initaing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# make a connection
while True:
    global Conected
    try:
        # try having a connection
        ip = input("ip>")
        port = int(input("port>"))
        s.connect((ip, port))
        break
    except:
        # if doesnot connected
        print("enter the correct ip and port or the server maybe havent been online")

def recving_massage():
    while Conected:
        # always try to recvie a masage if conected and automicly change to str not bytes
        msg = s.recv(1048).decode("utf-8")
        print(msg)

def send_massage():
    global Conected
    # send a username
    username = input("username>")
    s.send(bytes(username,"utf-8"))

    while Conected:
        # Have a gui for input so it dont have an overlay for the output that use a print
        msg = easygui.enterbox()

        # make sure that they dont just close the window
        if msg != None:
            # checking for disconect
            if msg == 'q':
                # send disconect masage to go (to line 51 on server)
                s.send(bytes("DISCONECT","utf-8"))
                # end loop
                Conected = False

            # if not disconect send the masage
            else:
                msg = "["+username+"]" + msg
                s.send(bytes(msg,"utf-8"))

# control of conected
Conected = True

# starting recving and sending
# recving is a thread
thread = threading.Thread(target=recving_massage)
thread.start()
send_massage()
