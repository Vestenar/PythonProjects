def cipher26(message):
    ans = message[0]
    for i in range(1, len(message)):
        s = sum([ord(j)-97 for j in ans]) % 26
        for n in range(2):
            x = 26 * n + (ord(message[i]) - 97) - s
            if 0 <= x <=25:
                break
        ans += chr(x+97)
    return ans


print(cipher26("taiaiaertkixquxjnfxxdh"))
print(cipher26("abdgkpvcktdoanbqgxpicxtqon"))

'''
You've intercepted an encrypted message, and you are really curious about its contents. 
You were able to find out that the message initially contained only lowercase English letters, 
and was encrypted with the following cipher:

    Let all letters from 'a' to 'z' correspond to the numbers from 0 to 25, respectively.
    The number corresponding to the ith letter of the encrypted message 
is then equal to the sum of numbers corresponding to the first i letters of the initial 
unencrypted message modulo 26.

Now that you know how the message was encrypted, implement the algorithm to decipher it.

Example

For message = "taiaiaertkixquxjnfxxdh", the output should be
cipher26(message) = "thisisencryptedmessage".

The initial message "thisisencryptedmessage" was encrypted as follows:

    letter 0: t -> 19 -> t;
    letter 1: th -> (19 + 7) % 26 -> 0 -> a;
    letter 2: thi -> (19 + 7 + 8) % 26 -> 8 -> i;
    etc.

'''
