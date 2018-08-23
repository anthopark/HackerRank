class ListNode:
    def __init__(self, data=-1):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLength(self):
        count = 0
        curr = self.head
        while curr != None:
            curr = curr.next
            count += 1
        
        return count

    def addNode(self, data):
        
        newNode = ListNode(data)
        
        if self.head == None:
            self.head = newNode

        else:
            self.tail.next = newNode
        
        self.tail = newNode
        return
    
    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data, " ", sep='', end='')
            curr = curr.next
        print()


sll = SinglyLinkedList()
sll.addNode(1)
sll.addNode(2)
sll.addNode(3)
sll.addNode(4)
sll.addNode(5)


print(sll.getLength())
sll.printList()

def nthToTheLast(sll: SinglyLinkedList, n:int):
    firstPtr = secondPtr = sll.head
    count = 0
    while firstPtr != None:       
        firstPtr = firstPtr.next
        if count > n:
            secondPtr = secondPtr.next
        count += 1
        
    return secondPtr.data

n = int(input("Enter nth: "))
print(nthToTheLast(sll, n))
