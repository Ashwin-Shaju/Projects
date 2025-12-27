import socket
import threading

target = input("Enter target IP: ")
ports = range(20, 1025)

def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        try:
            banner = s.recv(1024).decode().strip()
            print(f"[OPEN] Port {port} | Banner: {banner}")
        except:
            print(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

threads = []
for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
