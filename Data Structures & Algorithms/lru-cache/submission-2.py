class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.nodes:
            self._move_to_end(self.nodes[key])
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self._move_to_end(self.nodes[key])
        else:
            if len(self.nodes) == self.capacity:
                self._remove_head()
            self._add_to_tail(key, value)
        
    def _move_to_end(self, node):
        if node != self.tail:
            if node == self.head:
                self.head = node.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None
    
    def _remove_head(self):
        key = self.head.key

        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        
        del self.nodes[key]

    def _add_to_tail(self, key, val):
        node = self.Node(key, val)
        if self.tail is not None:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = node
        self.nodes[key] = node

    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev