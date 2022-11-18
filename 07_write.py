from py532lib.mifare import *
import time
Mifare().SAMconfigure()
Mifare().set_max_retries(MIFARE_SAFE_RETRIES)
uid = Mifare().scan_field()
if uid:
    address = Mifare().mifare_address(1,2)
    data = b'@@@@'
    data_write = Mifare().mifare_write_standard(address,data)