'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/11/7 10:10 
'''


# class ListNode:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def create(self, data):
#         self.head = ListNode(0)
#         cur = self.head
#         for i in range(len(data)):
#             node = ListNode(data[i])
#             cur.next = node
#             cur = cur.next

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# 定义单链表类
class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        # 判断链表是否为空
        return self.__head == None

    def length(self):
        # 链表长度
        cur = self.__head  # cur用来移动遍历节点
        count = 0  # count 记录数量
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历整个链表
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        # 链表头部添加元素
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        # 链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        # 在指定位置添加元素
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            # 不需要包含等号
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # while循环退出，pre指到pos前一个位置，也就是插入的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):

        # 删除节点
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 判断当前节点是否是头结点，如果是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        # 查找节点是否存在
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    a = SingleLinkList()
    # print(a.is_empty())
    # print(a.length())
    # a.append(1)
    # print(a.is_empty())
    # print(a.length())
    #
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.travel()
    # print(1 and 2)