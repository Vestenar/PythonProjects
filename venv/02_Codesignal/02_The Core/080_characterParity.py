def characterParity(symbol):
    try:
        if int(symbol)%2 == 0:
            return "even"
        else:
            return "odd"
    except:
        return "not a digit"

print(characterParity("23cdc"))

def characterParity(s):
    return "not a digit" if not s.isdigit() else ["even","odd"][int(s)%2]
print(characterParity("23cdc"))