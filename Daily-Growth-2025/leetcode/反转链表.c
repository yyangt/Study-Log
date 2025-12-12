/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reversebeforen(struct ListNode* head, int n) {
    if (n==1){

      sus=head->next;
      return head;

    }
    struct ListNode* newnode=reversebeforen(head->next,n-1);
    head->next->next=head;
    head->next=sus;
    return newnode;
    
}