def caesar(text, key):
    import string
    letters = dict(enumerate(string.ascii_uppercase))
    text = ''.join(i.upper() for i in text if i.isalpha())
    crypted = ''.join([letters[(string.ascii_uppercase.index(i) + key) % 26] for i in text])
    print('Encrypted: ', crypted)
    print('Decrypted back: ', text)



text = "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet."
key = 42

(caesar(text, key))
