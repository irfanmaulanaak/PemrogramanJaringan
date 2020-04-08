#Irfan Maulana Akbar (175150207111036)

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("0.0.0.0", 9979) )
try:
    while True:
        #Kirim Data
        data = input("Masukkan String Yang Akan Dikirim: ")
        sock.send( data.encode('ascii') )
        print()
except KeyboardInterrupt:
    print("\nClient Mati")


