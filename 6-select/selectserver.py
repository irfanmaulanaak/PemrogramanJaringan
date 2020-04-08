#import library
import socket
import select

#socket tcp/ipv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binding socket
sock.bind( ("",9989) )
#Listen socket
sock.listen(10)

#jika ada koneksi maka fungsi accept akan ditrigger
#List yang berisi aktivitas input apa saja yang akan di monitor
list_monitor = [sock]

#send tidak blocking, yang blocking accept dan recv, jadi yang kita monitor 
#adalah object yang berhubungan sama fungsi accept dan recv
#dilakukan pengecekan IO berkali-kali/scr berulang maka ditambahkan looping
while True:
    #Cek aktifitas IO
    #dijadikan 3 variabel karena outputnya jadi satu, jadi harus dipisah
    inready, outready, errready = select.select(list_monitor, [], [])
    #Iterasi semua aktifitas input yang siap untuk dieksekusi
    for s in inready:
        #jika aktivitas input berhubungan dengan socket -> fungsi accept()
        if s == sock :
            #Terima permintaan koneksi
            conn, client_addr = s.accept()
            #Tambahkan koneksi baru ke list yang dimonitor
            #conn memiliki fungsi recv jadi perlu dimonitor dan dimasukkan ke list_monitor
            list_monitor.append(conn)
        #Jika aktifitas input berhubungan dengan koneksi -> fungsi recv()
        else:
            try:
                data = s.recv(100)
                data = data.decode('ascii')
                data = "OK " + data
                s.send(data.encode('ascii'))
            except socket.error :
                list_monitor.remove(s)
                print("Client memutuskan koneksi")
            