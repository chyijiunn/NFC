import binascii					#將字元編碼引入
string = b'\x048\xd5r\xaeO\x80'	#設定要解的 bytearray
a = binascii.hexlify(string)	#轉為字串

print(a)

string = [16,15,14,13,12,11,10,9,8,7] 		#設定為16 bits
code = bytearray(string)
print('4_16bit:',code)