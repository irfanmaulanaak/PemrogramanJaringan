#Irfan Maulana Akbar (175150207111036)

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind (("", 9979))

sock.listen(10)

#Fungsi yang akan dieksekusi pada setiap thread
#credit: https://stackoverflow.com/questions/27139240/i-need-the-server-to-send-messages-to-all-clients-python-sockets
# Pendekatan dengan menggunakan metode broadcast(mengirim data ke semua)
clients = set()
clients_lock = threading.Lock()
def handle_thread(conn):
    with clients_lock:
        clients.add(conn)
    try:
        while True:
            #Receive data
            data = conn.recv(100)
            data = data.decode('ascii')
            #Kirim balik ke client
            with clients_lock:
                for c in clients:
                    c.sendall(data.encode('ascii'))
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
