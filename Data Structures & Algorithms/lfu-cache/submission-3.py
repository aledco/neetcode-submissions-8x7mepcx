import heapq

from collections import defaultdict

DEBUG = False

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = {}
        
        # idea: maintain a map of linked lists. The keys of the map are use counters, and the linked lists are the nodes. linked lists are in order of recencty
        # also maintain the smallest use counter

        self.lists = defaultdict(LFUList)
        self.min_uses = 0

    def __str__(self):
        res = "LFUCache(\n"
        res += f"\tcap={self.cap},\n"
        res += f"\tmin_uses={self.min_uses},\n"
        res += "\tlists=(\n"
        for k, l in self.lists.items():
            res += f"\t\t{k}: {l},\n"
        res += "\t)\n"
        res += ")"
        return res
        

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        
        if DEBUG:
            print(f"get({key})")
            print("BEFORE")
            print(self)

        node = self.data[key]
        self.incrementUses(node)

        if DEBUG:
            print("AFTER")
            print(self)
            print()

        return node.val

    def put(self, key: int, value: int) -> None:
        if DEBUG:
            print(f"put({key}, {value})")
            print("BEFORE")
            print(self)

        if key in self.data:
            node = self.data[key]
            node.val = value
            self.incrementUses(node)
        else:
            if len(self.data) == self.cap:
                self.pop()

            node = ListNode(key=key, val=value, uses=1)
            self.data[key] = node
            self.lists[1].addToBack(node)
            self.min_uses = 1
        
        if DEBUG:
            print("AFTER")
            print(self)
            print()

    def incrementUses(self, node: 'ListNode') -> None:
        # remove node from current linked list
        self.lists[node.uses].remove(node)

        # insert node at the back of the next list
        node.uses += 1
        self.lists[node.uses].addToBack(node)

        # check if min_uses needs to be updated
        if self.lists[self.min_uses].isEmpty():
            self.min_uses += 1
            # self.updateMinUses()

        

    # def updateMinUses(self):
    #     import sys
    #     self.min_uses = sys.maxsize
    #     for uses, L in self.lists.items():
    #         if not L.isEmpty():
    #             self.min_uses = min(self.min_uses, uses)
        
    def pop(self):
        assert not self.lists[self.min_uses].isEmpty(), "min_uses points to empty list"
        popped = self.lists[self.min_uses].popFront()
        del self.data[popped.key]


class LFUList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
    
    def __str__(self):
        res = str(self.head)
        curr = self.head.next
        while curr is not None:
            res += " -> " + str(curr)
            curr = curr.next
        return res
    
    def addToBack(self, node):
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def popFront(self):
        node = self.head.next
        if node is None:
            return None
        self.remove(node)
        return node

    def remove(self, node):
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            temp = node.next
            node.prev.next = temp
            temp.prev = node.prev
        node.prev = node.next = None

    def isEmpty(self):
        return self.head.next is None

class ListNode:
    def __init__(self, key=None, val=None, uses=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.uses = uses
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return f"ListNode(key={self.key}, val={self.val}, uses={self.uses})"

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)