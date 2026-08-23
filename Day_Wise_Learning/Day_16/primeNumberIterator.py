class Prime:
    def __init__(self, limit=10):
        self.limit = limit
        self.start = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.limit:
            num = self.start
            self.start += 1

            if num < 2:
                continue

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                return num

        raise StopIteration

    def __len__(self):
        return self.limit


fib = Prime(30)

for i in fib:
    print(i)