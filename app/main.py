# Uncomment this to pass the first stage
import socket
import threading

def prepare_user_agent_body(msg):
    agent = msg.split(": ")[1]
    body_str = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(agent)}\r\n\r\n{agent}"
    print(body_str)

    return body_str.encode()

def prepare_echo_body(msg):
    body_str = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(msg)}\r\n\r\n{msg}"
    print(body_str)
    return body_str.encode()
   
def handle_data(conn):
    data = conn.recv(1024)
    data_str = data.decode()
    data_line = data_str.split("\r\n")
    method = data_line[0].split(" ")[0]
    path = data_line[0].split(" ")[1]

    print(data_line)
    if path == "/":
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    elif path.startswith("/echo"):
    
        body = prepare_echo_body(path.split("/echo/")[1])
        conn.sendall(body)
    elif path.startswith("/user-agent"):
        user_agent = data_line[2]
        # print(user_agent)
        body = prepare_user_agent_body(user_agent)

        conn.sendall(body)
    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

    conn.close()

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client

    # client is a connection
    while True:
        conn, addr = server_socket.accept()
        # handle_data(data, conn)
        client_thread = threading.Thread(
            target=handle_data,
            args=(conn,),
        )

        client_thread.start()

if __name__ == "__main__":
    main()
