class Node():

    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_previous(self):
        return self.previous_node

    def set_previous(self, new_previous):
        self.previous_node = new_previous

    def get_current(self):
        return self

