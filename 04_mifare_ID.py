from py532lib.mifare import *
import time
import binascii

'''                                             這邊跟下面是一樣的
while True:
    scanID = Mifare().scan_field()
    ID = binascii.hexlify(scanID)
    print('ID:',ID)
    time.sleep(1)
'''

while True:
    ID = binascii.hexlify(Mifare().scan_field())#只是兩行寫成一行而已
    print('ID:',ID)
    time.sleep(1)