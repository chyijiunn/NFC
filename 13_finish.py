from py532lib.mifare import *
import time , binascii
import hashlib

card = Mifare()
i = 0

while True:
    uid = card.scan_field()
    if uid:
        ID = binascii.hexlify(uid)
        hs_ori = hashlib.md5(ID)
        hs_ori_md5 = hs_ori.hexdigest()
        
        if hs_ori_md5 == 'c8c108778b83980115c820f51fbd087d':
            print(i,':','open')
        else:print(i,':','No!')
        time.sleep(1)
        i = i + 1
