import binascii
import base64
import itertools
import operator


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


def bytes_scorer(string_of_bytes):
    target = string_of_bytes
    spaces = target.count(b' ')
    e = target.count(b'e')
    t = target.count(b't')
    a = target.count(b'a')
    return spaces + e + t + a

def best_string(string_of_bytes):
    charlist = [num for num in bytes(range(128))]
    best = (0, 0, 0)
    for char in charlist:
        xor_result = bytes(char ^ byte for byte in string_of_bytes)
        scored_value = bytes_scorer(xor_result)
        if scored_value > best[0]:
            best = scored_value, xor_result, char
    return best


def challenge3():
    ch3str = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ch3bytes = binascii.unhexlify(ch3str)
    print(best_string(ch3bytes))


def challenge4():
    with open('4.txt', 'r') as file:
        best_overall = (0, 0, 0)
        for line in file:
            line = line.strip('\n')
            line = binascii.unhexlify(line)
            best_match = best_string(line)
            if best_match[0] > best_overall[0]:
                best_overall = best_match
    print(best_overall)


def repeating_key_xor(encrypt_string, key):
    encrypt_string = binascii.a2b_qp(encrypt_string)
    key = binascii.a2b_qp(key)
    result = bytes(map(operator.xor, encrypt_string, itertools.cycle(key)))
    print(binascii.hexlify(result))
        

def challenge5():
    encrypt_string = ("Burning 'em, if you ain't quick and nimble\n"
                "I go crazy when I hear a cymbal")
    key = "ICE"
    result = repeating_key_xor(encrypt_string, key)


if __name__ == '__main__':
    challenge5()
