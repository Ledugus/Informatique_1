class Node:
    """Represents a Node in a LinkedList data structure."""

    def __init__(self, cargo=None, next=None):
        """
        Creates a new Node object.
        @pre:  -
        @post: A new Node object has been initialised.
            A node can contain a cargo and a reference to another node.
            If none of these are given, the node is initialised with
            empty cargo (None) and no reference (None).
        """
        self.__cargo = cargo
        self.__next = next

    def value(self):
        """
        @pre:  -
        @post: Returns the value of the cargo contained in this node,
            or None if no cargo was put there.
        """
        return self.__cargo

    def set_value(self, value):
        """
        @pre:  -
        @post: The cargo of this node has been set to value.
        """
        self.__cargo = value

    def next(self):
        """
        @pre:  -
        @post: Returns the next node to which this node refers,
            or None if there is no next node.
        """
        return self.__next

    def set_next(self, node):
        """
        @pre:  -
        @post: The next node of this node has been set to node.
        """
        self.__next = node

    def __str__(self):
        """
        @pre:  self is a (possibly empty) Node object.
        @post: returns a print representation of the cargo contained in this Node.
        """
        return str(self.value())

    def __eq__(self, other):
        """
        Comparator to compare two Node objects by their cargo.
        """
        if other is not None:
            return self.value() == other.value()
        else:
            return False


class LinkedList:
    """Represents a linked list datastructure."""

    def __init__(self):
        """
        Initialises a new LinkedList object.
        @pre:  -
        @post: A new empty LinkedList object has been initialised.
            It has 0 length, contains no nodes and its head refers to None.
        """
        self.length = 0
        self.head = None

    def size(self):
        """
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.length

    def first(self):
        """
        @pre:  -
        @post: Returns a reference to the head of this linked list,
            or None if the linked list contains no nodes.
        """
        return self.head

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the front of this LinkedList.
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
            This new Node is added to the front of the LinkedList.
            The length counter has been incremented.
            The head of the list now points to this new node.
            Nothing is returned.
        """
        node = Node(cargo, self.head)
        self.head = node
        self.length += 1
