import binascii
string = b'\x048\xd5r\xaeO\x80'
a = binascii.hexlify(string)

print(a)
