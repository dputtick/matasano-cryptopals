import binascii
import base64


def challenge1():
    hexint = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
    hexstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    bhexstr = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    bytestr = binascii.unhexlify(bhexstr)
    b64string = base64.b64encode(bytestr)
    print(b64string)


def challenge2():
    firststr = '1c0111001f010100061a024b53535009181c'
    secstr = '686974207468652062756c6c277320657965'
    firstbytes = binascii.unhexlify(firststr)
    secbytes = binascii.unhexlify(secstr)
    xorbytes = bytearray(x ^ y for x, y in zip(firstbytes, secbytes))
    print(bytes(xorbytes).decode())


def challenge3():
    ch3str = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ch3bytes = binascii.unhexlify(ch3str)
    charlist = [num for num in bytes(range(128))]
    un_xor_dict = {}
    for char in charlist:
        ch3result = bytes(char ^ byte for byte in ch3bytes)
        un_xor_dict[char] = ch3result
    ch3best = (0, 0, 0)
    for key, value in un_xor_dict.items():
        e = value.count(b'e')
        t = value.count(b't')
        a = value.count(b'a')
        space = value.count(b' ')
        comparer = sum([e, t, a, space])
        if comparer > ch3best[0]:
            ch3best = comparer, value, key
    print(ch3best[1:])

challenge3()
    
