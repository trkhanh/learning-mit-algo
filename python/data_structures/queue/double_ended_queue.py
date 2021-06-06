# Python code to demonstrate working of
# extend(), extendleft(), rotate(), reverse()

import collections

de = collections.deque([1, 2, 3])

# using extend() to add numbers to right end
de.extend([4, 5, 6])
print("The deque after extending deque at end is : ")
print(de)
de.extendleft([7, 8, 9])
print("The deque after extending deque at beginning is : ")
print(de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)
# printing modified deque
print("The deque after rotating deque is : ")
print(de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print("The deque after reversing deque is : ")
print(de)

startValue = de.pop()
print("The deque after popping value at end is : ")
print(de)

startValue = de.popleft()
print("The deque after popping value at start is : ")
print(de)

# eliminate element searched by value
de.remove(5)

print("The deque after eliminating element searched by value : ")
print(de)
