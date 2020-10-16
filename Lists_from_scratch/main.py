import lists
import numpy as np



#Init list
my_linked_list = lists.LinkedList()
my_stack = lists.Stack()
my_queue = lists.Queue()
my_tree = lists.Tree()
my_recalibrator = lists.TreeRecalibrator()

for i in range(100):
    my_tree.insert(np.random.randint(0, 100))

my_tree.display()

my_recalibrator.recalibrate(my_tree)



"""
# Test Queue
my_queue.add(2)
my_queue.add(5)
print(my_queue.pop())

# Test Stack
my_stack.add(10)
my_stack.add(332)
print(my_stack.pop())

# Test Linked List
# Append 10 Values to the list
for i in range(1, 11):
    my_linked_list.append(i)

# Insert specific value at specific index
my_linked_list.insert(2, 22)

# Delete Value at specific index
my_linked_list.delete(3)

# Print the list
for i in range(0, my_linked_list.size):
    print(my_linked_list.value_at(i))

# Print Value at specific Position
print(my_linked_list.value_at(2))
"""