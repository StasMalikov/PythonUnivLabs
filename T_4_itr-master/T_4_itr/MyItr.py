class MyIterator:
    def __init__(self, start_number, end_number, step):
        self.i = start_number - step
        self.end_number = end_number
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.i < self.end_number - self.step):
            self.i += self.step
            return self.i
        else:
            raise StopIteration
