import socket
import threading
import sys

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            print("Listening for clients")
            client, address = self.sock.accept()
            #client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        print("Client connected %s" % str(address))
        buffer = 1024
        while True:
            try:
                data = bytes(client.recv(buffer))
                if data:
                    message = "Client  %s  connected" % str(address)
                    self.readMessage(client, address, data)
                    self.sendMessage(client, message)
            except:
                print("Client %s disconnected" % str(address))
                client.close()
                print(sys.exc_info()[0])
                return False

    def readMessage(self, client, address, data):
        command = data.decode('ASCII')
        print(str(address) + " " + command)

    def sendMessage(self, client, data):
        client.send(data.encode('ASCII'))

if __name__ == "__main__":
    serverIP = 'localhost'
    port_num = 5005
    print("Server starting")
    ThreadedServer(serverIP,port_num).listen()
