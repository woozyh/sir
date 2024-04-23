class Node(object):
    """
    `A simple class for abstracting nodes in linked list.`
    `docId`: gets an integer value for document id.
    `next`: gets the next node for pointing.
    """    
    __slots__ = ('docId', 'next')
    def __init__(self, docId: int, next=None) -> None:
        self.docId = docId
        self.next  = next


class list(object):

    """
    A simple linked list implementation with 3 parameter:
        `head`: always points to first node of list.
        `tail`: always points to last node of list.
        `size`: for each item it stores the size that item.(size -> length)
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def addToTail(self, docId: int) -> None:
        newDoc = Node(docId)
        if (self.isEmpty()):
            self.head = self.tail = newDoc
        else: 
            self.tail.next = newDoc
            self.tail = newDoc
        self.size += 1
