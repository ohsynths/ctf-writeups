import struct, base64
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
data = (BASE / 'src' / 'myNetworkTraffic.pcap').read_bytes()

pos = 24
packets = []
while pos < len(data):
    ts_sec, ts_usec, incl_len, orig_len = struct.unpack('<IIII', data[pos:pos+16])
    pos += 16
    packet = data[pos:pos+incl_len]
    pos += incl_len
    ip_header_len = (packet[0] & 0x0F) * 4
    tcp_offset = ip_header_len
    tcp_header_len = ((packet[tcp_offset + 12] >> 4) & 0x0F) * 4
    tcp_payload = packet[tcp_offset + tcp_header_len:]
    if tcp_payload:
        packets.append((ts_sec + ts_usec/1e6, tcp_payload.decode()))

packets.sort(key=lambda x: x[0])

decoded = b''
for ts, b64 in packets:
    decoded += base64.b64decode(b64)

import re
flag = re.search(rb'picoCTF\{[^}]+\}', decoded)
if flag:
    print(flag.group().decode())
