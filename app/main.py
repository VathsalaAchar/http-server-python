import socket  # noqa: F401


def main():

    # create a TCP server listening on port 4221
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()  # wait for client
    status, header, resp = b"HTTP/1.1 200 OK", b"", b""
    http_resp = b"\r\n".join([status, header, resp])
    with conn:
        print(f"connecting from {addr}")
        conn.sendall(http_resp)


if __name__ == "__main__":
    main()
