from resultat import Resultat
from coureur import Coureur

class OrderedLinkedList:

    def __init__(self, lst=[])-> None:
        """
        Initialises a new linked list object, with a given list of elements lst.
        @pre:  -
        @post: A new linked list object has been initialised.
               Its length is equal to the number of elements in lst.
               The data elements stored in the linked list's nodes correspond to those of the list lst,
               and appear in the same order as in that list.
               If no list lst is passed as argument, the newly created linked list
               will have 0 length, contain no nodes and its head will point to None. 
        """
        self.__length = 0          # current length of the linked list
        self.__head = None         # pointer to the first node in the list
        self.__last = None         # pointer to the last node in the list
        lst.reverse()              # reverse to ensure elements will appear in same order
        for e in lst:             # add elements of input list lst one by one
            self.add(e)

    def size(self) -> int:
        """
        Accessor method which returns the number of nodes contained in this linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length

    def inc_size(self) -> None:
        """
        Mutator method to increase the size count of this linked list by one.
        @pre:  -
        @post: 1 has been added to the size counter of the number of nodes contained in this linked list.
        """
        self.__length += 1

    def dec_size(self) -> None:
        """
        Mutator method to decrease the size count of this linked list by one.
        @pre:  -
        @post: 1 has been substracted from the size counter of the number of nodes contained in this linked list.
        """
        self.__length -= 1

    def first(self):
        """
        Accessor method which returns the first node of this linked list.
        @pre:  -
        @post: Returns a reference to the head of this linked list,
               or None if the linked list contains no nodes.
        """
        return self.__head

    def set_first(self, n):
        """
        Mutator method to reassign the head of this linked list to a new node.
        @pre:  -
        @post: The head of this linked list new refers to node n.
        """
        self.__head = n

    def add(self, cargo: Resultat):
        """ 
        Adds a new Node with given cargo to the front of this linked list. 
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented by 1.
               The head of the linked list now points to this new node.
        """
        to_insert = self.Node(cargo)
        self.__length += 1
        if self.__head == None:
            self.__head = to_insert
            return
        elif self.__head.value() > cargo.temps():
            to_insert.set_next(self.__head)
            self.__head = to_insert
            return
        current = self.__head
        while type(current) == self.Node and type(current.next()) == self.Node:
            if current.next().value() > cargo.temps():
                break
            current = current.next()

        node_next = current.next()
        current.set_next(to_insert)
        to_insert.set_next(node_next)

    def remove(self, coureur: Coureur):
        """
        Removes the node (associated to the coureur) from the list. Leaves the list intact if already empty. 
        """
        first = self.first()
        if first is None:
            current = first.next()
        if current is not None: 
            if current.value().coureur == coureur:
                

        if self.size() == 0:       # when there are no more elements in the list,
            self.__last = None       # remove the pointer to the last element

    def get(self, coureur: Coureur) -> Resultat:
        return self.first().value()

    class Node:

        def __init__(self, cargo, next=None):
            """
            Initialises a new Node object.
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
            Returns the value of the cargo contained in this node.
            @pre:  -
            @post: Returns the value of the cargo contained in this node, 
                   or None if no cargo  was put there.
            """
            return self.__cargo

        def next(self):
            """
            Returns the next node to which this node links.
            @pre:  -
            @post: Returns the node to which this node is linked with its 
                   next pointer, or None if that pointer is None.
            """
            return self.__next

        def set_next(self, node):
            """
            Sets the next node to which this node links to a new node.
            @pre:  -
            @post: The node to which this node is linked next, 
                has been set to the new node passed as parameter.
                   Can also be set to None by passing None as parameter.
            """
            self.__next = node

        def __str__(self):
            """
            Returns a string representation of the cargo of this node.
            @pre:  self is a (possibly empty) Node object.
            @post: Returns a print representation of the cargo contained in this Node.
            """
            return str(self.value())

        def __eq__(self, other) -> bool:
            """
            Comparator to compare two Node objects by their cargo. 
            """
            if other is not None:
                return self.value() == other.value()
            else:
                return False

        def print_list(self):
            """
            Prints the cargo of this node and then recursively of each node connected to this one.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "a b c ... ",
                   where "a" is the string-representation of this node,
                   "b" is the string-representation of my next node, and so on.
                   A space is printed in-between the printed value.
            """
            head = self
            tail = self.__next       # go to my next node
            if tail is not None:    # as long as the end of the list has not been reached
                print(head, end=" ")  # print my head
                tail.print_list()    # recursively print remainder of the list
            else:                   # print the last element
                print(head, end=" ")

        def print_backward(self):
            """
            Recursively prints the cargo of each node connected to this node (in opposite order),
            and then prints the cargo of this node as last value.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "... c b a",
                   where a is my cargo (self), b is the cargo of the next node, and so on.
                   The nodes are printed in opposite order: the last nodes' value is printed first.
            """
            head = self
            tail = self.__next        # go to my next node
            if tail is not None:     # as long as the end of the list has not been reached
                tail.print_backward()  # recursively print remainder of the list backwards
            print(head, end=" ")    # print my head

        def print_list_avec_separateur(self, separateur):
            head = self
            tail = self.__next      # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=separateur)  # print my head, with separateur
                # recursively print remainder of the list
                tail.print_list_avec_separateur(separateur)
            else:                 # print the last element
                print(head, end=" ")  # print my head, with a space
