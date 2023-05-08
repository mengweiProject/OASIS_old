'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/18 17:36 
'''

import socket
import threading


class HandleData(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self) -> None:
        while True:
            recv_content = self.client_socket.recv(1024)
            if len(recv_content) != 0:
                print(recv_content)
                self.client_socket.send(recv_content)
            else:
                self.client_socket.close()
                break


class TCPServer(threading.Thread):
    def __init__(self, port):
        super().__init__()
        # 创建套接字
        self.server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_s.bind(('', port))
        self.server_s.listen(128)

    def run(self) -> None:
        while True:
            new_s, client_info = self.server_s.accept()
            print(client_info)

            handle_data_thread = HandleData(new_s)
            handle_data_thread.start()

    def __del__(self):
        self.server_s.close()


if __name__ == '__main__':
    tcp_server = TCPServer(7788)
    tcp_server.start()