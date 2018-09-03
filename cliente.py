#Importamos la libreria de sockets y cifrado
import socket
import pyDes

def Main():
        #Definimos HOST y PORT
        host = '127.0.0.1'
        port = 5000
#Creamos el SOCKET
        mySocket = socket.socket()
#Como este es un CLIENTE usamos el metodo CONNECT
        mySocket.connect((host, port))
#Preparamos el mensaje a enviar
        message = input(" -> ")
#Creamos el argumento
        k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0",
                    pad=None, padmode=pyDes.PAD_PKCS5)

        while message != 'q':
                #Los pasamos a bytes
                data2bytes = message.encode()
                #Los ciframos
                d = k.encrypt(data2bytes)
                print("Mensaje Cifrado: "+str(d))
                #Se CODIFICA la info
                mySocket.send(d)
                #Se guarda la info del SERVER y se DECODIFICA
                data = mySocket.recv(1024).decode()

                print('Del servidor conectado: ' + data)
                #Se vuelve a pedir input
                message = input(" -> ")
#se CIERRA la conexion
        mySocket.close()


if __name__ == '__main__':
    Main()
