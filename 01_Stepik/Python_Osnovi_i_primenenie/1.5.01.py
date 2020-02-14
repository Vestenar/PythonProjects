class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0

Counter

x = Counter()
x.inc()         # 1
print(x.count)
Counter.inc(x)  # 2 эквивалентно  # 1
print(x.count)
x.reset()
print(x.count)