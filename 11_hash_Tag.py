from py532lib.mifare import *
import time
import binascii
import hashlib

hs = hashlib.md5(b'043bd572ae4f80')
hs_md5 = hs.hexdigest()

i=0
while True:
    ID = binascii.hexlify(Mifare().scan_field())
    hs_ori = hashlib.md5(ID)
    hs_ori_md5 = hs_ori.hexdigest()
    if hs_ori_md5 == hs_md5:
        #print(i,'ID:',hs_ori_md5)
        print('open')
    else:print('No!')
    time.sleep(1)
    i = i + 1