import socket

#Menginisialisasi objek socket
sock = socket.socket()

#Untuk menyambung dengan server
sock.connect((socket.gethostname(), 12344))
filename = input(str("Please enter the file name that you'd like to upload : "))
#Untuk membuka file
selectedFile = open(filename,'rb')
print('Mengirim...')
#Untuk membaca isi data dari file
fileToSend = selectedFile.read(1024)
while (fileToSend):
    print('Mengirim...')
    #Untuk mengirimkan data ke server
    sock.send(fileToSend)
    fileToSend = selectedFile.read(1024)
selectedFile.close()
print("Menunggu server menerima...")
#Ketika file sudah dikirim maka socket dimatikan
sock.shutdown(socket.SHUT_WR)
print("Pengiriman Berhasil")
sock.close                     # Close the socket when done