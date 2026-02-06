class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) if res else "[]")


if __name__ == "__main__":
    nums = [10, 20, 30, 40]
    n = 3

    head = build_list(nums)
    print("Danh sách ban đầu:")
    print_list(head)

    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)

    print("\nSau khi xóa node thứ", n, "từ cuối:")
    print_list(new_head)
