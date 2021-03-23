# https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
# 直接看官方题解吧

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        head = ListNode(next=head)  # 由于头部的特殊属性，开一个虚拟头，方便操作
        _head = head
        for _ in range(left - 1):
            _head = _head.next

        this = _head.next

        for _ in range(right - left):
            nxt = this.next
            this.next = nxt.next
            nxt.next = _head.next
            _head.next = nxt

        return head.next

head = ListNode()
this = head
for v in [1,2]:
    this.val = v
    this.next = ListNode()
    this = this.next

s = Solution()
this = s.reverseBetween(head, 1, 2)

while this.next:
    print(this.val, end=' ')
    this = this.next

