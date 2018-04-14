import binascii
import socket
import time
import signal
import sys
import config
import Adafruit_PN532 as PN532

CS = 18
MOSI = 23
MISO = 24
SCLK = 25

#global IDnumber

CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
DELAY = 5
HEADER = b'BG'

def close(signal,frame):
    sys.exit()

signal.signal(signal.SIGINT,close)

pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

print('PN532 NFC RFID 13.56MHz Card Reader')
uid = 0
def scan():
    checked = True
    while checked:
        uid = pn532.read_passive_target()
        
        if uid is None:
            continue
        print('')
        print('Card UID 0x{0}'.format(binascii.hexlify(uid)))
        if not pn532.mifare_classic_authenticate_block(uid, 4, PN532.MIFARE_CMD_AUTH_B, CARD_KEY):
            print('Failed to authenticate with card!')
            continue
        data = pn532.mifare_classic_read_block(4)
        if data is None:
            print('Failed to read data from card!')
            continue
    # Check the header
        if data[0:2] !=  HEADER:
            print('Card is not written with proper block data!')
            continue
    # Parse out the block type and subtype
        print('User Id: {0}'.format(int(data[2:8].decode("utf-8"), 16)))
        IDnumber = '{0}'.format(int(data[2:8].decode("utf-8"), 16))
        
    # stops scanning
        checked = False
        print('Returning: ' + str(int(data[2:8].decode("utf-8"), 16)))
        return int(data[2:8].decode("utf-8"), 16)
        
def getUID(self, uid, value):
    self.value = uid
    return value
