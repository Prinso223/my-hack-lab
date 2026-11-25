import socket

target = input("Enter website to scan e.g google.com: ")
print(f"Scanning {target}...")

for port in [21, 22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")
    s.close()

print("Scan done!")
