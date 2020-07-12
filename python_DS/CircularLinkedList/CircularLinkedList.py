class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove_node(self, key):
        if self.head:
            # if key matches to the head node
            if self.head.data == key:
                cur = self.head
                # loop to iterate to last node
                while cur.next != self.head:
                    cur = cur.next
                # if list contains only one node
                if self.head == self.head.next:
                    self.head = None
                # if there are other nodes
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            # if key matches to other than head node
            else:
                cur = self.head
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    # here we are using __len__ to override the original len() method
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        # we will iterate through remaining list as cur is holding the next node i.e 1st node of 2nd split list
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        # to append data of last node
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self,step):
        cur = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("KILL: " + str(cur.data))
            self.remove_node(cur)
            cur = cur.next

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False


cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
#
# cllist.remove_node("C")
# cllist.print_list()
# print(cllist.__len__())

# cllist.append("A")
# cllist.append("B")
# cllist.append("C")
# cllist.append("D")
# cllist.append("E")
# cllist.append("F")
# cllist.split_list()

# cllist.append(1)
# cllist.append(2)
# cllist.append(3)
# cllist.append(4)
# cllist.josephus_circle(1)
# cllist.print_list()

cllist2 = CircularLinkedList()
cllist2.append(1)
cllist2.append(2)
cllist2.append(3)
cllist2.append(4)
print(cllist.is_circular_linked_list(cllist2))
print(cllist.is_circular_linked_list(cllist))