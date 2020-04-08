import socket
import threading
import json

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
PORT = 9949
sock.connect( ("127.0.0.1", PORT) )

grup = input("Masukkan grup yang akan dituju: ")
data = {"group": grup, "pesan": ""}
strJson = json.dumps(data)
sock.send( strJson.encode('ascii') )

# Definisikan fungsi yang akan dieksekusi pada setiap thread

def handleThread(conn):
    try :
        while True :
            # To do : buat thred baru
            # Terima data dari client
            data = sock.recv(100)
            data = data.decode('ascii')
            dictJson = json.loads(data)
            if(dictJson["group"] == grup):
                print(dictJson["pesan"])    
    except (socket.error, KeyboardInterrupt) :
        conn.close()
        print("Client menutup koneksi")

while True :
    # Thread handling
    clientThread = threading.Thread(target=handleThread, args=(sock,))
    clientThread.start()
    #Daftar grup
    
    # sock.send( grup.encode('ascii') )
    # Kirim data ke server
    data = input("Masukkan string yang akan dikirim : ")
    data = {"group": grup, "pesan": data}
    strJson = json.dumps(data)
    sock.send( strJson.encode('ascii') )