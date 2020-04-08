#Irfan Maulana Akbar (175150207111036)


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 9979) )

#Kirim Data
data = " Pengirim ke Penerima"
sock.send( data.encode('ascii') )



