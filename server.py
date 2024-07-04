import socket
import threading

HOST = socket.gethostname()  # Use uppercase for clarity
PORT = 500  # Choose a port number above 1024
print(HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsconn = []
clientsadd = []
server_socket.bind((HOST, PORT))
server_socket.listen(500)  # Listen for up to 500 connections


def playg():
    connection1 = clientsconn.pop()  # poping  connection in list
    address1 = clientsadd.pop()  # poping address of clients in list
    connection2 = clientsconn.pop()  # poping  connection in list
    address2 = clientsadd.pop()  # poping address of clients in list
    print(f"Connection from {address1} (Player 1)")
    print(f"Connection from {address2} (Player 2)")
    connection1.sendall(b"start the game")
    connection2.sendall(b"start the game")
    while True:
        try:
            player1_data = connection1.recv(1024).decode()  # Receive data from Player 1
            player2_data = connection2.recv(1024).decode()  # Receive data from Player 2

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
            if player1_word == player2_word:  # checking whether word are equal or not
                connection1.sendall(b"won")  # Send "won" message in bytes
                connection2.sendall(b"won")
                connection1.close()
                connection2.close()
                # server_socket.close()
                break
            else:
                print("Play again")
                # Send both words back to clients (encoded):
                connection1.sendall(player2_bytes)
                connection2.sendall(player1_bytes)

        except ConnectionError:
            print("Connection error occurred.")
            break  # Exit the inner loop on connection error


def jointclients():  # accepting the clients
    while True:
        connection, address = server_socket.accept()
        clientsconn.append(connection)  # inserting connection in list
        clientsadd.append(address)  # inserting address of clients in list


def main():
    try:
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            if len(clientsadd) == 0 and len(clientsconn) == 0:
                continue
            if (
                len(clientsadd) >= 2 and len(clientsconn) >= 2
            ):  # checking for 2 players availability
                t1 = threading.Thread(target=playg)  # thread of playg function
                t2 = threading.Thread(target=main)  # thread of main function
                t2.start()
                t1.start()
                t1.join()
                t2.join()

    finally:
        server_socket.close()  # server is closing
        print("Server closed")


def game():
    main()


t4 = threading.Thread(target=game)  # thread of game function
t3 = threading.Thread(target=jointclients)  # thread of jointclients function

t3.start()
t4.start()
t3.join()
t4.join()
