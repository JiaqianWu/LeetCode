/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class AddTwoNumbers {
	public class ListNode {
		 int val;
		 ListNode next;
		 ListNode(int x) { val = x; }
	}
		 
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p!=null || q!=null) {
        	int m = (p!=null) ? p.val:0;
        	int n = (q!=null) ? q.val:0;
        	int sum = m + n + carry;
        	carry = sum/10;
        	curr.next = new ListNode(sum%10);
        	if (p!=null) {
        		p = p.next;
        	}
        	if (q!=null) {
        		q = q.next;
        	}
        	curr = curr.next;
        }
        if (carry > 0) {
        	curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }
}
