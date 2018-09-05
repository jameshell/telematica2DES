#Importamos la libreria de sockets y cifrado
import socket
import pyDes

def Main():
        #Definimos HOST y PORT
        #El ping es el del PC del SERVIDOR
        host = "172.30.10.181"
        port = 5000
#Creamos el SOCKET
        mySocket = socket.socket()
#Como este es un CLIENTE usamos el metodo CONNECT
        mySocket.connect((host, port))
#Accedemos al archivo que esta alojado en el sistema de carpetas
        with open('texto.txt', 'r') as archivo:
                message = archivo.read()

#Preparamos el mensaje a enviar (En este ejemplo ya no se usa porque tiene que ser un archivo)
       #message = input(" -> ")
#Creamos el argumento!!!!
        k = pyDes.des(b"DESCRYPT", pyDes.ECB, b"\0\0\0\0\0\0\0\0",
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
