def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 0
    height = 0
    while height <= desiredHeight:
        height += upSpeed
        days += 1
        if height >= desiredHeight:
            break
        height -= downSpeed

    return days

'''#решение bandorthild (формула)
def growingPlant(upSpeed, downSpeed, desiredHeight):
    return 1 if desiredHeight<=upSpeed else (desiredHeight-upSpeed-1)//(upSpeed-downSpeed)+2'''

upSpeed = 5
downSpeed = 2
desiredHeight = 7
print(growingPlant(upSpeed,downSpeed,desiredHeight))