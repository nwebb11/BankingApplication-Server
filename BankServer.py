import socket
import threading
import sys

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = '127.0.0.1'
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            #client.settimeout(60)
            print("New client connected")
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        buffer = 1024
        while True:
            try:
                message = "hello"
                #print(address)
                client.send(message.encode('ASCII'))
                #data = bytes(client.recv(buffer))
                #if data:
                    #print(data + '%s'%data.decode('ASCII'))
                    #break
                #else:
                    #print(sys.exc_info()[0])
                    #raise error('Client disconnected')
                client.close()
            except:
                client.close()
                return False

if __name__ == "__main__":
    serverIP = '127.0.0.1'
    port_num = 5005
    ThreadedServer(serverIP,port_num).listen()
