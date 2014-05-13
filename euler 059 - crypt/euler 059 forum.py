cipher = eval('['+open(r"cipher1.txt").read()[:-1]+']')

def decrypt(cipher, key):      
    def iter_key():        
        nonlocal key
        key[:-1], key[-1] = key[1:], key[0]
        return key[-1]
    result = [chr(char ^ iter_key()) for char in cipher]
    return "".join(map(str, result))

def decrypt_message(cipher):
    for a in range(ord("a"), ord("z") + 1):
        for b in range(ord("a"), ord("z") + 1):
            for c in range(ord("a"), ord("z") + 1):
                text = decrypt(cipher, [a,b,c])
                if ' the ' in text:
                    return sum([ord(x) for x in text])

print (decrypt_message(cipher))
