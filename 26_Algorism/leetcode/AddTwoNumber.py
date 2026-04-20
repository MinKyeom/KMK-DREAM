# 출처:https://leetcode.com/problems/add-two-numbers/

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

      node1 = l1
      node2 = l2

      num1 = ""
      num2 = ""

      while node1 != None :
          num1 += str(node1.val)
          node1 = node1.next

      while node2 != None:
          num2 += str(node2.val)
          node2 = node2.next
      
      result = int(num1[::-1])+int(num2[::-1])
      final = list(map(int,list(str(result)[::-1])))
      
      final_result = ListNode(final[0])
      current = final_result

      for i in range(1, len(final)):
          current.next = ListNode(final[i])
          current = current.next
          
      return final_result