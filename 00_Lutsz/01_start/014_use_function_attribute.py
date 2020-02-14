def saver(inpdata):
    saver.x.append(inpdata)
    print(saver.x)


saver.x = []

saver(10)
saver(20)
saver(30)