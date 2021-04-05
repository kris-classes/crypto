"""
HTCS6702 Cryptography - Kris Pritchard / @krp

This file simulates netcat-like behaviour to help students understand how client-server connection works. You'll use this code for the assignment so make sure you understand how it all works.
"""
import fire
import socket


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to localhost on port 1234')
    s.connect(('localhost', 1234))  # Make sure the server is running before connecting.
    print('Connected! Type "exit" to exit.')

    while True:
        user_input = input('> ')
        if user_input == 'exit':
            print('Exiting!')
            exit()

        print(f'User typed: {user_input}')
        print(f'Converting to bytes and sending to server.')
        user_input_as_bytes = bytes(user_input.encode('ascii'))

        bytes_sent = s.send(user_input_as_bytes)

        server_reply = s.recv(100)
        print(f'Server replied: {server_reply}')



def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 1234))
    s.listen()
    print('Waiting for connections')
    client_socket, client_address = s.accept()
    print(f'Client connected from: {client_address}')

    while True:
        data = client_socket.recv(100)
        print(f'Received from client: {data}')
        print('Sending reply!')
        reply_msg = b'Reply from server: ' + data
        client_socket.send(reply_msg)
        

if __name__ == '__main__':
    fire.Fire(name='simple_netcat')
