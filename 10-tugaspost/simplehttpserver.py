#IRFAN MAULANA AKBAR(175150207111036)

import socket
import threading
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind (("0.0.0.0", 9969))

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

        #Mendapatkan panjang konten
        contlen = headers.partition("Content-Length: ")
        length_content = int(contlen[2].replace("\r\n\r\n", ""))
        #menerima pesan
        body = conn.recv(length_content)
        body = body.decode('ascii')
        reply = "OK " + body
        length_reply = str(len(reply))
        
        #kembalikan response ke client
        response = ("HTTP/1.1 200 OK\r\n"+
                    "Content-Type: text/html\r\n"+
                    "Content-Length:"+length_reply+"\r\n"+
                    "Connection: close\r\n"+
                    "\r\n"+
                    reply)
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
