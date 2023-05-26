class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """print the singly linked list with each node on line"""

        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next

        return self
