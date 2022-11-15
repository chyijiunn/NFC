string = 'open the gate'				#設定字串為打開門
code = bytearray(string,'utf-8')		#將之轉編碼 utf-8
print('1_str:',code)

string = 5								#設定為int
code = bytearray(string)
print('2_size:',code)

string = [1,2,3,4,5]					#設定為list
code = bytearray(string)
print('3_list:',code)

string = [16,15,14,13,12,11,10,9,8,7] 	#設定為16 bits
code = bytearray(string)
print('4_16bit:',code)

#哪裏怪怪的？