# ************************* DS by Amulya's Academy ******************************

# Day-1
# Built-in Data Structures
"""
1. List
2. Tuple
3. Set
4. Dictionary
"""

# Day-2

# List
l1 = [1,23,'r5',2,234]
print(l1)

# Tuple
T1 = (1,2,4,4)
T2 = (1,)
T3 = 1,2,3
print(type(T1, T2, T3))

# Day-3

# Dictionary
D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': [1,2,3,4,45]}
D3 = {'a': 1, 'b': 'Sachin'}

# Set
S1 = {12,4,23,4,23}

# Day-4
# Introduction to the stacks

# Day-5

# Implement of stacks in python using list and modules
# push => append
# pop => pop
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
stack.pop()
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)
stack.pop()

# We will made a program to execute stack operations
def Push_Element():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def Pop_Element():
    if not stack:
        print('Stack is empty...!')
    else:
        e = stack.pop()
        print('Element Removed: ',e)
        print(stack)

if __name__ == '__main__':
    
    while True:
        try:
            user = int(input('Enter the operation (1. Push || 2. Pop || 3. quit): '))
            if user == 1:
                Push_Element()
            if user == 2:
                Pop_Element()
            if user == 3:
                print("Thank you for your valuable time...!")
                quit()
        except Exception as E:
            print('Error occured: ', E)
            pass


# Day-6
# Stack using python module

import collections

# Implement of stacks in python using list and modules
# push => append
# pop => pop

# We will made a program to execute stack operations
def Push_Element():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def Pop_Element():
    if not stack:
        print('Stack is empty...!')
    else:
        e = stack.pop()
        print('Element Removed: ',e)
        print(stack)

if __name__ == '__main__':
    stack = collections.deque()
    
    while True:
        try:
            user = int(input('Enter the operation (1. Push || 2. Pop || 3. quit): '))
            if user == 1:
                Push_Element()
            if user == 2:
                Pop_Element()
            if user == 3:
                print("Thank you for your valuable time...!")
                quit()
        except Exception as E:
            print('Error occured: ', E)
            pass

# Stack using python module

import queue

# Implement of stacks in python using list and modules
# push => append
# pop => pop

# We will made a program to execute stack operations
def Push_Element():
    element = input("Enter the element: ")
    stack.put(element)

def Pop_Element():
    if not stack:
        print('Stack is empty...!')
    else:
        e = stack.get(timeout=1)
        print('Element Removed: ',e)

if __name__ == '__main__':
    stack = queue.LifoQueue(10)
    
    while True:
        try:
            user = int(input('Enter the operation (1. Push || 2. Pop || 3. quit): '))
            if user == 1:
                Push_Element()
            if user == 2:
                Pop_Element()
            if user == 3:
                print("Thank you for your valuable time...!")
                quit()
        except Exception as E:
            print('Error occured: ', E)
            pass



# Day-7
# Introduction to queue in python 

# Day-8
# queue using python list

def enqueue():
    element = int(input('Enter the number: '))
    queue.append(element)
    print("Element Added: ",element)
    print(queue)

def dequeue():
    if not queue:
        print('it\'s am empty queue.')
    else:
        e = queue.pop(0)
        print("Element Removed: ", e)
        print(queue)

def display():
    print(queue)

if __name__ == '__main__':
    
    queue = []
    while True:
        try:
            user = int(input("Enter the operation (1. Enqueue || 2. Dequeue || 3. Display || 4. Quit): "))
            if user == 1:
                enqueue()
            elif user == 2:
                dequeue()
            elif user == 3:
                display()
            elif user == 4:
                print("Thanks for your valuable time...!")
                quit()
            else:
                print("Enter the correct operation.")
        except Exception as E:
            print('Error Occurded: ',E)
            continue



# Day-9
# queue using python module - Collections
import collections

def enqueue():
    element = int(input('Enter the number: '))
    queue.appendleft(element)
    # queue.append(element)
    print("Element Added: ",element)
    print(queue)

def dequeue():
    if not queue:
        print('it\'s am empty queue.')
    else:
        e = queue.pop()
        e = queue.popleft()
        print("Element Removed: ", e)
        print(queue)

def display():
    print(queue)

if __name__ == '__main__':
    
    queue = collections.deque()
    while True:
        try:
            user = int(input("Enter the operation (1. Enqueue || 2. Dequeue || 3. Display || 4. Quit): "))
            if user == 1:
                enqueue()
            elif user == 2:
                dequeue()
            elif user == 3:
                display()
            elif user == 4:
                print("Thanks for your valuable time...!")
                quit()
            else:
                print("Enter the correct operation.")
        except Exception as E:
            print('Error Occurded: ',E)
            continue


# ----------------------------------------------------------------------------------------

import queue

def Enqueue():
    # Arguments: q.put(element, block=True, timeout)
    element = input('Enter your Choice: ')
    q.put(element)
    print('Element Added: ', element)
    print(q)

def Dequeue():
    # Arguments: q.put(element, block=True, timeout)
    e = q.get()
    print('Element Removed: ', e)
    print(q)

def Display():
    print(q)

if __name__ == '__main__':

    # Here you can add attribute of limit
    q = queue.Queue(4)
    q = queue.Queue()
    user = int(input('Enter the Operation || 1. Enqueue || 2. Dequeue || 3. Display || 4. Quit ||: '))
    while True:
        try:
            if user == 1:
                Enqueue()
            elif user == 2:
                Dequeue()
            elif user == 3:
                Display()
            elif user == 4:
                print("Thanks for your valuable time...!")
                quit()
            else:
                print("Enter the correct operation.")
        except Exception as E:
            print('Error Occurded: ',E)
            continue




# Day-10

# Priority queue using list
que = []
que.append(1)
que.append(3)
que.append(5)
que.sort()
que.pop(0)
que.pop(0)
que.pop(0)

# Priority queue using python module - queue
import queue

def enqueue():
    element = int(input('Enter the number: '))
    q.put(element)
    q.sort()
    # q.sort(reverse=True)  # If you want to make your queue reverse then use this method
    print("Element Added: ",element)
    print(q)

def dequeue():
    if not q:
        print('it\'s am empty queue.')
    else:
        e = q.get()
        print("Element Removed: ", e)
        print(q)

def display():
    print(q)

if __name__ == '__main__':
    
    q = queue.PriorityQueue()
    while True:
        try:
            user = int(input("Enter the operation (1. Enqueue || 2. Dequeue || 3. Display || 4. Quit): "))
            if user == 1:
                enqueue()
            elif user == 2:
                dequeue()
            elif user == 3:
                display()
            elif user == 4:
                print("Thanks for your valuable time...!")
                quit()
            else:
                print("Enter the correct operation.")
        except Exception as E:
            print('Error Occurded: ',E)
            continue







# Day 11
# Introduction to linked list



# Day 12
# Intorduction to singly linked list and how it works





# Day 13
# 