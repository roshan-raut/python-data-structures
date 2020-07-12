class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.prev = None
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_node_after(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.pre = cur
                nxt.prev = new_node
                return
            cur = cur.next

    def add_node_before(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node= Node(data)
                prv = cur.prev
                prv.next = new_node
                new_node.next = cur
                new_node.prev = prv
                cur.prev = new_node
                return
            cur = cur.next

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # case1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # case2:
                else:
                    nxt = cur.next
                    cur.next = None
                    cur.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # case3:
                if cur.next:
                    nxt = cur.next
                    prv = cur.prev
                    prv.next = nxt
                    nxt.prev = prv
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # case4:
                else:
                    prv = cur.prev
                    prv.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def remove_duplicates(self):
        cur = self.head
        duplicates = dict()
        while cur:
            if cur.data in duplicates:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
            else:
                duplicates[cur.data] = 1
                cur = cur.next

    def pairs_with_sum(self, sum_value):
        tmp = self.head
        sum_list = []
        while tmp:
            cur = tmp.next
            while cur:
                if (tmp.data + cur.data) == sum_value:
                    result = "("+str(tmp.data)+","+str(cur.data)+")"
                    sum_list.append(result)
                cur = cur.next
            tmp = tmp.next
        return sum_list

dllist = DoublyLinkedList()
# dllist.prepend(0)
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
# dllist.prepend(5)
# dllist.add_node_after(3,6)
# dllist.add_node_before(4,9)

# dllist.delete(5)
# dllist.delete(3)
# dllist.delete(4)
# dllist.delete(10)

# dllist.reverse()
# dllist.print_list()

# dllist.append(8)
# dllist.append(4)
# dllist.append(4)
# dllist.append(6)
# dllist.append(4)
# dllist.append(8)
# dllist.append(4)
# dllist.append(10)
# dllist.append(12)
# dllist.append(12)
#
# dllist.remove_duplicates()
# dllist.print_list()

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(dllist.pairs_with_sum(5))