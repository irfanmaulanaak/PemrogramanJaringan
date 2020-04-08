#Irfan Maulana Akbar (175150207111036)

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 8939) )

#Terima Balasan dari Server
data = sock.recv(100)
data = data.decode('ascii')
print(data)