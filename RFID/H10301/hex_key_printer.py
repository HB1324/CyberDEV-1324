# Used to print Hex Keys for H10301 RFID Cards

for i in range(0x1A0000, 0x1A9999):
    print(f"{i:06X}")
