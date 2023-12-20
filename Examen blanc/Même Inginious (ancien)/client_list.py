class Client:
    """
    Un client. Chaque client a un nom d'utilisateur (supposé unique,
    par exemple adresse email) et un code pin qui est stocké comme un entier.
    """

    def __init__(self, name, pin):
        self.userName = name
        self.pin = pin

    def getUserName(self):
        return self.userName

    def getPin(self):
        return self.pin

    def setPin(self, pin):
        self.pin = pin

    def __str__(self):
        return self.userName + "(" + str(self.pin) + ")"


class ClientList:
    """Une liste de clients"""

    # un noeud de la liste
    class Node:
        def __init__(self, client, prev):
            self.data = client
            self.link = prev

    def __init__(self):
        self.last = None

    def __str__(self):
        pass

    #########################
    ### QUESTION : UPDATE ###
    #########################
    def update(self, name, pin):
        current_node = self.last
        while current_node:
            if current_node.data.getUserName() == name:
                current_node.data.setPin(pin)
                return
            current_node = current_node.link
        new_node = ClientList.Node(Client(name, pin), self.last)
        self.last = new_node
