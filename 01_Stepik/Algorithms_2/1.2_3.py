class Server:
    def __init__(self, maxlen):
        self.buffer = []
        self.maxlen = maxlen
        self.cputime = 0

    def fill_buffer(self, arrival, duration):

        while self.buffer and self.buffer[0] <= arrival:
            self.buffer.pop(0)

        if len(self.buffer) >= self.maxlen:
            print(-1)
        else:
            self.cputime = max(arrival, self.buffer and self.buffer[-1] or arrival)
            self.buffer.append(self.cputime + duration)
            print(self.cputime)


buffer, n = map(int, input().split())
s = Server(maxlen=buffer)
for i in range(n):
    s.fill_buffer(*(map(int, input().split())))
    print(s.buffer)



