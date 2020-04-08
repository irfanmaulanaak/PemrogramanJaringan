import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind (("0.0.0.0", 9999))

sock.listen(10)

while True :
    #Terima Permintaan koneksi
    conn, client_addr = sock.accept()
    #Receive data
    data = conn.recv(100)
    data = data.decode('ascii')
    data = "OK" + data
    #Kirim balik
    conn.send(data.encode('ascii'))
    #Tutup Koneksi (Opsional)
    # conn.close()
