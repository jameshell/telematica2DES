import pyDes
#Fuente del codigo: http://twhiteman.netfirms.com/des.html

# Los datos hay que pasarlos a bytes...
data ="Please encrypt my data"
data2bytes=data.encode('utf-8')

#.des(llave, modo, IV, padding, modo de PAD)
k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

d = k.encrypt(data2bytes)
print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))
assert k.decrypt(d) == data2bytes
