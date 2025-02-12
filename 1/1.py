class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Функція для реверсування списку
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    # Функція для сортування вставками
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self.head = sorted_list

    # Функція для об'єднання двох відсортованих списків
    def merge_sorted_lists(self, list2):
        p1 = self.head
        p2 = list2.head
        merged_list = LinkedList()
        
        while p1 and p2:
            if p1.data < p2.data:
                merged_list.insert_at_end(p1.data)
                p1 = p1.next
            else:
                merged_list.insert_at_end(p2.data)
                p2 = p2.next
        
        # Якщо один список ще не порожній, додаємо його елементи
        while p1:
            merged_list.insert_at_end(p1.data)
            p1 = p1.next
            
        while p2:
            merged_list.insert_at_end(p2.data)
            p2 = p2.next
        
        return merged_list
    
llist1 = LinkedList()
llist1.insert_at_end(10)
llist1.insert_at_end(20)
llist1.insert_at_end(5)
llist1.insert_at_end(30)

llist2 = LinkedList()
llist2.insert_at_end(15)
llist2.insert_at_end(25)

print("До сортування:")
llist1.print_list()

llist1.insertion_sort()
print("\nПісля сортування:")
llist1.print_list()

merged_list = llist1.merge_sorted_lists(llist2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()

print("\nРеверсований список:")
llist1.reverse()
llist1.print_list()