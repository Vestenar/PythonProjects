def stolenLunch(note):
    dic = dict(zip("0123456789abcdefghij","abcdefghij0123456789"))
    # print(dic)
    # print(list(dic.keys()))
    code = note.split(" ")
    decode = []
    print(code)
    for word in code:
        if any(s in word for s in list(dic.keys())):
            for i in range(len(word)):
                if word[i] in dic.keys():
                    word = word[:i] + str(dic[word[i]]) + word[i+1:]
        decode.append(word)
    print(decode)
    return " ".join(decode)


print("9ust gd93hd som4 r0n3om not4 9k735id 3sicd t70t you, 359cdi 3s5di l8ttl4 on4?, w8ll 019kdi sid    sk3ud cjn4v4r 64t!")

note = "just 63jd73 some random note jkhdf83 ds823 that you, dfj238 dsf38 little one?, will abjk38 s83    skdu3 29never get!"
print(stolenLunch(note))
print("9ust gd93hd som4 r0n3om not4 9k735id 3sicd t70t you, 359cdi 3s5di l8ttl4 on4?, w8ll 019kdi sid    sk3ud cjn4v4r 64t!")


'''
When you recently visited your little nephew, he told you a sad story: 
there's a bully at school who steals his lunch every day, and locks it away in his locker. 
He also leaves a note with a strange, coded message. 
Your nephew gave you one of the notes in hope that you can decipher it for him. 
And you did: it looks like all the digits in it are replaced with letters and vice versa. 
Digit 0 is replaced with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by 'j'.

The note is different every day, so you decide to write a function that 
will decipher it for your nephew on an ongoing basis.

Example

For note = "you'll n4v4r 6u4ss 8t: cdja", the output should be
stolenLunch(note) = "you'll never guess it: 2390".
'''
