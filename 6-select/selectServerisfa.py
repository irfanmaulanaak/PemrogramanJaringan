#import lib
import socket
import select

#socket tcp/ipv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binding
sock.bind(("",9998) )
#Listen
sock.listen(10)

#List yang berisi aktifitas input apa saja yangakan saya monitor
list_monitor =  [sock]
list_conn = []
#accept dan receive itu blocking
#select.select(list_monitor, [], [])

while 1:
    #I/O Check
    inready, outready, errready = select.select(list_monitor,[],[])
    #Iterate whole ready executing input activty
    for s in inready:
        #If Input activity related to socket -> recv() function
        if s == sock:
            #accept connection request
            conn, client_addr = s.accept()
            # add new connection to list (monitor conn)
            list_monitor.append(conn)
            list_conn.append(conn)
        #If input activity related to conection -> recv() function
        else:
            try:
                data = s.recv(100)
                data = data.decode('ascii')
                for s in list_conn:
                    data = "OK " + data
                    s.send(data.encode('ascii'))
            except socket.error :
                list_monitor.remove(s)
                print("Client memutuskan koneksi")
