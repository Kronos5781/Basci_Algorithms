import nodes

class LinkedList():
    def __init__(self, head=None, root=None):
        self.head = head
        self.root = root
        self.size = 0

    def node_at_index(self, index):
        current = self.root
        counter = 0
        while current:
            if counter == index:
                return current.get_current()
            current = current.get_next()
            counter += 1

    def append(self, data):
        new_node = nodes.Node(data)

        # If This is the first Node set it to be the Head else Link it to the old head and then set it as the new one
        if self.head == None:
            self.head = new_node
        else:
            new_node.set_previous(self.head)
            self.head.set_next(new_node)
            self.head = new_node

        # If the node has no previous Node Set it as the Root Node
        if new_node.get_previous() == None:
            self.root = new_node

        #Increase Size
        self.size += 1

    def insert(self, index, data):
        # Create New Node
        new_node = nodes.Node(data)

        # Update all Links in order
        new_node.set_previous(self.node_at_index(index - 1))
        new_node.set_next(self.node_at_index(index))

        prev = new_node.get_previous()
        next = new_node.get_next()

        prev.set_next(new_node)
        next.set_previous(new_node)

        # Increase Size
        self.size += 1

    def delete(self, index):
        # update links
        prev, next = self.node_at_index(index).get_previous(), self.node_at_index(index).get_next()
        prev.set_next(next)
        next.set_previous(prev)

        #Decrease Size
        self.size -= 1

    def value_at(self, index):
        return self.node_at_index(index).get_data()


class Stack:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def add(self, data):
        new_node = nodes.Node(data)

        if self.head == None:
            self.head = new_node
        else:
            new_node.set_previous(self.head)
            self.head = new_node

        self.size += 1

    def pop(self):
        current = self.head
        self.head = current.get_previous()
        self.size -= 1

        return current.get_data()


class Queue:

    def __init__(self, root=None, head=None):
        self.root = root
        self.head = head
        self.size = 0

    def add(self, data):
        new_node = nodes.Node(data)

        # If This is the first Node set it to be the Head else Link it to the old head and then set it as the new one
        if self.head == None:
            self.head = new_node
        else:
            new_node.set_previous(self.head)
            self.head.set_next(new_node)
            self.head = new_node

        # If the node has no previous Node Set it as the Root Node
        if new_node.get_previous() == None:
            self.root = new_node

        #Increase Size
        self.size += 1

    def pop(self):
        current = self.ro
        self.size -= 1

        return current.get_data()


class Tree:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def insert_forward(self, current, new ,data):
        # Recursive Function that searches for the correct point in the Tree to insert a new value
        if current.get_data():
            if data < current.get_data():
                if current.get_previous() is None:
                    current.set_previous(new)
                else:
                    self.insert_forward(current.get_previous(), new, data)
            elif data > current.get_data():
                if current.get_next() is None:
                    current.set_next(new)
                else:
                    self.insert_forward(current.get_next(), new, data)
        else:
            current.data = data

    def get_tree(self, current, arr):
        # Recursive function that loops through the whole tree and appends the values to a Linked List
        # From lowest to highest
        if current.get_previous() != None:
            self.get_tree(current.get_previous(), arr)
        arr.append(current.get_data())
        if current.get_next() != None:
            self.get_tree(current.get_next(), arr)

    def display_aux(self, current):
        # When the Node has no Subnode
        if current.get_next() is None and current.get_previous() is None:
            line = str(current.get_data())
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # When the Node only has a Subnode on the left
        if current.get_next() is None:
            lines, n, p, x = self.display_aux(current.get_previous())
            s = str(current.get_data())
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # When the Node has a Subnode only on the right
        if current.get_previous() is None:
            lines, n, p, x = self.display_aux(current.get_next())
            s = str(current.get_data())
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # When the Node has two Subnodes
        left, n, p, x = self.display_aux(current.get_previous())
        right, m, q, y = self.display_aux(current.get_next())
        s = str(current.get_data())
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def insert(self, data):
        new_node = nodes.Node(data)

        if self.root == None:
            self.root = new_node
        else:
            self.insert_forward(self.root, new_node, data)

    def display(self):
        lines, *_ = self.display_aux(self.root)
        for line in lines:
            print(line)



class TreeRecalibrator:

    def __init__(self):
        pass

    def copy_arr(self, arr, new_arr, start, end):
        # Copy values from one array to the other based on start and end parameters start = 0 --> index = 0
        for i in range(start, end):
            new_arr.append(arr.value_at(i))

    def recalibrate_forward(self, new_tree, arr):
        # Get Middle of the array and insert it into the new tree
        new_tree.insert(arr.value_at(arr.size // 2))

        #Initialize 2 new linked lists for the two halves of the array
        left = LinkedList()
        right = LinkedList()

        # Copy the old array into the new ones
        self.copy_arr(arr, left, 0, arr.size // 2)
        self.copy_arr(arr, right, (arr.size + 1) // 2, arr.size )

        # If the array is at least 3 numbers in size Call the Function recursively to repeat the process
        # This is done for both the 'left' and 'right' array
        # If the array is to small to split just add the numbers to the Tree in reverse
        if left.size > 2:
            self.recalibrate_forward(new_tree, left)
        else:
            for i in range(left.size - 1, -1, -1):
                new_tree.insert(left.value_at(i))
        if right.size > 2:
            self.recalibrate_forward(new_tree, right)
        else:
            for i in range(right.size - 1, -1, -1):
                new_tree.insert(right.value_at(i))


    def recalibrate(self, tree):
        # Init a new LinedList called array for the values of the old BinaryTree and a new Tree to save the recalibrated values to
        arr = LinkedList()
        new_tree = Tree()

        # Get the values out of the old Tree and call the recursive calibration function
        tree.get_tree(tree.root, arr)
        self.recalibrate_forward(new_tree, arr)

        # Display the recalibrated Binary tree
        new_tree.display()
