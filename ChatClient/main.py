import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000  # The port used by the server
FORMAT = 'utf-8'
ADDR = (HOST, PORT)  # Creating a tuple of IP+PORT

def start_client():
    client_socket.connect((HOST, PORT))  # Connecting to server's socket
    Opening_Message=client_socket.recv(1024).decode(FORMAT)
    print(Opening_Message)

    tosend=input()
    client_socket.send(tosend.encode(FORMAT))

    if tosend=='1':
        askName=client_socket.recv(1024).decode(FORMAT)
        print(askName)
        name = input()
        client_socket.send(name.encode(FORMAT))

        askID = client_socket.recv(1024).decode(FORMAT)
        print(askID)
        ID = input()
        client_socket.send(ID.encode(FORMAT))

        askpsw = client_socket.recv(1024).decode(FORMAT)
        print(askpsw)
        psw = input()
        client_socket.send(psw.encode(FORMAT))
    elif tosend=='2':
        askName = client_socket.recv(1024).decode(FORMAT)
        print(askName)
        name = input()
        client_socket.send(name.encode(FORMAT))

        askpsw = client_socket.recv(1024).decode(FORMAT)
        print(askpsw)
        psw = input()
        client_socket.send(psw.encode(FORMAT))

        ID=client_socket.recv(1024).decode(FORMAT)
    elif tosend==3:
        client_socket.close()

if __name__ == '__main__':
    IP = socket.gethostbyname(socket.gethostname())
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[CLIENT] Started running")
    start_client()
    print("\nGoodbye client:)")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
