class Node(object):
    
    def __init__(self, data=None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, next):
        self._next = next
    pass
    

class SinglyLinkedList(object):
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._num_nodes = 0
        pass
        
    def __str__(self):
        if self.empty():
            return 'Singly Linked List is empty'
        curr_node = self._head
        str_ = ''
        while curr_node.next != None:
            str_ += str(curr_node.data) + '->'
            curr_node = curr_node.next
        str_ += str(curr_node.data) + '-> None'
        return str_
        pass

    def __len__(self):
        return self._num_nodes
        pass 
            
    def empty(self):
        return self._num_nodes == 0
        pass
        
    def insert(self, i, data):
        if i < 0 or i > self._num_nodes:
            raise IndexError("Invalid index")

        new_node = Node(data)
        if i == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            curr_node = self._head
            for _ in range(i-1):
                curr_node = curr_node.next
            if curr_node.next is not None:
                new_node.next = curr_node.next
            curr_node.next = new_node
        self._num_nodes += 1

        self._adjust_tail()

        pass

    def _adjust_tail(self):
        if self.empty():
            self._tail = None
        else:
            curr = self._head
            for _ in range(self._num_nodes - 1):
                curr = curr.next
            self._tail = curr

    def remove(self, i):
        if self.empty():
            return 
        if i < 0 or i >= len(self):
            raise IndexError("pop index out of range")
        if i == 0:
            self._head = self._head.next
            self._num_nodes -= 1
            self._adjust_tail()
            return
        node = self._head
        for j in range(i-1):
            if node.next is None:
                raise IndexError("pop index out of range")
            node = node.next
        node.next = node.next.next
        self._num_nodes -= 1
        self._adjust_tail()
        pass
              
    def clear(self):
        node = self._head
        while node is not None:
            next_node = node.next
            node.next = None
            node = next_node
        self._head = None
        self._tail = None
        self._num_nodes = 0
        pass
    
    def get(self, i):
        if i < 0 or i >= self._num_nodes:
            raise IndexError("SinglyLinkedList index out of range")
        
        curr = self._head
        for _ in range(i):
            curr = curr.next
        
        return curr.data
        pass
    
    def pop(self, i=None):
        if self._num_nodes == 0:
            raise IndexError("pop from empty SinglyLinkedList")
        if i is None:
            i = self._num_nodes - 1

        if i < 0 or i >= self._num_nodes:
            raise IndexError("pop index out of range")

        if i == 0:
            data = self._head.data
            self._head = self._head.next
            if self._num_nodes == 1:
                self._tail = None
            self._num_nodes -= 1
            return data

        prev_node = self._head
        for j in range(i-1):
            prev_node = prev_node.next

        data = prev_node.next.data
        if i == self._num_nodes - 1:
            prev_node.next = None
            self._tail = prev_node
        else:
            prev_node.next = prev_node.next.next
        self._num_nodes -= 1
        return data
        pass
    
    def search(self, target, start=0):
        if self._num_nodes == 0:
            raise IndexError("SinglyLinkedList is empty")

        if start < 0 or start >= self._num_nodes:
            raise IndexError("start index out of range")

        current_node = self._head
        i = 0
        while i < start:
            current_node = current_node.next
            i += 1

        while current_node is not None:
            if current_node.data == target:
                return current_node.data, i
            current_node = current_node.next
            i += 1

        return None, -1
        pass

    def extend(self, sll):
        if not isinstance(sll, SinglyLinkedList):
            raise TypeError("Argument should be a SinglyLinkedList object.")
        
        # if sll.empty():
        #     return
        
        # if self.empty():
        #     self._head = sll._head
        #     self._tail = sll._tail
        #     self._num_nodes = sll._num_nodes
        #     return
        
        # self._tail.next = sll._head
        # self._tail = sll._tail
        # self._num_nodes += sll._num_nodes

        for i in range(sll._num_nodes):
            self.insert(self._num_nodes, sll.get(i))

        pass 


# def test():
#     linked_list = SinglyLinkedList()

#     linked_list.insert(0, 1)
#     linked_list.insert(1, 2)
#     linked_list.insert(2, 3)
#     linked_list.insert(3, 4)

#     print(linked_list)
#     print(linked_list._tail.data)

#     linked_list2 = SinglyLinkedList()

#     linked_list2.insert(0, 5)
#     linked_list2.insert(1, 6)
#     linked_list2.insert(2, 7)
#     linked_list2.insert(3, 8)

#     print(linked_list2)
#     print(linked_list2._tail.data)

#     linked_list.extend(linked_list2)
#     print(linked_list)
#     print(linked_list._tail.data)

#     linked_list2.insert(3, 9)

#     print(linked_list)
#     print(linked_list._tail.data)






if __name__ == "__main__":
    test()