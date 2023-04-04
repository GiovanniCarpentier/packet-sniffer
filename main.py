import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:
    packet = s.recvfrom(2048)

    ethernet_header = packet[0][0:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)

    dest_mac = binascii.hexlify(eth_header[0]).decode('utf-8')
    src_mac = binascii.hexlify(eth_header[1]).decode('utf-8')
    eth_type = binascii.hexlify(eth_header[2]).decode('utf-8')
    
    print(f"Destination MAC: {dest_mac}, Source MAC: {src_mac}, Type: {eth_type}")
