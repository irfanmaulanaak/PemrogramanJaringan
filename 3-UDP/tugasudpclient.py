import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#kirim data ke server
server_addr = ("127.0.0.1", 9000)
data = input("Masukkan Angka dan operator = ")
sock.sendto(data.encode('ascii'), server_addr)

#terima balasan dari server
data = sock.recv(65536)
data = data.decode('ascii')

print(data)
sock.close()