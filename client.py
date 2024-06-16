"""import socket

host = socket.gethostname()  # as both code is running on same pc
port = 5000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

while True:
    message = input("Enter the word -> ")
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    if data.lower().strip() == "won":
        print("congrats words of both players are matched.")
        client_socket.close()  # close the connection
        break
    else:
        print("words dosen't match. try again !")
        # w1 = client_socket.recv(1024).decode()
        # w2 = client_socket.recv(1024).decode()
        print("guess the word whose related with ", message)
        # message = input("Enter the word -> ")  # again take input
"""

import socket

HOST = socket.gethostname()  # Use uppercase for clarity
PORT = 5000  # Socket server port number

client_socket = socket.socket()  # Instantiate

try:
    # Connect to the server
    client_socket.connect((HOST, PORT))

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

            print("guess the word related to ", message, " and ", data)

except ConnectionError:
    print("Connection error occurred.")

finally:
    # Close the socket even on exceptions
    client_socket.close()

print("Client closed.")
