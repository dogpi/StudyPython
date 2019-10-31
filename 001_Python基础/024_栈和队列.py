'''
栈：先进后出FILO
队列：先进先出FIFO
'''

# 模拟栈
stack = []

stack.append('A')
print(stack)
stack.append('B')
print(stack)
stack.append('C')
print(stack)
stack.append('D')
print(stack)
print()
print("pop",stack.pop())
print(stack)
print("pop",stack.pop())
print(stack)
print("pop",stack.pop())
print(stack)
print("pop",stack.pop())
print(stack)

print("**************************")

# 模拟队列
import collections

queue = collections.deque()
print(queue)

queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)
queue.append("D")
print(queue)

print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)