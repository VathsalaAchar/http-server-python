import socket  # noqa: F401


def main():

    # create a TCP server listening on port 4221
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()  # wait for client


if __name__ == "__main__":
    main()
