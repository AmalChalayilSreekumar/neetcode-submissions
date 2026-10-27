class Node:
    """
    A node in a doubly linked list.

    Each node stores one cache entry (key + value) plus pointers to its
    neighbours. We store the key inside the node (not just the value) because
    when we evict the least recently used node, we need to know its key so we
    can also delete it from the hash map.
    """

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None  # node closer to the LRU end
        self.next = None  # node closer to the MRU end


class LRUCache:
    """
    LRU (Least Recently Used) cache with O(1) get and put.

    Idea: combine two data structures, each covering the other's weakness.

      1. Hash map  (key -> Node):  O(1) lookup by key, but has no ordering.
      2. Doubly linked list:       keeps nodes ordered by recency of use, and
                                   lets us remove / insert a node in O(1) as
                                   long as we already have a pointer to it.

    List layout (the two sentinel nodes are dummies that never hold real data):

        head <-> [LRU] <-> ... <-> ... <-> [MRU] <-> tail

      - The node right after `head` is the LEAST recently used (evict first).
      - The node right before `tail` is the MOST recently used.

    Using sentinel nodes means we never have to handle special cases like
    "the list is empty" or "we're removing the first/last node", because every
    real node always has a real neighbour on both sides.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Maps key -> Node, so we can jump straight to a node in O(1).
        self.map = {}

        # Sentinel nodes: they mark the two ends of the list.
        self.head = Node()  # head.next is the least recently used node
        self.tail = Node()  # tail.prev is the most recently used node

        # Start with an empty list: head and tail point at each other.
        self.head.next = self.tail
        self.tail.prev = self.head

    # ------------------------------------------------------------------
    # Helper methods for the linked list. Each one is O(1).
    # ------------------------------------------------------------------

    def _remove(self, node: Node) -> None:
        """Unlink `node` from wherever it currently sits in the list."""
        prev_node = node.prev
        next_node = node.next

        # Make the neighbours point at each other, skipping over `node`.
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_end(self, node: Node) -> None:
        """Insert `node` just before `tail`, marking it as most recently used."""
        last = self.tail.prev  # the current most recently used node

        # Wire node in between `last` and `tail`.
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get(self, key: int) -> int:
        """
        Return the value for `key`, or -1 if it isn't in the cache.

        A successful get counts as "using" the key, so we move its node to the
        most recently used end of the list.
        """
        # Cache miss: nothing to return and nothing to reorder.
        if key not in self.map:
            return -1

        node = self.map[key]

        # Cache hit: this key is now the most recently used.
        # Pull the node out of its current position and re-add it at the end.
        self._remove(node)
        self._add_to_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update `key` with `value`.

        If inserting a new key pushes us over capacity, evict the least
        recently used entry first.
        """
        # Edge case: a cache with no capacity can't store anything.
        # Without this guard, the eviction step below would try to evict
        # the `tail` sentinel from an empty list and crash.
        if self.capacity <= 0:
            return

        # Case 1: key already exists -> update its value and refresh recency.
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_end(node)
            return

        # Case 2: brand new key. If the cache is full, make room first.
        if len(self.map) >= self.capacity:
            lru = self.head.next     # least recently used node
            self._remove(lru)
            del self.map[lru.key]

        # Create the new node and make it the most recently used.
        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_to_end(new_node)