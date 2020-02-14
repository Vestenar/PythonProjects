import time

def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elasped = time.clock() - start
            self.alltime += elasped
            if trace:
                format ='%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elasped, self.alltime)
                print(format % values)
            return result
    return Timer
