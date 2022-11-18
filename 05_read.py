from py532lib.mifare import *
import time
Mifare().SAMconfigure()
Mifare().set_max_retries(MIFARE_SAFE_RETRIES)
uid = Mifare().scan_field()
if uid:                                     # 如果 uid 有掃到，回傳 True ，執行下面一次
    address = Mifare().mifare_address(1,2)  # (section,block)回傳 address
    data = Mifare().mifare_read(address)    # 讀取該 address 資料 
    print(bytes(data))
        
