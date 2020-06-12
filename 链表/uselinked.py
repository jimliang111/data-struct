# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head: ListNode, val: int) -> ListNode:
    """
    leetcode 203
    移除链表的元素
    in: 1->2->6->3->4->5->6, val = 6
    out: 1->2->3->4->5
    """
    dummy_head = ListNode(-1)
    dummy_head.next = head

    prev = dummy_head
    while prev.next is not None:
        if prev.next.val == val:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy_head.next


def recursive(head, val):

    if head is None:
        return head

    head.next = recursive(head.next, val)

    return head.next if head.val == val else head


if __name__ == '__main__':
    head = ListNode(1)
    node = head
    for i in range(2, 8):
        if i == 3:
            value = 6
        elif i < 3:
            value = i
        else:
            value = i - 1
        node.next = ListNode(value)
        node = node.next

    # answer = removeElements(head, 6)
    answer = recursive(head, 6)

    while answer is not None:
        print(answer.val, end='->')
        answer = answer.next
