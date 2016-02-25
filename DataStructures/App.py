from DataStructures.LinkedList import  LinkedList
from DataStructures.Stack import  Stack
from DataStructures.Queue import  Queue

list = LinkedList()

list.insertEnd(12)
list.insertEnd(122)
list.insertEnd(32)
list.insertStart(31)

list.traverseList()

list.remove(12)

list.traverseList()

print("\n")
print("Stack:")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.size())

print("\n")
print("Queue:")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.size())