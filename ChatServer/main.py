import socket
import threading

HOST = '127.0.0.1'  # Standard loopback IP address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)
FORMAT = 'utf-8'  # Define the encoding format of messages from client-server
ADDR = (HOST, PORT)  # Creating a tuple of IP+PORT
Group_IDs = set()
Psw = dict()
GroupMem = dict()

def listenToMes(conn, groupID):
    while True:
        mes = conn.recv(1024)
        for i in range(len(GroupMem[groupID])):
            conn.send(mes)

def Handle_Client(conn, add):
    Opening_message = "Hello client, please choose an option:\n1. Connect to a group chat.\n2. Create a group chat.3. Exit the server."
    conn.send(Opening_message.encode(FORMAT))
    rec = conn.recv(1024).decode(FORMAT)

    try:
        groupID=0
        if rec == 1:
            conn.send("Enter your name:".encode(FORMAT))# Asking for client's name
            client_name = conn.recv(1024).decode(FORMAT)
            conn.send("Enter group ID:".encode(FORMAT))  # Asking for Group ID
            groupID = conn.recv(1024).decode(FORMAT)
            conn.send("Enter password:".encode(FORMAT))  # Asking for password
            psw = conn.recv(1024).decode(FORMAT)

            if groupID in Group_IDs and psw == Psw[groupID]:
                GroupMem[groupID].append(client_name, conn)
        elif rec == 2:
            conn.send("Enter your name:".encode(FORMAT))  # Asking for client's name
            client_name = conn.recv(1024).decode(FORMAT)
            conn.send("Enter password:".encode(FORMAT))  # Asking for password
            psw = conn.recv(1024).decode(FORMAT)
            groupID = len(Group_IDs)+1
            Group_IDs.add(groupID)
            Psw[groupID] = psw
            GroupMem[groupID] = [(client_name, conn)]
            conn.send(("Group ID generated: "+str(groupID)).encode(FORMAT))  # Asking for client's name
        elif rec == 3:
            conn.close()

        listenToMes(conn, groupID)

    except:
        pass


def start_server():
    server_socket.bind(ADDR)  # binding socket with specified IP+PORT tuple

    print(f"[LISTENING] server is listening on {HOST}")
    server_socket.listen()  # Server is open for connections

    while True:
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}\n")  # printing the amount of threads working

        connection, address = server_socket.accept()  # Waiting for client to connect to server (blocking call)
        thread = threading.Thread(target=Handle_Client, args=(connection, address))  # Creating new Thread object.
        # Passing the handle func and full address to thread constructor
        thread.start()  # Starting the new thread (<=> handling new client)


if __name__ == '__main__':
    IP = socket.gethostbyname(socket.gethostname())  # finding your current IP address
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Opening Server socket
    start_server()



