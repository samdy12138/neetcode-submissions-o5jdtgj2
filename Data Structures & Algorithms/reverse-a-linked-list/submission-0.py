# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        cur=head
        while cur:
            nextcur=cur.next
            cur.next=pre
            pre=cur
            cur=nextcur
        return pre
        