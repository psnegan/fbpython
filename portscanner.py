import socket

ports = [21,22,80,8080,443,445,3306,25]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex(("globo.com",port))
    if code==0:
        print(f"{port}\tport open")

    else:
        print(f"{port}\tport closed")