from py532lib.mifare import *
import time
card = Mifare()
card.SAMconfigure()
card.set_max_retries(MIFARE_SAFE_RETRIES)

uid = card.scan_field()
if uid:                                 # 如果 uid 有掃到，回傳 True ，執行下面一次
    address = card.mifare_address(i,j)  # i = 0 ~ 3 section ; j = 0 ~ 3 block，回傳 address
    data = card.mifare_read(address)    # 讀取該 address 資料 
    print(bytes(data))
        
