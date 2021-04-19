import whois
# domain = whois.query('45.178.109.143')
# print(domain.__dict__)
def verificarPorta(ip,port):
    if s.connect_ex((ip,port)):
        # print("Porta", port, "esta fechada")
        pass;
    else:
        print("Porta", port, "esta aberta")
        return;
import socket
ip = '45.178.109.143'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
verificarPorta(ip,80);
for port in range(0,30000):
    verificarPorta(ip,port);
    