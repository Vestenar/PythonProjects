class Stack:

    def __init__(self):
        self.stack = []
        self.stack_max = [-float('inf')]

    def pop(self):
        if self.stack[-1] == self.stack_max[-1]:
            self.stack_max.pop()
        self.stack.pop()

    def push(self, arg):
        if not self.stack_max or arg >= self.stack_max[-1]:
            self.stack_max.append(arg)
        self.stack.append(arg)

    def max(self):
        print(self.stack_max[-1])


s = Stack()
for i in range(int(input())):

    line = input()
    if line.startswith('push'):
        s.push(int(line.split()[-1]))
    elif line == 'max':
        s.max()
    elif line == 'pop':
        s.pop()
    # print(f'{s.stack=} ----> {s.stack_max=}')
