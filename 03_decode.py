import binascii					#將字元編碼引入
string = b'\x048\xd5r\xaeO\x80'	#設定要解的 HEX
a = binascii.hexlify(string)	#轉為字串

print(a)
