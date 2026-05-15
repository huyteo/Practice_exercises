class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):

        current = head

        while current and current.next:

            # nếu trùng
            if current.val == current.next.val:

                # bỏ node duplicate
                current.next = current.next.next

            else:
                current = current.next

        return head


# tạo linked list
def build_linked_list(arr):

    dummy = ListNode()
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

    arr = [1,1,2,3,3]

    head = build_linked_list(arr)

    print("Linked List ban đầu:")
    print_linked_list(head)

    sol = Solution()

    result = sol.deleteDuplicates(head)

    print("\nSau khi xóa duplicate:")
    print_linked_list(result)