# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        if self.check_if_lists_intersect(headA, headB):
            large, small = self.make_lists_same_length(headA, headB)
            while large:
                if large == small:
                    return large
                large=large.next
                small=small.next
        else:
            return None
        
        
    def check_if_lists_intersect(self, headA, headB):
        if headA is None and headB is None:
            return False
        if headA is None:
            return False
        if headB is None:
            return False
        p = headA
        q = headB
        while p:
            prev_p=p
            p=p.next
        while q:
            prev_q=q
            q=q.next
        if prev_p==prev_q:
            return True
        else:
            return False
        
    def make_lists_same_length(self, headA, headB):
        len_headA = self.length(headA)
        len_headB = self.length(headB)
        if len_headA > len_headB:
            diff = len_headA-len_headB
            large = headA
            small =headB
        elif len_headB > len_headA:
            diff = len_headB-len_headA
            large=headB
            small=headA
        else:
            return headA, headB
        while diff>0:
            large=large.next
            diff-=1
        return large, small
        
    def length(self, head):
        if head is None:
            return 0
        count=0
        if head:
            count+=1
            head=head.next
        return count
            
