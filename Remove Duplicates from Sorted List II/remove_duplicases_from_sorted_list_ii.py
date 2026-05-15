class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):

        # tạo dummy node
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:

            # nếu phát hiện duplicate
            if current.next and current.val == current.next.val:

                duplicate = current.val

                # bỏ qua tất cả node duplicate
                while current and current.val == duplicate:
                    current = current.next

                prev.next = current

            else:
                prev = prev.next
                current = current.next

        return dummy.next


# hàm tạo linked list
def build_linked_list(arr):

    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# hàm in linked list
def print_linked_list(head):

    while head:
        print(head.val, end=" -> ")
        head = head.next

    print("None")


if __name__ == "__main__":

    arr = [1,2,3,3,4,4,5]

    head = build_linked_list(arr)

    print("Linked List ban đầu:")
    print_linked_list(head)

    sol = Solution()

    result = sol.deleteDuplicates(head)

    print("\nSau khi xóa duplicates:")
    print_linked_list(result)