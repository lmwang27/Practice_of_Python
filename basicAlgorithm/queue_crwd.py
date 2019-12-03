'''
--enqueue
--dequeue
--size
--is_empty
-- use linkedlist to implement it
'''

from linkedList_crwd import ListNode
from queue import Queue


class MyQueue:
    def __init__(self):
        self.count = 0 
        self.head = None
        self.tail = None
    
    def put(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def get(self):
        if self.head is None:
            raise Exception("this is a empty queue")
        cur = self.head
        self.head = cur.next
        self.count -= 1

        return cur.val

    def empty(self):
        return self.head is None

    def qsize(self):
        return self.count


if __name__ == "__main__":

    my_queue = MyQueue()
    my_queue.put(1)
    my_queue.put(3)
    my_queue.put(5)
    my_queue.put(7)

    que = Queue(maxsize = 100)


    print(my_queue.qsize())

