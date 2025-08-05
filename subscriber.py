# Kauã de Albuquerque Almeida
import socket
import threading

HOST = 'localhost'
PORT = 1883
TOPIC = 'datacenter/temperatura'

def receber_mensagens(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        mensagem = data.decode().strip()
        print(f"[Subscriber] Mensagem recebida: {mensagem}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[Subscriber] Conectado ao broker!")

        # Envia inscrição no tópico
        subscribe_msg = f"SUBSCRIBE:{TOPIC}\n"
        s.sendall(subscribe_msg.encode())
        print(f"[Subscriber] Inscrito no tópico '{TOPIC}'")

        # Thread para ouvir mensagens
        thread = threading.Thread(target=receber_mensagens, args=(s,))
        thread.start()

        thread.join()

if __name__ == "__main__":
    main()
