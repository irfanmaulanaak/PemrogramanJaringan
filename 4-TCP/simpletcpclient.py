import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 9999) )

#Kirim Data
data = "Selamat Sore"
sock.send( data.encode('ascii') )

#Terima Balasan dari Server
data = sock.recv(100)
data = data.decode('ascii')
print(data)
print(data)