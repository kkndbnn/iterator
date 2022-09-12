nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
class FlatIterator:
    def __init__(self,nested_list):
        self.start = -1
        self.end = len(nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        x = nested_list[self.start]
        for elem in x:
            print(elem)

def Flatgenerator(lst):
    for list in lst:
        for el in list:
            yield el
class NestedIterator:
    def __init__(self, list_):
        self._stopped = False
        self._list = list_
        self._i = 0
        self._j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self._i < len(self._list):
                if self._j < len(self._list[self._i]):
                    v = self._list[self._i][self._j]
                    self._j += 1
                    return v

                self._i += 1
                self._j = 0
            self._stopped = True
        raise StopIteration
def main(nested_list):
    flat_list = list(NestedIterator(nested_list))
    print(flat_list)

main(nested_list)
print(Flatgenerator(nested_list))
print(FlatIterator(nested_list))