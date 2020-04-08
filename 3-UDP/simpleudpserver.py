import socket

#inisiasi socket UDP/IPV4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind server agar bisa menerima semua data dengan menggunakan ip 0.0.0.0 atau dikosongin ("")
sock.bind( ("0.0.0.0", 9000) )

#terima data dari client
#recv return value cuma 1 (data)
#recvfrom return value ada 2 (data dan address) dipakai UDP
while True:

    data, client_addr = sock.recvfrom(65536)

    #konversi array of bytes jadi string
    data = data.decode('ascii')
    #tambah "OK" di depan data
    data = "OK " + data

    #Kirim balik ke client
    sock.sendto(data.encode('ascii'), client_addr)

#tutup socket
sock.close()