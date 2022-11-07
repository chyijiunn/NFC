from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
import binascii


pn532 = Pn532_i2c()
pn532.SAMconfigure()

while True:
    card_data = pn532.read_mifare().get_frame_type()
    #a = binascii.hexlify(card_data)
    #b = hex_to_ascii(a)
    print(card_data)
    sleep(1)