class CircularLinkedList:

    class Node:
        def __init__(self, cargo=None, next=None):
            """ Initialises a new Node object. """
            self.__cargo = cargo
            self.__next = next

        def value(self):
            """ Returns the value of the cargo contained in this node. """
            return self.__cargo

        def next(self):
            """ Returns the next node to which this node links. """
            return self.__next

        def set_next(self, node):
            """ Sets the next node to which this node links to a new node. """
            self.__next = node

        def __str__(self) -> str:
            return str(self.value())

    def __init__(self):
        """ Initialises a new empty circular linked list.
        @pre:  -
        @post: A new circular linked list with no nodes has been initialised.
               The first pointer refers to None.
        """
        self.__first = None       # pointer to the first node
        self.__last = None       # pointer to the last node

    def first(self):
        """ Returns the first node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the first node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__first

    def last(self):
        """ Returns the last node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the last node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__last

    def add(self, cargo):
        """ Adds new Node with given cargo to front of this circular linked list.
        @pre:  self is a (possibly empty) CircularLinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the circular linked list.
               The head of the list now points to this new node.
               The last node now points to this new node.
        """
        node = self.Node(cargo, self.first())
        self.__first = node
        if self.last() == None:   # when this was the first element being added,
            self.__last = node     # set the last pointer to this new node
        self.last().set_next(node)


def remove(self, cargo):
    """ Removes a node with given cargo from the circular linked list.
    @pre:  -
    @post: A node with given cargo was removed from the circular linked list.
            The removed node, with next pointer set to None, is returned.
            In case multiple nodes with this cargo exist, only one is removed.
            The list is unchanged if no such node exists or the list is empty.
            In that case, None is returned as result.
    """
    if self.first() == None:
        return None
    node = self.first()
    previous = node
    if node.value() == cargo:
        print("node=first")
        print(node.next())
        if node == node.next():
            self.__first = None
            self.__last = None
        else:
            self.__first = node.next()
            self.__last.set_next(self.first())
        node.set_next(None)
        return node
    node = node.next()
    while node != self.first():
        if node.value() == cargo:
            if node == self.first():
                self.__first = node.next()
                node.set_next(None)
                return node
            if node == self.last():
                self.__last = previous
            previous.set_next(node.next())
            node.set_next(None)
            return node
        previous = node
        node = node.next()
    return None


def removeAll(self, cargo):
    """ Removes all nodes with given cargo. """
    while self.remove(cargo) != None:
        pass

    def __str__(self):
        s = "[ "
        tail = self.first()
        while tail:
            s += str(tail.value()) + " "
            tail = tail.next()
            if tail == self.first():
                break
        s += "]"
        return s


c = CircularLinkedList()
c.add('first')
c.add('3')
c.add('coucou')
c.add('2')
c.add('3')
c.add('3')
c.add('last')

print(c)
print(c.remove('coucou'))
print(c)
print(c.removeAll('3'))
print(c)
c2 = CircularLinkedList()
c2.add('alone')
c2.remove('alone')
print(c2.first(), c2.last())
