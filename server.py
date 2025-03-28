import socket

HOST = "localhost"
PORT = 5000

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        print("Esperando conexión...")
        connection, address = s.accept()
        with connection:
            print(f"Conectado: {address}")
            while True:
                data=connection.recv(1024)
                decoded_data = data.decode("utf-8")
                print(f"Cliente envía: {decoded_data}")
                print("----")

                if decoded_data == 'DESCONEXION':
                    connection.sendall(b'Goodbye.')
                    connection.close()
                    print(f"Conexión terminada con {address}")
                    break

                if not data:
                    connection.close()
                    break

                connection.sendall(data.upper())
