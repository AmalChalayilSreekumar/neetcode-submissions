class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hash map that maps each old node to its copy.
        # We seed it with None -> None so that when a node's next or random
        # pointer is None, looking it up gives None instead of a KeyError.
        # This also handles an empty list, since head would be None.
        oldToCopy = {None: None}

        # Make a current pointer that starts at the head of the original list
        curr = head

        # Iterate through the original linked list and create a copy of every node. Just the val not any
        # of the pointers yet

        while curr:
            # Make a new node with the same value as the current node
            copy = Node(curr.val)
            # Store the pairing so we can find this copy from the old node later
            oldToCopy[curr] = copy
            # Move on to the next node in the original list
            curr = curr.next

        # Reset curr to head to iterate through list again
        curr = head

        # Second pass to set the pointers
        while curr:
            # Grab the copy that corresponds to the current original node
            copy = oldToCopy[curr]
            # The copy's next should be the COPY of the original's next node
            copy.next = oldToCopy[curr.next]
            # The copy's random should be the COPY of the original's random node
            # (not the original random node, or we'd be linking into the old list)
            copy.random = oldToCopy[curr.random]
            # Move on to the next node in the original list
            curr = curr.next

        # The head of the copied list is the copy of the original head
        # (this is None if the original list was empty)
        return oldToCopy[head]