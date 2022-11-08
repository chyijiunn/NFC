from py532lib.mifare import *
import time
card = Mifare()
card.SAMconfigure()
card.set_max_retries(MIFARE_SAFE_RETRIES)
uid = card.scan_field()
if uid:
    address = card.mifare_address(i,j)
    data = card.mifare_read(address)
    print(bytes(data))
        
