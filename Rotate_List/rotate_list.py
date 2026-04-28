class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def build_list(arr):
    head = ListNode(arr[0])
    cur = head
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        tail.next = head

        k = k % n
        steps = n - k

        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 2

    head = build_list(arr)

    print("Before:")
    print_list(head)

    sol = Solution()
    new_head = sol.rotateRight(head, k)

    print("After:")
    print_list(new_head)