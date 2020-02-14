import re
import zipfile
inf = ""
out = []
n = "90052"
zip = zipfile.ZipFile("channel.zip", "r")

while True:
    try:
        file = n + ".txt"
        msg = str(zip.read(file))
        n = re.findall("\d+", msg)[0]
        a = str(zip.getinfo(file).comment)[2:-1]
        if a != "\\n":
            inf += a
        else:
            out.append(inf)
            inf = ""

    except:
        break

for i in out:
    print(i)