class MyHashMap:

    def __init__(self):
        self.size = 0
        self.data = [None] * 10000

    def put(self, key: int, value: int) -> None:
        _, c = self.lookup(key)
        if c is not None:
            c.val = value
            return

        self.size += 1
        # if self.size * 2 > len(self.data):
        #     self.resize(len(self.data) * 2)
        self.add_node(HashMapNode(key=key, val=value))
    
    def get(self, key: int) -> int:
        _, c = self.lookup(key)
        if c is not None:
            return c.val
        return -1
    
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
        if self.data[i].key == key:
            return None, self.data[i]
        else:
            curr = self.data[i]
            while curr.next is not None:
                if curr.next.key == key:
                    return curr, curr.next
                curr = curr.next
            return None, None
            
    def resize(self, n):
        resized_data = [None] * n
        for node in self.data:
            if node is None:
                continue
            curr = node
            while curr is not None:
                self.add_node(curr, resized_data)
                curr = curr.next
        self.data = resized_data

    def add_node(self, node, data=None):
        if data is None:
            data = self.data
        i = self.index(node.key, len(data))
        node.next = data[i]
        data[i] = node
    
    def index(self, key, n=None):
        if n is None:
            n = len(self.data)
        return hash(key) % n


class HashMapNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

