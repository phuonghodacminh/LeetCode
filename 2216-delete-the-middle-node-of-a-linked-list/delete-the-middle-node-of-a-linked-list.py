# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        _1st = head
        _2nd = head
        _1stprev = None
        while _2nd and _2nd.next:
            _1stprev = _1st
            _1st = _1st.next
            _2nd = _2nd.next.next
        
        if not _1stprev:
            return None
        else:
            _1stprev.next = _1st.next
            _1st.next = None
        
        return head

        