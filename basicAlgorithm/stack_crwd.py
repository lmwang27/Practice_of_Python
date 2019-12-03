'''

there is no stack in python
--push
--pop
--peek
--is_empty
--size

'''

class MyStack:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.size ==0

    def push(self, item):
        self.items.append(item)
        self.size +=1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()

    def peek(self):
        if self.size > 0:
            return self.items[-1]

    def size(self):
        return self.size


if __name__ == '__main__':
    my_stack = MyStack()

    for i in range(50):
        my_stack.push(i)

    while not my_stack.is_empty():
        print(my_stack.pop(), end=' ')

    print()
