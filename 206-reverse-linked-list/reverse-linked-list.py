# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr, ans = head, None
        while ptr:
            head = head.next
            ptr.next = ans
            ans = ptr
            ptr = head
        
        return ans

        