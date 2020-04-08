#IRFAN MAULANA AKBAR(175150207111036)

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind (("0.0.0.0", 9998))


sock.listen(10)

#Fungsi yang akan dieksekusi pada setiap thread
def handle_thread(conn):
    try:
        #Baca Header
        headers = ""
        while True:
            #Rev data setiap 4 byte
            temp = conn.recv(4)
            temp = temp.decode('ascii')
            headers =  headers + temp
            if "\r\n\r\n" in headers :
                headers.replace("\r\n\r\n", "")
                break
        #Ceteak headers yang diterima
        print(headers)
        selectedFile = open("index.html", 'r')
        #kembalikan response ke client
        response = ("HTTP/1.1 200 OK\r\n"+
                    "Content-Type: text/html\r\n"+
                    "Content-Length: 1024\r\n"+
                    "Connection: close\r\n"+
                    "\r\n"+
                    selectedFile.read())
        print(response)
        conn.send(response.encode('ascii'))
    except (socket.error, KeyboardInterrupt):
        conn.close()
        print("Client Menutup Koneksi")

try:
    while True :
        #Terima Permintaan koneksi
        conn, client_addr = sock.accept()
        #Buat thread baru setiap ada permintaan koneksi dari client
        clientThread = threading.Thread(target=handle_thread, args=(conn,))
        clientThread.start()
except KeyboardInterrupt:
    print("\nServer Mati")
