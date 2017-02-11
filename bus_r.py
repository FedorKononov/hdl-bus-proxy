import socket

def tohexstr(s):
    return ''.join('%02x' % ord(c) for c in s)

bus_h = '10.4.1.255'
tunnel_h = '192.168.10.106'

bus = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bus.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bus.bind((bus_h,6000))

tunnel=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg_bus = bus.recvfrom(1024)
    print ('\x1b[6;30;42m' + 'Bus recv():' + '\x1b[0m ')+ tohexstr(msg_bus[0]), msg_bus[1]
    tunnel.sendto(msg_bus[0], (tunnel_h, 6002))
