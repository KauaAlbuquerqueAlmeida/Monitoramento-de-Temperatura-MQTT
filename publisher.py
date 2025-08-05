# Kauã de Albuquerque Almeida
import socket
import time
import random

HOST = 'localhost'
PORT = 1883
TOPIC = 'datacenter/temperatura'

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[Publisher] Conectado ao broker!")

        while True:
            temperatura = round(random.uniform(30.0, 90.0), 2)
            mensagem = f"PUBLISH:{TOPIC}:Temperatura do servidor: {temperatura} °C\n"
            s.sendall(mensagem.encode())
            print(f"[Publisher] Enviado: {mensagem.strip()}")
            time.sleep(2)

if __name__ == "__main__":
    main()
