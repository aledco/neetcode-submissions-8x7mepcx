class RandomizedSet:

    def __init__(self):
        self.data = ListNode()
        self.pointers = {}

    def insert(self, val: int) -> bool:
        if val in self.pointers:
            return False
        
        node = ListNode(val, self.data.next, self.data)
        if node.next:
            node.next.prev = node
        self.data.next = node
        self.pointers[val] = node
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pointers:
            return False
        
        node = self.pointers[val]
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        del self.pointers[node.val]        
        del node
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(list(self.pointers.keys()))


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()