import socket

HOST = "localhost"
PORT = 5000

with socket.socket() as s:
    s.connect((HOST, PORT))
    print("Para finalizar conexión, escribir: DESCONEXION (En Mayúsculas)")
    while True:
        input_str = input("Ingresar mensaje para enviar a servidor:")
        s.sendall(input_str.encode())
        data = s.recv(1024)
        if data == b'Goodbye.':
            print("Conexion terminada.")
            break

        print(f"Servidor responde: {data.decode('utf-8')}")
