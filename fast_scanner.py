import socket
import threading
import time

target = input("Enter target IP (127.0.0.1): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

start_time = time.time()

thread_limit = threading.Semaphore(50)
open_ports = []

def scan_port(port):
    with thread_limit:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            result = s.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

            s.close()
        except:
            pass

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print("\nScan completed!")
print(f"Open ports: {open_ports}")
print(f"Total open ports: {len(open_ports)}")
print(f"Scan duration: {end_time - start_time:.2f} seconds")
