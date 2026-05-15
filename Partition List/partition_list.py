class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):

        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy
        large = large_dummy

        current = head

        while current:

            if current.val < x:

                small.next = current
                small = small.next

            else:

                large.next = current
                large = large.next

            current = current.next

        large.next = None

        small.next = large_dummy.next

        return small_dummy.next


# tạo linked list
def build_linked_list(arr):

    dummy = ListNode(0)
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# in linked list
def print_linked_list(head):

    while head:
        print(head.val, end=" -> ")
        head = head.next

    print("None")


if __name__ == "__main__":

    arr = [1,4,3,2,5,2]
    x = 3

    head = build_linked_list(arr)

    print("Linked List ban đầu:")
    print_linked_list(head)

    sol = Solution()

    result = sol.partition(head, x)

    print("\nSau khi partition:")
    print_linked_list(result)