import socket

HOST = socket.gethostname()  # Use uppercase for clarity
PORT = 500  # Socket server port number

client_socket = socket.socket()  # Instantiate


def main():
    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print("waiting for another player!")
        msg = client_socket.recv(1024).decode()
        print("Game has been started:")
        if msg == "start the game":
            while True:
                # Get user input
                message = input("Enter a word: ")

                # Send message to server (encoded)
                client_socket.sendall(message.encode())

                # Receive response from server (decoded)
                data = client_socket.recv(1024).decode()

                # word2 = client_socket.recv(1024).decode()
                if data.lower().strip() == "won":
                    print("Congratulations! Words matched.")
                    break
                else:
                    print("Words don't match. Try again!")
                    print("guess the word related to ", data, " and ", message)

                # print(data)

    except ConnectionError:
        print("Connection error occurred.")

    finally:
        # Close the socket even on exceptions
        # print("error")
        client_socket.close()

    print("Client closed.")


main()
