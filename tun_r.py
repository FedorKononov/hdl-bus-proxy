import socket

def tohexstr(s):
    return ''.join('%02x' % ord(c) for c in s)

bus_h = '10.4.1.255'
tunnel_h = '10.4.1.10'

bus_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bus_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bus_s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

tunnel=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tunnel.bind((tunnel_h,6001))

while True:
    msg_tun = tunnel.recvfrom(1024)
    print ('\x1b[0;30;43m' + 'Tun recv():' + '\x1b[0m ')+ tohexstr(msg_tun[0]), msg_tun[1]
    bus_s.sendto(msg_tun[0], (bus_h, 6000))