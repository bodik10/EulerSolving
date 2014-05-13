from string import ascii_lowercase

cipher = eval('['+open(r"cipher1.txt").read()[:-1]+']')

def decrypt(text, key, isEncrypt = False):
    if type(key) is str:    
        key = [ord(k) for k in key]     # 'abc' -> [97, 98, 99]
    if type(text) is str:
        text = [ord(k) for k in text]   # 'abc' -> [97, 98, 99]

    def iter_key():         # swaping key [10, 20, 34] -> [20, 34, 10], return 10
        nonlocal key
        key[:-1], key[-1] = key[1:], key[0]
        return key[-1]

    # if encrypt - return list with encrypted codes
    if isEncrypt:   
        result = [char ^ iter_key() for char in text]
        return result

    # if decrypt - return decrypted text
    result = [chr( char ^ iter_key() ) for char in text]
    return "".join(map(str, result))

def all_comb(seq, depth, prev=()):
    for char in tuple(seq):
        res = prev + (char,)
        if len(res) == depth:
            yield "".join(res)
        else:
            for res in all_comb(seq, depth, prev=res):
                yield "".join(res)

for key in all_comb(ascii_lowercase, 3):
    
    text = decrypt(cipher, key)
    
    if " the " in text:
        decrypted = text
        print ("Key is:", key)
        print (decrypted)
        print ("Sum of the ASCII values in the original text is:", sum([ord(x) for x in decrypted]))
        break
