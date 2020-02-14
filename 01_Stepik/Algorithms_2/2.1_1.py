class heap:
    def __init__(self, inmass: list=[]) -> list:
        self.heap = ['head'] + inmass
        self.size = len(self.heap) - 1
        self.replaces = []
        self.buildheap()

    def buildheap(self):
        for i in range(self.size // 2, 0, -1):
            self.siftdown(i)

    def parent(self, i):
        return i // 2

    def leftchild(self, i):
        return 2 * i

    def rightchild(self, i):
        return 2 * i + 1

    def siftup(self, i):
        while i > 1 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def siftdown(self, i):
        maxindex = i
        l = self.leftchild(i)
        r = self.rightchild(i)
        if l <= self.size and self.heap[l] > self.heap[maxindex]:
            maxindex = l
        if r <= self.size and self.heap[r] > self.heap[maxindex]:
            maxindex = r
        if i != maxindex:
            self.heap[i], self.heap[maxindex] = self.heap[maxindex], self.heap[i]
            self.replaces.append([i - 1, maxindex - 1])
            self.siftdown(maxindex)

    def insert(self, p):
        self.size += 1
        self.heap.append(p)
        self.siftup(self.size)

    def extractmax(self):
        result = self.heap[1]
        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        self.size -= 1
        self.heap = self.heap[:-1]
        self.siftdown(1)
        return result

    def remove(self, i):
        self.heap[i] = float('inf')
        self.siftup(i)
        self.extractmax()

    def changepriority(self, i, p):
        oldp = self.heap[i]
        self.heap[i] = p
        if p > oldp:
            self.siftup(i)
        else:
            self.siftdown(i)

    def show(self):
        print('-' * 80)
        print(f'drawing heap with id{str(id(self))}')
        from math import log2
        dots = 2 * int(log2(len(self.heap) + 1) + 1)
        i = 1
        while dots > 0:
            part = self.heap[2 ** (i - 1):(2 ** i)]
            print("." * dots + ('.'*dots).join(map(str, part)) + '.' * dots)
            dots //= 2
            i += 1


H = heap([-1 * int(i) for i in input().split()])
print(len(H.replaces))
for repl in H.replaces:
    print(' '.join(map(str, repl)))

# a = [[-1, 1], [0, 2], [0, 3], [-2, 4], [0, 5], [-5, 6], [0, 7], [-2, 8], [0, 9]]
# print(a)
# H = heap(a)
# H.show()
# H.changepriority(1, [-5,9])
# H.show()
# H.changepriority(1, [-2,7])
# H.show()
# H.changepriority(1, [-4,5])
# H.show()
# H.changepriority(1, [-2,3])
# H.show()
# H.changepriority(1, [-3,2])
H.show()