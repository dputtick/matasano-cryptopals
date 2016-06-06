## Challenge 9
def challenge9():
    test = b"YELLOW SUBMARINE"
    print(pkcs7_pad(test, 16))


def pkcs7_pad(block, blocksize):
    block_length = len(block)
    padding_length = block_length % blocksize
    if padding_length == 0:
        padding_length = blocksize
    padding_string = bytes([padding_length] * padding_length)
    return block + padding_string


if __name__ == '__main__':
    challenge9()