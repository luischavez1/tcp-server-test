# tcp-server-test
Servidor y cliente TCP para ejecutar en local

# Instrucciones

Instrucciones para ejecutar y probar.

## Instrucciones para ejecutar servidor

En terminal, ubicarse en carpeta de proyecto y ejecutar el servidor:

```bash
python server.py
```
Aparecerá el siguiente mensaje:
```bash
Esperando conexión...
```

## Instrucciones para ejecutar cliente

Mientras el servidor está corriendo, en otra ventana de terminal, ubicarse en carpeta de proyecto y ejecutar el cliente:

```bash
python client.py
```
Aparecerá el siguiente mensaje:
```bash
Para finalizar conexión, escribir: DESCONEXION (En Mayúsculas)
Ingresar mensaje para enviar a servidor:
```
Una vez que ambos procesos estén corriendo, aparecerá el siguiente mensaje en la ventana de servidor:

```bash
Conectado: ('127.0.0.1', 40990)
```

## Uso
En ventana cliente, ingresar un mensaje para envíar a servidor:

```bash
Ingresar mensaje para enviar a servidor: hola
Servidor responde:  HOLA

```
En caso de querer terminar la conexión, escribir en mayúsculas: DESCONEXION
```bash
Ingresar mensaje para enviar a servidor:DESCONEXION
Conexion terminada.
```
