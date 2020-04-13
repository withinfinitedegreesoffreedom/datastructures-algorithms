class node: 
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def display(self):
        elems = []
        cur = self.head
        while cur != None:   
            elems.append(cur.data)        
            cur = cur.next            
        return elems

    def get(self, index):
        if index >= self.length():
            print("Index out of bounds")
            return 
        i = 0
        cur = self.head
        while True:
            if index == i:
                return cur.data
            cur = cur.next
            i += 1            

    def insert(self, data, index):
        if index >= self.length():
            print("Index out of bounds")
            return 
        idx = 0
        cur = self.head
        while True: 
            prev = cur
            cur = cur.next
            if idx == index:
                new_node = node(data)
                prev.next = new_node
                prev = prev.next
                prev.next = cur
                return 
            idx += 1


    def remove(self, index):
        if index >= self.length():
            print("Index out of bounds")
            return
        idx = 0
        cur = self.head
        if idx == index:
            self.head = cur.next
            return
        while True:
            if idx == index:
                prev.next = cur.next
                return 
            prev = cur
            cur = cur.next
            idx += 1

    def kthtolast(self, k):
        fast = self.head
        slow = self.head

        n = 1
        while fast.next != None:
            fast = fast.next 
            if n > k:
                slow = slow.next
            n += 1
        return slow.data

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def node_swap(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 is not None and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 is not None and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def merge_sorted_list(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p.data <= q.data: 
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p
        
        return new_head
            
    def count_elem(self, elem):
        cur = self.head
        if not cur:
            return 0
        count = 0
        while cur:
            if cur.data == elem:
                count += 1
            cur = cur.next 
        return count        

    def count_elem_recursive(self, node, elem):
        if not node:
            return 0
        if node.data == elem:
            return 1 + self.count_elem_recursive(node.next, elem)
        else:
            return self.count_elem_recursive(node.next, elem)

    def rotate(self, pivot):
        if not self.head:
            return
        p = self.head
        q = self.head
        while p and q:
            if p.data == pivot and q.data == pivot:
                while q.next:
                    q = q.next
                q.next = self.head
                self.head = p.next
                p.next = None
                return self.head
            p = p.next
            q = q.next
        return p

    def tail_to_head(self):
        if self.head is None:
            return
        p = self.head
        prev = None
        while p.next:
            prev = p
            p = p.next
        prev.next = None            
        p.next = self.head
        self.head = p
        return p








my_list = linkedlist()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print(my_list.display())
print(my_list.length())
print(my_list.get(2))
my_list.remove(0)
print(my_list.display())
print(my_list.length())
my_list.insert(3, 0)
my_list.insert(3, 1)
my_list.insert(4, 4)
print(my_list.display())
print(my_list.kthtolast(0))
my_list.reverse()
print(my_list.display())
my_list.node_swap(2, 5)
print(my_list.display())

'''# remove duplicates 
hashmap = {}
cur = my_list.head
while cur.next != None:
    prev=cur
    cur=cur.next
    if cur.data not in hashmap.keys():
        hashmap[cur.data] = 1
    else:
        prev.next = cur.next
    
print(my_list.display())
my_list.reverse()
print(my_list.display())


my_list_1 = linkedlist()
my_list_1.append(7)
my_list_1.append(1)
my_list_1.append(6)

my_list_2 = linkedlist()
my_list_2.append(5)
my_list_2.append(9)
my_list_2.append(2)

# addition
added_list = linkedlist()
p1 = my_list_1.head
p2 = my_list_2.head
c = 0
while p1.next != None:
    s = p1.next.data + p2.next.data + c
    if s > 10:
        s = s % 10
        c = 1
    added_list.append(s)
    p1 = p1.next
    p2 = p2.next
print(added_list.display())'''

llist_1 = linkedlist()
llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2 = linkedlist()
llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

print(llist_1.display())
print(llist_2.display())

llist_1.merge_sorted_list(llist_2)
print(llist_1.display())

llist_1.tail_to_head()
print(llist_1.display())

'''llist = linkedlist()
llist.append(0)
llist.append(4)
llist.append(0)
llist.append(1)
llist.append(3)
llist.append(2)
llist.append(0)
print(llist.count_elem(1))
print(llist.count_elem_recursive(llist.head, 1))'''

llist_1.rotate(5)
print(llist_1.display())