from data_structures.node import LinkedListNode


class LinkedList:
    """
    A singly linked list data structure.

    A linked list is a linear data structure where each element is a node
    that contains a value and a reference to the next node.

    Attributes:
        head: The first node in the linked list.
        tail: The last node in the linked list.
        length: The number of nodes in the linked list.
    """

    def __init__(self, value: int):
        """
        Initializes a linked list with a single node.

        Args:
            value: The integer value for the initial node.
        """
        node = LinkedListNode(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def append(self, value: int) -> bool:
        """
        Appends a new node with the given value to the end of the list.

        Args:
            value: The integer value to append to the list.

        Returns:
            True if the node was successfully appended.
        """
        new_node = LinkedListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> LinkedListNode:
        """
        Removes and returns the last node from the list.

        Returns:
            The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None

        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self.length -= 1
        return pop_node

    def prepend(self, value: int):
        """
        Prepends a new node with the given value to the beginning of the list.

        Args:
            value: The integer value to prepend to the list.

        Returns:
            True if the node was successfully prepended.
        """
        new_node = LinkedListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> LinkedListNode:
        """
        Removes and returns the first node from the list.

        Returns:
            The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None

        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_head = self.head.next
            self.head.next = None
            self.head = temp_head
        self.length -= 1
        return pop_node

    def get(self, index: int) -> LinkedListNode:
        """
        Retrieves the node at the specified index.

        Args:
            index: The zero-based index of the node to retrieve.

        Returns:
            The node at the specified index, or None if the index is out of bounds.
        """
        if 0 <= index < self.length:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            return temp_node
        return None

    def set_value(self, index: int, value: int) -> bool:
        """
        Sets the value of the node at the specified index.

        Args:
            index: The zero-based index of the node to update.
            value: The new integer value to set.

        Returns:
            True if the value was successfully set, False if the index is out of bounds.
        """
        target_node = self.get(index)
        if target_node is not None:
            target_node.value = value
            return True
        return False

    def insert(self, index: int, value: int) -> bool:
        """
        Inserts a new node with the given value at the specified index.

        Args:
            index: The zero-based index where the new node should be inserted.
            value: The integer value for the new node.

        Returns:
            True if the node was successfully inserted, False if the index is out of bounds.
        """
        if 0 <= index <= self.length:
            previous_node = self.get(index - 1)
            if previous_node is None:
                return self.prepend(value)
            if previous_node.next is None:
                return self.append(value)
            new_node = LinkedListNode(value)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.length += 1
            return True
        return False

    def remove(self, index: int) -> LinkedListNode:
        """
        Removes and returns the node at the specified index.

        Args:
            index: The zero-based index of the node to remove.

        Returns:
            The removed node, or None if the index is out of bounds.
        """
        if 0 <= index <= self.length:
            previous_node = self.get(index - 1)
            if previous_node is None:
                return self.pop_first()
            if previous_node.next is None:
                return self.pop()
            target_node = previous_node.next
            previous_node.next = target_node.next
            target_node.next = None
            self.length -= 1
            return target_node
        return None

    def reverse(self):
        """
        Reverses the linked list in place.

        The head becomes the tail and the tail becomes the head.
        All node references are reversed.
        """
        prev_tmp = None
        current = self.head

        while current:
            next_tmp = current.next
            current.next = prev_tmp
            prev_tmp = current
            current = next_tmp
        
        self.tail = self.head
        self.head = prev_tmp

    def remove_duplicates(self) -> LinkedListNode:
        """
        Removes duplicate values from the linked list, keeping only the first occurrence.

        Modifies the list in place by adjusting node references.

        Returns:
            The head node of the modified list, or None if the list is empty.
        """
        if not self.head:
            return None
        
        seen_values = {self.head.value}
        current = self.head

        while current.next:
            if current.next.value in seen_values:
                current.next = current.next.next
            else:
                seen_values.add(current.next.value)
                current = current.next

        self.tail = current

    def print_list(self):
        """
        Prints all values in the linked list.

        Values are printed one per line, preceded by a separator line.
        """
        temp_node = self.head
        output = ""        
        while temp_node is not None:
            output += f"{temp_node.value} -> "
            temp_node = temp_node.next
        print(output)

    def reverse_between(self, start: int, end: int):
        """
        Reverses a portion of the linked list between two indices.

        Reverses the nodes from start to end (inclusive) in place.

        Args:
            start: The zero-based starting index of the range to reverse.
            end: The zero-based ending index of the range to reverse.

        Returns:
            None if the list is empty or has fewer than 2 nodes, otherwise modifies
            the list in place.
        """
        if not self.head or start >= end or start < 0:
            return

        dummy = LinkedListNode(0)
        dummy.next = self.head
        prev = dummy

        # Move prev to the node BEFORE start index — but don't go past the end
        for _ in range(start):
            if not prev.next:      # Safety: stop if we've reached the end
                return
            prev = prev.next

        # The node at index 'start' will become the new tail if reversal reaches end
        new_tail_candidate = prev.next

        current = prev.next
        for _ in range(end - start):
            if not current or not current.next:
                break
            node = current.next
            current.next, node.next, prev.next = node.next, prev.next, node

        self.head = dummy.next

        # Only update tail if the reversed section included the original tail
        if end >= self.length - 1:
            self.tail = new_tail_candidate
