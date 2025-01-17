import socket
import pickle
import threading
import time


def handle_client(client_socket, array):
    data = pickle.dumps(array)
    client_socket.send(data)

    name = pickle.loads(client_socket.recv(1024))
    data = client_socket.recv(1024)
    sorted_array = pickle.loads(data)
    output[name] = sorted_array
    print(output)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

# received array
main_client, client_address = server_socket.accept()
data = main_client.recv(1024)
array = pickle.loads(data)

output = {
    'bogo': None,
    'stalin': None,
    'bubble': None
}

for i in range(3):
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(target=handle_client, args=(client_socket, array))
    client_thread.start()

time.sleep(0.5)
main_client.send(pickle.dumps(output))
server_socket.close()
