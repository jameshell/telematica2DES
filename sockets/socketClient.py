#Importamos la libreria de sockets y cifrado
import socket

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
        while message != 'q':
                #Se CODIFICA la info
                mySocket.send(message.encode())
                #Se guarda la info del SERVER y se DECODIFICA
                data = mySocket.recv(1024).decode()

                print('Del servidor conectado: ' + data)
                #Se vuelve a pedir input
                message = input(" -> ")
#se CIERRA la conexion
        mySocket.close()


if __name__ == '__main__':
    Main()
