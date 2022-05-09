import os

# for debug
P = r"C:\Program Files\iTunes\iTunes1.exe"
if not os.path.exists(P):
    # for production
    P = r"C:\Program Files\iTunes\iTunes.exe"

with open(P, 'rb') as f:
    data = f.read()

data = bytearray(data)

# Patch passwordSettings (actually useless)
data[0x77daf4:0x77daf4+5] = b'\xBF\x03\x00\x00\x00'
data[0x77db7e:0x77db7e+2] = b'\xEB\x0A'

# Patch signIn reason to serverDialog
data[0x7a9ed4:0x7a9ed4+6] = b'\xB9\x23\xFF\xFF\xFF\x90'

with open(P, 'wb') as f:
    f.write(data)