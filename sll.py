class SLNode:
    """Singly Linked List Node"""

    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    """Singly Linked List"""

    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        """add node to the front of the list"""
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def add_to_back(self, val):
        """add node to the back of the list"""

        if self.head is None:
            return self.add_to_front(val)

        runner = self.next
        return self

    def print_list(self):
        """print the singly linked list with each node on line"""

        if self.head is None:
            print("Empty List")
            return self

        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next

        return self


sll_1 = SList()

sll_1.print_list()
sll_1.add_to_front(10).add_to_front(20)
sll_1.print_list()
