class ListNode:
    def __init__(self , val):
        self.val = val
        self.next = None


def build_linked_list():
    print('Build linked list')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1


def run_linkedList_example():
    print("linkedlist example")
    node_1 = build_linked_list()

    cur = node_1

    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


# did not modify next , so data will not change
def run_linked_list_quiz_1():
    print('linked list quiz_1')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_2 = node_3

    cur = node_1

    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


def run_linked_list_quiz_2():
    print('linked list quiz_2')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_1 = node_2

    cur = node_1

    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


def run_linked_list_quiz_3():
    print('linked list quiz_2')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_1.next = node_3

    cur = node_1

    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, location):
        cur = self.head
        count = 0
        while cur is not None:
            if count == location:
                return cur.val
            cur = cur.next
            count += 1

    def add(self, location, val):
        prev = self.head

        if location == 0:
            node = ListNode(val)
            node.next = self.head
            self.head = node
            self.size +=1
        else:
            for i in range(location-1):
                prev = prev.next
            node = ListNode(val)
            node.next = prev.next
            prev.next = node
            self.size += 1

    def set(self, location, val):
        cur = self.head
        for i in range(location):
            cur = cur.next
        cur.val = val

    def remove(self, location):
        cur = self.head
        if location > 0:
            pre = self.head
            for i in range(location-1):
                pre = pre.next
            pre.next = pre.next.next
            self.size -= 1
        elif location == 0:
            self.head = self.head.next
            self.size -= 1

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()


if __name__ == '__main__':
    myList = MyLinkedList();
    myList.add(0, 1)
    myList.add(1, 3)
    myList.add(2, 5)
    myList.add(3, 7)

    myList.remove(2)
    myList.set(2, 9)

    myList.traverse()
