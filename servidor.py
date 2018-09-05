#Importamos la libreria de sockets y cifrado
import socket
import pyDes


def Main():
    #Definimos HOST y PORT
    # El ping es el de este PC
    host = "127.0.0.1"
    port = 5000
#Creamos el SOCKET
    mySocket = socket.socket()
#Como este es el SERVER hacemos usamos el metodo BIND
    mySocket.bind((host, port))
#Dejamos al SERVER esperando CONEXIONES
    mySocket.listen(1)
#Confirmamos la conexion que llegue
    conn, addr = mySocket.accept()
    print("Conexion hecha desde: " + str(addr))

#Creamos el argumento!!!!!
    k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0",
              pad=None, padmode=pyDes.PAD_PKCS5)

    while True:
            #Se guarda la info del CLIENTE y se DECODIFICA
            data = conn.recv(1024)
            #Se descifra el mensaje
            d = k.decrypt(data)
            if not data:
                    break
            print("Del cliente conectado: " + str(d))

            message = str(d).upper()
            print("(enviando): " + message)
            #Se reenvia la info en MAYUSCULAS
            conn.send(message.encode())
#se CIERRA la conexion
    conn.close()


if __name__ == '__main__':
    Main()
