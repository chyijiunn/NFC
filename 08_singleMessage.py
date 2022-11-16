from py532lib.mifare import *
import time , binascii
#讀一個區域資料
uid = Mifare().scan_field()
i = 0
if uid:
    ID = binascii.hexlify(uid)
    print('ID:',ID)
    print(bytes(Mifare().mifare_read(Mifare().mifare_address(1,2))))