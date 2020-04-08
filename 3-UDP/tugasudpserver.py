import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind( ("0.0.0.0", 9000) )

while True:

    data, client_addr = sock.recvfrom(65536)

    data = data.decode('ascii')

    data1 = data.split( )

    if data1[2] == "+":
        
        val = int(data1[0]) + int(data1[1])
    elif data1[2] == "-":
        val = int(data1[0]) - int(data1[1])
    elif data1[2] == "*":
        val = int(data1[0]) * int(data1[1])
    elif data1[2] == "/":
        val = int(data1[0]) / int(data1[1])

    data = str(val)

    sock.sendto(data.encode('ascii'), client_addr)

#tutup socket
sock.close()