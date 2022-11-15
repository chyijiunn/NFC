from py532lib.mifare import *
import time
import binascii
import hashlib

hs = hashlib.md5(b'ffffffffffffff')#這裡之後就會刪掉，不出示明文標籤
hs_md5 = hs.hexdigest()

i=0
while True:
    ID = binascii.hexlify(Mifare().scan_field())
    hs_ori = hashlib.md5(ID)# Tag上的 ID 雜湊後物件
    hs_ori_md5 = hs_ori.hexdigest()#雜湊值
    if hs_ori_md5 == hs_md5:#如果雜湊值相同
        #print(i,'ID:',hs_ori_md5)
        print('open')#可開啟
    else:print('No!')#否則不通過
    time.sleep(1)
    i = i + 1