#Importamos la libreria de sockets y cifrado
import socket
 
def Main():
#Definimos HOST y PORT
    host = "127.0.0.1"
    port = 5000
#Creamos el SOCKET
    mySocket = socket.socket()
#Como este es el SERVER hacemos usamos el metodo BIND
    mySocket.bind((host,port))
#Dejamos al SERVER esperando CONEXIONES
    mySocket.listen(1)
#Confirmamos la conexion que llegue
    conn, addr = mySocket.accept()
    print ("Conexion hecha desde: " + str(addr))
    while True:
            #Se guarda la info del CLIENTE y se DECODIFICA
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("Del cliente conectado: " + str(data))
             
            data = str(data).upper()
            print ("(enviando): " + str(data))
            #Se reenvia la info en MAYUSCULAS
            conn.send(data.encode())
#se CIERRA la conexion
    conn.close()
     
if __name__ == '__main__':
    Main()