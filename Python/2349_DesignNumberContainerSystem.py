import heapq

class NumberContainers:

    def __init__(self):
        self.numbers_container = {}
        self.number_indices = {}

    def change(self, index: int, number: int) -> None:
        self.numbers_container[index] = number  

        if number in self.number_indices:
            heapq.heappush(self.number_indices[number], index)
        else:
            self.number_indices[number] = [index]
            heapq.heapify(self.number_indices[number])

    def find(self, number: int) -> int:
        while number in self.number_indices and self.number_indices[number]:
            if self.numbers_container[self.number_indices[number][0]] == number:
                return self.number_indices[number][0]
            else:
                heapq.heappop(self.number_indices[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

obj = NumberContainers()
print(obj.find(10))
obj.change(2, 10)
obj.change(1, 10)
obj.change(3, 10)
obj.change(5, 10)
print(obj.find(10))
obj.change(1, 20)
print(obj.find(10))