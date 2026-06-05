class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         break
        # else: return None

        # fast = head

        # while fast != slow:
        #     fast = fast.next
        #     slow = slow.next
        
        # return slow

        '''
        Alternative solution
        '''

        seen = set()


        while head:
            if head in seen:
                return head

            seen.add(head)
            head = head.next

        return None