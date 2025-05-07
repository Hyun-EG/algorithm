class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 링크드 리스트 원소 찾기
    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # 링크드 리스트 해당 index에 원소 추가
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        prev_node = self.get_node(index-1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

    # 링크드 리스트 해당 index의 원소 제거
    def delete_node(self, index):
        delete_index = self.get_node(index)
        next_index = delete_index.next
        if index == 0:
            self.head = self.head.next
            return
        prev_index = self.get_node(index-1)
        prev_index.next = next_index

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.delete_node(0)
linked_list.print_all()
