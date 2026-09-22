class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # initialize dummy nodes for left and rightmost nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right
    
    # insert node at the right of the list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    # remove node from anywhere in the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        '''
        - Just remove the k-v if it exists then add the new k-v
        - if addition of new k-v exceeds cap size, remove LRU
        '''
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
        
        
