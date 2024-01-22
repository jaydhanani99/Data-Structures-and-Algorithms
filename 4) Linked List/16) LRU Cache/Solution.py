class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key, value): 
        self.next   = None
        self.prev   = None
        self.value  = value
        self.key    = key
        
class LRUCache:

    def __init__(self, capacity: int):
        self.hash       =   {}
        self.head       =   None
        self.tail       =   None
        self.size       =   0
        self.capacity   =   capacity

    def get(self, key: int) -> int:
        if self.hash.get(key):
            node    =   self.hash[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.hash.get(key) is None:
            node    =   Node(key, value)
            self.addNode(node)
        else:
            node            =   self.hash[key]
            node.value      =   value
            self.removeNode(node)
            self.addNode(node)
            
    def addNode(self, node):
        if self.size    ==  self.capacity:
            self.removeNode(self.tail)
            
        if self.head is None:
            self.head   =   node
            self.tail   =   node
        else:
            self.head.prev  =   node
            node.next       =   self.head
            self.head       =   node
        self.size       +=  1
        self.hash[node.key]  =   node
            
    def removeNode(self, node):
        if self.head is node:
            if self.size == 1:
                self.head   =   None
                self.tail   =   None
            else:
                self.head       =   self.head.next
                self.head.prev  =   None
        elif self.tail is node:
            if self.size == 1:
                self.head   =   None
                self.tail   =   None
            else:
                self.tail   =   self.tail.prev
                self.tail.next  =   None
        else:
            node.prev.next  =   node.next
            node.next.prev  =   node.prev
        self.size       -=  1
        del self.hash[node.key]

    def print_link(self):
        if self.head:
            temp    =   self.head
            print(str(temp.value)+'->', end =" ")
            temp = temp.next
            while(temp and temp is not self.head):
                print(str(temp.value)+'->', end =" ")
                temp    =   temp.next
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)