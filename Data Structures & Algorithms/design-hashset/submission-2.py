class MyHashSet:

    def __init__(self):
        self.size = 0
        self.data = []
        self.resize(10000)

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.size += 1
        if self.size * 2 > len(self.data):
            self.resize(self.size * 4)
        self.add_node(HashSetNode(val=key))

    def remove(self, key: int) -> None:
        p, c = self.lookup(key)
        if c is None:
            return
        
        i = self.index(key)
        if p is None:
            self.data[i] = c.next
        else:
            p.next = c.next
            
        self.size -= 1
        # if self.size * 4 < len(self.data):
        #     self.resize(max(self.size * 2, 16))

    def contains(self, key: int) -> bool:
        _, c = self.lookup(key)
        return c is not None
    
    def lookup(self, key):
        i = self.index(key)
        if self.data[i] is None:
            return None, None
        if self.data[i].val == key:
            return None, self.data[i]
        else:
            curr = self.data[i]
            while curr.next is not None:
                if curr.next.val == key:
                    return curr, curr.next
                curr = curr.next
            return None, None
            
    def resize(self, n):
        resized_data = [None] * n
        for node in self.data:
            if node is not None:
                curr = node
                while curr is not None:
                    self.add_node(curr, resized_data)
                    curr = curr.next
        self.data = resized_data

    def add_node(self, node, data=None):
        if data is None:
            data = self.data
        i = self.index(node.val, len(data))
        node.next = data[i]
        data[i] = node
    
    def index(self, key, n=None):
        if n is None:
            n = len(self.data)
        return hash(key) % n


class HashSetNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)