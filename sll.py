"""This is an implementation of a Singly Linked List"""

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
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = SLNode(val)
        return self

    def remove_from_front(self):
        """remove the node at the front of the list"""

        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        return temp.value

    def remove_from_back(self):
        """remove the node at the back of the list"""

        if self.head is None:
            return

        if self.head.next is None:
            return self.remove_from_front()

        runner = self.head
        # move runner to the second to last node
        while runner.next.next is not None:
            runner = runner.next
        value = runner.next.value
        runner.next = None
        return value

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
sll_1.add_to_front(10).add_to_front(20).add_to_back(5)
sll_1.print_list()

print("-----")
print(sll_1.remove_from_front())
print(sll_1.remove_from_back())
print("-----")
sll_1.print_list()
