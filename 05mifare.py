from py532lib.mifare import *
import time
import binascii
while True:
    ID = binascii.hexlify(Mifare().scan_field())
    print('ID:',ID)
    time.sleep(1)