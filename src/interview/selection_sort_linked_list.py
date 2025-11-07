"""
Selection Sort of LL ( ** Interview Question)

Assignment:
Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order
 using the selection sort algorithm. The method should update the head and tail pointers of the linked list to reflect 
 the new order of the nodes in the list. You can assume that the input linked list will contain only integers. 
 You should not use any additional data structures to sort the linked list.

Note:
This Linked List does not have a tail pointer, which will make the method more straightforward to implement since you 
will not need to reassign the tail at the end.

Input:
The LinkedList object containing a linked list with unsorted elements (self).

Output:
None. The method sorts the linked list in place.

Method Description:
If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.
The selection sort algorithm works by repeatedly finding the smallest element in the unsorted part of the list and 
swapping it with the first element in the unsorted part of the list. The method starts with the entire linked list 
being the unsorted part of the list. For each pass through the unsorted part of the list, the method iterates through 
each element to find the smallest element in the unsorted part of the list. Once the smallest element is found, it is 
swapped with the first element in the unsorted part of the list. After each pass, the smallest element in the unsorted
part of the list will be at the beginning of the unsorted part of the list. The method continues iterating through the 
unsorted part of the list until the entire list is sorted. After the linked list is fully sorted, the head and tail 
pointers of the linked list are updated to reflect the new order of the nodes in the list.

Constraints:
- The linked list can contain duplicates.
- The method should be implemented in the LinkedList class.
- The method should not use any additional data structures to sort the linked list.

"""

from data_structures.linked_list import LinkedList


class SelectionSortLL(LinkedList):
    def __init__(self, value: int):
        super().__init__(value)
    
    def selection_sort(self):
        if self.length <= 1:
            return None
        current_node = self.head
        while current_node.next is not None:
            smallest_node = current_node
            inner_current_node = current_node.next
            while inner_current_node is not None:
                if inner_current_node.value < smallest_node.value:
                    smallest_node = inner_current_node
                inner_current_node = inner_current_node.next
            if smallest_node != current_node:
                smallest_node.value, current_node.value = current_node.value, smallest_node.value
            current_node = current_node.next

        # update head and tail
        current = self.head
        while current.next is not None:
            current = current.next
        self.tail = current


# Test Cases:
# -----------------------------------

# Test 1: Empty list
print("Test 1: Empty list")
ll1 = SelectionSortLL(5)
ll1.head = None
ll1.length = 0
ll1.selection_sort()
ll1.print_list()  # Should print: empty 
print("-" * 30)

# Test 2: Single element
print("Test 2: Single element")
ll2 = SelectionSortLL(5)
ll2.selection_sort()
ll2.print_list()  # Should print: 5
print("-" * 30)

# Test 3: Already sorted list
print("Test 3: Already sorted list")
ll3 = SelectionSortLL(1)
ll3.append(2)
ll3.append(3)
ll3.selection_sort()
ll3.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 4: Reverse order
print("Test 4: Reverse order")
ll4 = SelectionSortLL(3)
ll4.append(2)
ll4.append(1)
ll4.selection_sort()
ll4.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 5: Random order
print("Test 5: Random order")
ll5 = SelectionSortLL(2)
ll5.append(1)
ll5.append(3)
ll5.selection_sort()
ll5.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 6: List with duplicates
print("Test 6: List with duplicates")
ll6 = SelectionSortLL(3)
ll6.append(2)
ll6.append(2)
ll6.append(1)
ll6.append(3)
ll6.selection_sort()
ll6.print_list()  # Should print: 1 -> 2 -> 2 -> 3 -> 3
print("-" * 30)
