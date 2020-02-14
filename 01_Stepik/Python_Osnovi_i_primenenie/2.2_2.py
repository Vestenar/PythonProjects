from simplecrypt import decrypt
psws = []
with open(r"C:\adb\cript\encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open(r"C:\adb\cript\passwords.txt", "r") as psw:
    for line in psw:
        psws.append(line)
        try:
            print(decrypt(line.strip(), encrypted))
        except:
            print("no")