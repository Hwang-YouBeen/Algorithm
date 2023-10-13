class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self._data = data
        self._left = left
        self._right = right
        self._parent = parent

    def __str__(self):
        return "Node({})".format(self._data)
    
    def __repr__(self):
        return str(self)

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, value):
        self._right = value

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, value):
        self._parent = value

    def count_children(self):
        count = 0
        if self._left is not None:
            count += 1
        if self._right is not None:
            count += 1
        return count
    
    def children(self):
        children = []
        if self._left is not None:
            children.append(self._left)
        if self._right is not None:
            children.append(self._right)
        return children
        pass


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._num_nodes = 0
        pass
    
    def __len__(self):
        return self._num_nodes
        pass
    
    def empty(self):
        return self._num_nodes == 0
        pass
    
    def insert(self, data):
        if self._root is None:
            self._root = Node(data)
        else:
            self._insert_recursive(self._root, data)
        self._num_nodes += 1

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                node.left.parent = node
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
                node.right.parent = node
            else:
                self._insert_recursive(node.right, data)       
        pass
    
    def inorder(self, get_node=False):
        traversal = []
        self._inorder_recursive(self._root, traversal, get_node)
        return traversal

    def _inorder_recursive(self, node, traversal, get_node):
        if node:
            self._inorder_recursive(node.left, traversal, get_node)
            if get_node:
                traversal.append(node)
            else:
                traversal.append(node.data)
            self._inorder_recursive(node.right, traversal, get_node)    
        pass
    
    def preorder(self, get_node=False):
        traversal = []
        self._preorder_recursive(self._root, traversal, get_node)
        return traversal
    
    def _preorder_recursive(self, node, traversal, get_node):
        if node:
            if get_node:
                traversal.append(node)
            else:
                traversal.append(node.data)
            self._preorder_recursive(node.left, traversal, get_node)
            self._preorder_recursive(node.right, traversal, get_node)
        pass
    
    def postorder(self, get_node=False):
        traversal = []
        self._postorder_recursive(self._root, traversal, get_node)
        return traversal

    def _postorder_recursive(self, node, traversal, get_node):
        if node:
            self._postorder_recursive(node.left, traversal, get_node)
            self._postorder_recursive(node.right, traversal, get_node)
            if get_node:
                traversal.append(node)
            else:
                traversal.append(node.data)
        pass
    
    def min(self, root=None, get_node=False):
        if root is None:
            root = self._root
        if root is None:
            return None
        
        node = root
        while node.left:
            node = node.left
        
        if get_node:
            return node
        else:
            return node.data
        pass
    
    def max(self, root=None, get_node=False):
        if root is None:
            root = self._root
        if root is None:
            return None
        
        node = root
        while node.right:
            node = node.right
        
        if get_node:
            return node
        else:
            return node.data
        pass       
        
    def search(self, data):
        if self.empty():
            raise IndexError("BinarySearchTree is empty.")

        node = self._root
        while node:
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        
        return None
        pass
    
    def remove(self, data):
        node = self.search(data)
        if node is None:
            return None

        if self._num_nodes == 1:
            self._root = None
            self._num_nodes = 0
            return node

        parent = node.parent

        if node.left and node.right:
            successor = self._get_successor(node)
            node.data = successor.data
            self._remove_subtree(successor)
        else:
            self._remove_subtree(node)

        self._num_nodes -= 1
        return node

    def _get_successor(self, node):
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor

    def _remove_subtree(self, node):
        parent = node.parent

        if node.left:
            child = node.left
        else:
            child = node.right

        if parent:
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child
        else:
            self._root = child

        if child:
            child.parent = parent

        node.left = None
        node.right = None
        node.parent = None


    
    
    def clear(self):
        self._postorder_clear(self._root)
        self._root = None
        self._num_nodes = 0
    
    def _postorder_clear(self, node):
        if node:
            self._postorder_clear(node.left)
            self._postorder_clear(node.right)
            node.left = None
            node.right = None
            node.parent = None
        pass