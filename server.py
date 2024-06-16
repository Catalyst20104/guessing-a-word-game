import socket

HOST = socket.gethostname()  # Use uppercase for clarity
PORT = 5000  # Choose a port number above 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)  # Listen for up to 2 connections

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        connection1, address1 = server_socket.accept()
        connection2, address2 = server_socket.accept()

        print(f"Connection from {address1} (Player 1)")
        print(f"Connection from {address2} (Player 2)")

        while True:
            try:
                player1_data = connection1.recv(
                    1024
                ).decode()  # Receive data from Player 1
                player2_data = connection2.recv(
                    1024
                ).decode()  # Receive data from Player 2

                if (
                    not player1_data or not player2_data
                ):  # Handle empty data or connection closure
                    print("One or both players disconnected.")
                    break

                player1_word = str(player1_data)
                player2_word = str(player2_data)

                print(f"Player 1: {player1_word}")
                print(f"Player 2: {player2_word}")

                player1_bytes = player1_word.encode()
                player2_bytes = player2_word.encode()
                if player1_word == player2_word:
                    connection1.sendall(b"won")  # Send "won" message in bytes
                    connection2.sendall(b"won")
                    connection1.close()
                    connection2.close()
                    server_socket.close()
                    break
                else:
                    print("Play again")
                    # Send both words back to clients (encoded):
                    connection1.sendall(player2_bytes)
                    connection2.sendall(player1_bytes)

            except ConnectionError:
                print("Connection error occurred.")
                break  # Exit the inner loop on connection error


finally:
    server_socket.close()  # Ensure socket is closed even on exceptions

print("Server closed")
