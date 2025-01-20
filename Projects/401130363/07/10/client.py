# client.py
import socket

def game_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 12358))
    print(sock.recv(1024).decode())

    while True:
        response = sock.recv(1024).decode()
        if response.startswith("GAME_BOARD"):
            print(response[11:])
            player_move = input("Choose your position (0-8): ")
            sock.send(player_move.encode())
        elif "Game Over" in response or "No Winner" in response:
            print(response)
            break

    sock.close()

if __name__ == "__main__":
    game_client()
