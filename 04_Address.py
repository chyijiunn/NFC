from py532lib.mifare import *
import time
import binascii

while True:
    ID = binascii.hexlify(Mifare().scan_field())
    #adress = Mifare.mifare_address(0,1,1)
    data = Mifare.mifare_read(adress)
    print('ID:',ID)
    #print('address:',adress)
    #print(type(adress))
    print('data:',data)
    time.sleep(1)

