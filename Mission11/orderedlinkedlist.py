class OrderedLinkedList:
    """ Represents a linked list datastructure. """

    def __init__(self, lst=[]):
        """
        Initialises a new LinkedList object.
        @pre:  list of cargo values (default = [])
        @post: A new OrderedLinkedList object has been initialised according to the list,
        """
        self.__length = 0
        self.__head = None
        for cargo in lst:
            self.insert(cargo)

    def size(self):
        """
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length

    def inc_size(self):
        self.__length += 1

    def dec_size(self):
        self.__length -= 1

    def first(self):
        """
        @pre:  -
        @post: Returns a reference to the head of this linked list,
               or None if the linked list contains no nodes.
        """
        return self.__head

    def remove_first(self):
        if self.__head is not None:
            self.__head = self.__head.next()
            self.dec_size()

    def add(self, cargo):
        self.insert(cargo)

    def insert(self, cargo):
        to_insert = Node(cargo)
        self.__length += 1
        if self.__head == None or self.__head.value() >= cargo:
            to_insert.set_next(self.__head)
            self.__head = to_insert
            return
        current = self.__head
        while type(current) == Node and type(current.next()) == Node:
            if current.next().value() >= cargo:
                break
            current = current.next()
        node_next = current.next()
        current.set_next(to_insert)
        to_insert.set_next(node_next)

    def remove(self, cargo):
        node = self.first()
        previous = node
        while node is not None:
            if node.value().coureur() == cargo:
                if node == self.first():
                    self.remove_first()
                    return True
                previous.set_next(node.next())
                self.dec_size()
                return True
            previous = node
            node = node.next()
        return False

    def get_as_array(self):
        node = self.first()
        r = []
        while node is not None:
            r.append(node.value())
            node = node.next()
        return r

    def search(self, cargo):
        """Renvoie le premier élément égal à cargo et sa position (commence à 1)

        Args:
            cargo (any): la valeur à rechercher
        """
        node = self.first()
        i = 1
        while node is not None:
            if node.value().coureur() == cargo:
                return (node.value(), i)
            i += 1
            node = node.next()
        return None

    def __str__(self) -> str:
        s = "[ "
        tail = self.__head
        while tail:
            s += str(tail.value()) + " "
            tail = tail.next()
        s += "]"
        return s


class Node:
    """ Represents a Node in a OrderedLinkedList data structure. """

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
