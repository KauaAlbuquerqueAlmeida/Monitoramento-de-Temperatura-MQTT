import serial
import socket
import time

HOST = 'localhost'
PORT = 1883
TOPIC = 'datacenter/temperatura'

# Altere para a porta correta (ex: COM3 no Windows, /dev/ttyUSB0 no Linux)
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("[ArduinoPublisher] Conectado à porta serial.")
    except Exception as e:
        print(f"[ERRO] Não foi possível abrir a porta serial: {e}")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[ArduinoPublisher] Conectado ao broker!")

        while True:
            try:
                linha = ser.readline().decode().strip()
                if linha and linha != "Erro":
                    temperatura = linha
                    mensagem = f"PUBLISH:{TOPIC}:Temperatura do servidor: {temperatura} °C\n"
                    s.sendall(mensagem.encode())
                    print(f"[ArduinoPublisher] Enviado: {mensagem.strip()}")
                    time.sleep(2)
            except Exception as e:
                print(f"[ERRO] Falha durante leitura/envio: {e}")

if __name__ == "__main__":
    main()

    