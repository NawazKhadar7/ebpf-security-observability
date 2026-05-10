import socket,struct

def checksum(data):
    if len(data)%2:data+=b'\0'
    total=sum(struct.unpack('!'+str(len(data)//2)+'H',data));total=(total&65535)+(total>>16);total=(total&65535)+(total>>16);return ~total&65535
def build_ipv4(source='10.0.0.1',destination='10.0.0.2',protocol=17):
    transport=struct.pack('!HHHH',12000,8080,8,0) if protocol==17 else struct.pack('!HHIIBBHHH',12000,8080,0,0,0x50,2,8192,0,0)
    header=struct.pack('!BBHHHBBH4s4s',0x45,0,20+len(transport),1,0,64,protocol,0,socket.inet_aton(source),socket.inet_aton(destination));crc=checksum(header);header=header[:10]+struct.pack('!H',crc)+header[12:]
    return b'\x02\x00\x00\x00\x00\x02\x02\x00\x00\x00\x00\x01\x08\x00'+header+transport

def parse(packet):
    if len(packet)<14:raise ValueError('short Ethernet frame')
    if packet[12:14]!=b'\x08\x00':return {'ipv4':False}
    if len(packet)<34:raise ValueError('short IPv4 header')
    header=packet[14:];version=header[0]>>4;ihl=(header[0]&15)*4;length=int.from_bytes(header[2:4],'big')
    if version!=4 or ihl<20 or len(header)<ihl or length<ihl or len(header)<length:raise ValueError('invalid IPv4 bounds')
    return {'ipv4':True,'source':socket.inet_ntoa(header[12:16]),'destination':socket.inet_ntoa(header[16:20]),'protocol':header[9],'header_bytes':ihl,'packet_bytes':length}
