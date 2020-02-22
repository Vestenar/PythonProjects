from urllib.request import urlopen

urlfile = urlopen(r'https://stepik.org/media/attachments/lesson/209717/1.html').read().decode('utf-8')
sfile = str(urlfile)
print(sfile.count("Python"))
print(sfile.count('C++'))