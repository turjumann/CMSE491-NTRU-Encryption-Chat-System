import socket
import threading
import NTRU

class Client:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        while 1:
            try:
                host = input('Enter host name --> ')
                port = int(input('Enter port --> '))
                self.s.connect((host,port))
                
                break
            except:
                print("Couldn't connect to server")

        self.username = input('Enter username --> ')
        self.s.send(self.username.encode())
        
        message_handler = threading.Thread(target=self.handle_messages,args=())
        message_handler.start()

        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()

    def handle_messages(self):
        while 1:
            #print(self.s.recv(1204).decode()) #Use this method for unencrypted messages received!
            decmsg = self.s.recv(1204).decode()
            decryptedArr = NTRU.decryption(decmsg)
            decmsgz = ''.join(chr(i) for i in decryptedArr)
            print(decmsgz)

    def input_handler(self):
        while 1:
            #self.s.send((self.username+' - '+input()).encode()) #Use this method for unecrypted messages sent!
            Message = input()
            combinedMsg = (self.username+' - '+Message)
            msg = NTRU.msg2Split(combinedMsg)
            m2Ascii = NTRU.char2Ascii(msg)
            encryptedArr = NTRU.encryption(m2Ascii)
            encryptedArr = ''.join([str(n) for n in encryptedArr])
            self.s.send(encryptedArr.encode())

client = Client()
