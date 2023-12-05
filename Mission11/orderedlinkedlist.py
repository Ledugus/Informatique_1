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

    def print(self):
        """
        Prints the contents of this LinkedList and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list()
        print("]")

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

    def print_backward(self):
        """
        Prints the contents of this LinkedList and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each
               of the LinkedList's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")

    def __str__(self, sep=" ") -> str:
        s = ""
        i = 1
        for cargo in self.get_as_array():
            s += f"{i}  {cargo}" + sep
            i += 1
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

    def print_list(self):
        """
        Prints the cargo of this node and then recursively
        of each node connected to this one.
        @pre:  -
        @post: Has printed a space-separated list of the form "a b c ... ",
               where "a" is the string-representation of this node,
               "b" is the string-representation of my next node, and so on.
               A space is printed after each printed value.
        """
        print(self.value(), end=" ")     # print my value
        tail = self.next()       # go to my next node
        if tail is not None:    # as long as the end of the list has not been reached
            tail.print_list()    # recursively print remainder of the list

    def print_backward(self):
        """
        Recursively prints the cargo of each node connected to this node (in opposite order),
        and then prints the cargo of this node as last value.
        @pre:  -
        @post: Has printed a space-separated list of the form "... c b a",
               where a is my cargo (self), b is the cargo of the next node, and so on.
               The nodes are printed in opposite order: the last node's value
               is printed first.
        """
        tail = self.next()        # go to my next node
        if tail is not None:     # as long as the end of the list has not been reached
            tail.print_backward()  # recursively print remainder of the list backwards
        print(self.value(), end=" ")    # print my value
