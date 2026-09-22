class Node:
    def __init__(self, key, value, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_length = 0

        self.head = None       # LRU
        self.last = None       # MRU

        self.ref_dict = {}

    def move_to_last(self, node):

        # Already the most recently used
        if node == self.last:
            return

        # Remove node from current position

        if node == self.head:
            self.head = node.nxt
            self.head.prev = None
        else:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev

        # Put node at the end

        node.prev = self.last
        node.nxt = None

        self.last.nxt = node
        self.last = node


    def get(self, key: int) -> int:

        if key not in self.ref_dict:
            return -1

        node = self.ref_dict[key]

        self.move_to_last(node)

        return node.value


    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.ref_dict:

            node = self.ref_dict[key]

            node.value = value

            self.move_to_last(node)

            return

        # Cache is full → remove LRU
        if self.curr_length == self.capacity:

            lru = self.head

            del self.ref_dict[lru.key]

            self.head = lru.nxt

            if self.head:
                self.head.prev = None
            else:
                self.last = None

            self.curr_length -= 1

        # Create new node
        new_node = Node(key, value)

        self.ref_dict[key] = new_node

        # Empty cache
        if self.last is None:

            self.head = new_node
            self.last = new_node

        else:

            new_node.prev = self.last
            self.last.nxt = new_node
            self.last = new_node

        self.curr_length += 1