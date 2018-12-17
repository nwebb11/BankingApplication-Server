import socket

class Client:
    def __init__(self, connection, address):
            self.connection = connection
            self.address = address

def main():
    server_ip = '127.0.0.1'
    port = 5005
    buffer = 1024
    Connect = True
    while Connect:
        listenClients(server_ip, port)
        
      
def listenClients(server_ip, port_num):
    try:
        socket_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_stream.bind((server_ip, port_num))
        socket_stream.listen(5)
        connection, address = socket_stream.accept()
        newClient = Client(connection, address)
        #message = newClient.connection.recv(1024)
        print("New client connected ", newClient.address)
        sendMessage(newClient, 'Server: Connected to server ')
        return newClient
    except:
        print(sys.exc_info()[0])

def sendMessage(client, message):
    message += str(client.address)
    client.connection.send(message.encode('ASCII'))
    print('Hello world')
    

main()
    
