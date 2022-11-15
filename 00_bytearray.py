string = 'open the gate'		#設定字串為打開門
code = bytearray(string,'utf-8')#將之轉編碼 utf-8
print('1_str:',code)

string = 5		#設定為int
code = bytearray(string)
print('2_size:',code)

string = [1,2,3,4,5]			#設定為list
code = bytearray(string)
print('3_list:',code)
