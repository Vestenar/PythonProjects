p = 1000000007
x = 263
chain_struct = {}


def add_string(string):
    ind = get_hash(string)
    prev = chain_struct.get(ind, [])
    if string not in prev:
        prev.insert(0, string)
    chain_struct[ind] = prev

def del_string(string):
    ind = get_hash(string)
    if string in chain_struct.get(ind, []):
        chain_struct.get(ind, []).remove(string)

def find_string(string):
    ind = get_hash(string)
    print('yes' if string in chain_struct.get(ind, []) else 'no')

def check_string(ind):
    print(' '.join(chain_struct.get(int(ind), [])))

def get_hash(word):
    hash = 0
    for ch in range(len(word)):
        hash += ord(word[ch]) * x**ch
    return (hash % p) % m


m = int(input())
n = int(input())
commands = {
    'add': add_string,
    'del': del_string,
    'find': find_string,
    'check': check_string}


for _ in range(n):
    comm, data = input().split()
    action = commands.get(comm)
    action(data)
