# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client

    # client is a connection
    conn, addr = server_socket.accept()
    print(conn)
    # read data
   # data = conn.recv(1024)

    # build response string encoded as utf-8
    #response = "HTTP/1.1 200 OK\r\n\r\n".encode()
    
    #request now makes it a webserver 
    request = conn.recv(4096)
    request = request.decode().split("\r\n")
    http_method, path, http_version = request[0].split(" ")

    if path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n".encode()
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()

    # send response to client
    conn.send(response)

if __name__ == "__main__":
    main()
