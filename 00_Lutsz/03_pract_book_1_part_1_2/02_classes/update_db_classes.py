import shelve

db = shelve.open('class-shelve')
bob = db['bob']
bob.giveRaise(0.1)
db['bob'] = bob

sue = db['sue']
sue.name = 'Sue Joannes'
db['sue'] = sue
db.close()
