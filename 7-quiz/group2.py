import socket
import threading
import json

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
PORT = 9989
sock.connect( ("127.0.0.1", PORT) )

group = "ajt"

# Definisikan fungsi yang akan dieksekusi pada setiap thread

def handleThread(conn):
    try :
        while True :
            # To do : buat thred baru
            # Terima data dari client
            data = sock.recv(100)
            data = data.decode('ascii')
            dictJson = json.loads(data)
            if(dictJson["group"] == group):
                print(dictJson["pesan"])
    except (socket.error, KeyboardInterrupt) :
        conn.close()
        print("Client menutup koneksi")

while True :
    # Thread handling
    clientThread = threading.Thread(target=handleThread, args=(sock,))
    clientThread.start()
    # Kirim data ke server
    data = input("Masukkan string yang akan dikirim : ")
    data = {"group": group, "pesan": data}
    strJson = json.dumps(data)
    # data = "GROUP " + str(PORT) + ": " + data
    sock.send( strJson.encode('ascii') )