import binascii
import base64

# challenge 1
hexint = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
hexstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
bhexstr = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
bytestr = binascii.unhexlify(hexstr)
blight = binascii.unhexlify(bhexstr)
print(bytestr == blight)
b64string = base64.b64encode(bytestr)

# challenge 2
firststr = '1c0111001f010100061a024b53535009181c'
secstr = '686974207468652062756c6c277320657965'
firstbytes = binascii.unhexlify(firststr)
secbytes = binascii.unhexlify(secstr)
xorbytes = bytearray(x ^ y for x, y in zip(firstbytes, secbytes))
