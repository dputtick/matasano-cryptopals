import binascii
import base64
import itertools
import operator
import math

## Challenge 1
def challenge1():
    hexint = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
    hexstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    bhexstr = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    bytestr = binascii.unhexlify(bhexstr)
    b64string = base64.b64encode(bytestr)
    print(b64string)

## Challenge 2
def challenge2():
    firststr = '1c0111001f010100061a024b53535009181c'
    secstr = '686974207468652062756c6c277320657965'
    firstbytes = binascii.unhexlify(firststr)
    secbytes = binascii.unhexlify(secstr)
    xorbytes = bytearray(x ^ y for x, y in zip(firstbytes, secbytes))
    print(bytes(xorbytes).decode())

## Challenge 3
def bytes_scorer(string_of_bytes):
    probs = {b'a': .0855, b'b': .0160, b'c': .0316, b'd': .0387, b'e': .1210,
            b'f': .0218, b'g': .0209, b'h': .0496, b'i': .0733, b'j': .0022,
            b'k': .0081, b'l': .0421, b'm': .0253, b'n': .0717, b'o': .0747,
            b'p': .0207, b'q': .0010, b'r': .0633, b'r': .0633, b't': .0894,
            b'u': .0268, b'v': .0106, b'w': .0183, b'x': .0019, b'y': .0172,
            b'z': .0011, b' ': .15}
    target_string = string_of_bytes.lower()
    list_of_probs = [(target_string.count(letter) * probs[letter])
                        for letter in probs]
    return sum(list_of_probs)


def best_unxor_char(string_of_bytes):
    charlist = (num for num in bytes(range(256)))
    char_scores = []
    for char in charlist:
        xor_result = bytes(char ^ byte for byte in string_of_bytes)
        scored_value = bytes_scorer(xor_result)
        char_scores.append((scored_value, char, xor_result))
    return max(char_scores)


def challenge3():
    ch3str = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ch3bytes = binascii.unhexlify(ch3str)
    print(best_unxor_char(ch3bytes))

## Challenge 4
def challenge4():
    with open('4.txt', 'r') as file:
        best_overall = (0, 0, 0)
        best_line = None
        for line in file:
            line = line.strip('\n')
            line = binascii.unhexlify(line)
            best_match = best_unxor_char(line)
            if best_match[0] > best_overall[0]:
                best_overall = best_match
    print(best_overall)

## Challenge 5
def repeating_key_xor(encrypt_string, key):
    result = bytes(map(operator.xor, encrypt_string, itertools.cycle(key)))
    return result


def challenge5():
    encrypt_string = (b"Burning 'em, if you ain't quick and nimble\n"
                b"I go crazy when I hear a cymbal")
    key = b"ICE"
    result = repeating_key_xor(encrypt_string, key)
    print(binascii.hexlify(result))

## Challenge 6
def hamming_distance(string1, string2):
    result = bytes(map(operator.xor, string1, string2))
    return sum(bin(x).count("1") for x in result)


def determine_keysize(target):
    possible_keys = []
    for keysize in range(2, 41):
        target_split = [target[i:i+keysize] for i in range(0, keysize*4, keysize)]
        combinations = itertools.combinations(target_split, 2)
        distances = list(itertools.starmap(hamming_distance, combinations))
        normalized_avg = sum(distances) / len(distances) / keysize
        possible_keys.append((normalized_avg, keysize))
    print(sorted(possible_keys))
    return [keysize for (distance, keysize) in sorted(possible_keys)]


def challenge6():
    # validate hamming_distance()
    string1 = b"this is a test"
    string2 = b"wokka wokka!!!"
    print(hamming_distance(string1, string2))
    with open('6.txt', 'r+b') as file:
        target = file.read()
    target = base64.b64decode(target)
    ordered_keys = determine_keysize(target)
    likely_keysize = ordered_keys[0]
    divided_blocks = []
    for i in range(likely_keysize):
        divided_blocks.append(target[i::likely_keysize])
    potential_key_list = []
    for block in divided_blocks:
        potential_key_list.append(best_unxor_char(block)[1])
    potential_key = bytes(potential_key_list)
    result = repeating_key_xor(target, potential_key)
    print(potential_key.decode())
    print(result.decode())


if __name__ == '__main__':
    challenge6()
