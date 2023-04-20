# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        final = []
        l1 = []
        l2 = []
        while list1:
            l1.append(list1.val)
            list1=list1.next
        while list2:
            l2.append(list2.val)
            list2=list2.next
        while True:
            num1=-101
            num2=-101
            len1=len(l1)
            len2=len(l2)
            if len1!=0:
                num1=l1[0]
            if len2!=0:
                num2=l2[0]
            if num1==-101 and num2==-101:
                break
            elif num1<=num2 and num1!=-101:
                final.append(num1)
                l1.remove(num1)
            else:
                if num2!=-101:
                    final.append(num2)
                    l2.remove(num2)
                else:
                    final.append(num1)
                    l1.remove(num1)
        if len(final)>0:
            val = final[0]
            head = ListNode(final[0])
            tail = head
            e = 1
            while e < len(final):
                tail.next = ListNode(final[e])
                tail = tail.next
                e+=1
            #print(head)
            return head
        # return head
