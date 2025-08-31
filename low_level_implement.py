class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.items[self.top] = item

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        self.rear += 1
        self.items[self.rear] = item

    def is_empty(self):
        return self.front == self.rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None
        return item

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is Node:
                    print("범위를 벗어난 삽입입니다.")
                    return
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, position):
        if self.is_empty():
            print("싱글 링크드 리스트가 비었습니다.")
            return

        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None or current.next is None:
                    print("범위를 벗어났습니다.")
                    return
                current = current.next
            deleted_node = current.next
            deleted_data = deleted_node.data
            current_next = current.next.next
        return deleted_data

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# 조합 구현 - 반복문
for i in range(1, 5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            print(i, j, k)

# 조합 구현 - 재귀

def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        
        for rest in comb(arr[i + 1:], n - 1): # 조합
        # for rest in comb(arr[:i] + arr[i+1:], n - 1) # 순열
        # for rest in comb(arr, n - 1): # 중복 순열
        # for rest in comb(arr[i:], n - 1): # 중복 조합
            result.append([elem] + rest)

    return result

print(comb([1, 2, 3, 4], 3))