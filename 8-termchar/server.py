import socket

#Menginisialisasi socket
sock = socket.socket()

#Binding ke socket yang sudah ditentukan
sock.bind((socket.gethostname(), 12344))

#Untuk menerima koneksi yang datang
sock.listen(5)
while True:
    #Menerima koneksi dari cleint
    conn, addr = sock.accept()
    print('Got connection from', addr)
    print("Menerima...")
    #Untuk menerima file
    l = conn.recv(1024)
    filename = input(str("Please enter the file name that you'd like to upload : "))
    receivedFile = open(filename,'wb')
    while (l):
        print("Menerima...")
        #Untuk mengirim data file yang akan dikirimkan
        receivedFile.write(l)
        l = conn.recv(1024)
    receivedFile.close()
    print("File diterima dengan nama file", filename)
    conn.close()