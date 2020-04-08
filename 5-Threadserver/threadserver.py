import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind (("0.0.0.0", 9999))

sock.listen(10)

#Fungsi yang akan dieksekusi pada setiap thread
def handle_thread(conn):
    try:
        while True:
            #Receive data
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK " + data
            #Kirim balik ke client
            conn.send(data.encode('ascii'))
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
