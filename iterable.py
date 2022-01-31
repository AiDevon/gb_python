class MyIterable:
    def __init__(self, counter: int):
        self.counter = counter
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start >= self.counter:
            raise StopIteration
        else:
            return self.start

for x in MyIterable(10):
    print(x)