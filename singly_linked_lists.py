class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def addToFront(self, val):
        # create node with the given value
        new_node = SLNode(val)
        # set new_node's nex to current head
        new_node.next = self.head
        # set head to new node
        self.head = new_node
        return self

    def addToEnd(self, val):
        if self.head == None:
            self.addToFront(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

my_list = SList()
my_list.addToFront('Jim').addToFront('Dwight').addToFront('Andy').addToEnd('Zack').print_values()


