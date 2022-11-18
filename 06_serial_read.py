from py532lib.mifare import *
import time , binascii
Mifare().SAMconfigure()
Mifare().set_max_retries(MIFARE_SAFE_RETRIES)
uid = Mifare().scan_field()
i = 0
if uid:
    ID = binascii.hexlify(uid)
    print('ID:',ID,':',uid)
    for section in range(3):    #讀 section = 0 , 1 的區域
        for block in range(4):  #讀 block = 0 ~ 3 的位置
            address = Mifare().mifare_address(section,block)
            data = Mifare().mifare_read(address)
            print(i,'(',section,',',block,'):',bytes(data))
            i += 1              #讀取第幾次-1
        

