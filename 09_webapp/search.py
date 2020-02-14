def search(phrase, letters="aioue"):
    return set(phrase).intersection(set(letters)) 
