#Irfan Maulana Akbar (175150207111036)

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind (("", 9979))
socka.bind (("", 8939))

sock.listen(10)
socka.listen(10)

while True :
    #Terima Permintaan koneksi
    conn, client_addr = sock.accept()
    conna, client_addr = socka.accept()
    #Receive data
    data = conn.recv(1000)
    data = data.decode('ascii')
    data = "OK" + data
    #Kirim balik
    conna.send(data.encode('ascii'))
    #Tutup Koneksi (Opsional)
    conn.close()
    conna.close()
