'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/18 9:45 
'''

import socket
import threading


user_info_dict = {'127.0.0.1': 'Tom'}


def send_message(udp_socket):
    while 1:
        msg = input("\n要发送的内容：\n")
        dest_ip = '127.0.0.1'
        # dest_ip = input('\n对方的ip地址：')
        dest_port = 8081
        udp_socket.sendto(msg.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    while 1:
        recv_msg_info = udp_socket.recvfrom(1024)
        recv_ip_port = recv_msg_info[1]
        recv_msg_str = recv_msg_info[0].decode('utf-8')
        print(f'{user_info_dict.get(recv_ip_port[0], "somebody")} >>> {recv_msg_str}')


if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 7890))

    send_thread = threading.Thread(target=send_message, args=(udp_socket, ))
    recv_thread = threading.Thread(target=recv_msg, args=(udp_socket, ))

    send_thread.start()
    recv_thread.start()