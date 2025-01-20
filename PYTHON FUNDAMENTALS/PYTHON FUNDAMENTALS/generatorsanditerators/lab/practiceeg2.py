class IntegerIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        # The __iter__ method returns the iterator object itself
        return self

    def __next__(self):
        # The __next__ method defines the logic for getting the next item
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # Raise StopIteration when the iteration is complete

# Example usage:
numbers = [10, 20, 30, 40, 50]
iterator = IntegerIterator(numbers)

for num in iterator:
    print(num)
