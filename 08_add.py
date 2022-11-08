from py532lib.mifare import *
import time , binascii
card = Mifare()
card.SAMconfigure()
card.set_max_retries(MIFARE_SAFE_RETRIES)
uid = card.scan_field()
i = 0
if uid:
    ID = binascii.hexlify(uid)
    print('ID:',ID)
    for section in range(2):    #讀 section = 0 , 1 的區域
        for block in range(4):  #讀 block = 0 ~ 3 的位置
            address = card.mifare_address(section,block)
            data = card.mifare_read(address)
            print(i,':',bytes(data))
            i += 1              #讀取第幾次-1
        

