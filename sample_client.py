import socket

import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

print('Connecting to {}', format(server_address))

try:
    sock.connect(server_address)

except socket.error as err:
    print(err)
    sys.exit(1)

message = input('What is your message?\n')

try:
    sock.sendall(message.encode())

    try:
        while True:
            data = str(sock.recv(32))

            if data:
                print('Server response: ' + data)
            else:
                break
    except (TimeoutError):
        print('Socket timeout, ending listening for server messages')
    
finally:
    print('closing socket')
    sock.close()