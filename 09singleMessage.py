from py532lib.mifare import *
import time , binascii
card = Mifare()
#card.SAMconfigure()
#card.set_max_retries(MIFARE_SAFE_RETRIES)
uid = card.scan_field()
i = 0
if uid:
    ID = binascii.hexlify(uid)
    print('ID:',ID)
    print(bytes(card.mifare_read(card.mifare_address(1,2))))