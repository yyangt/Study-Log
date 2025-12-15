/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* helper(struct ListNode* head, int n,int *k){
    if(head==NULL){
        return head;
    }
    head->next=helper(head->next,n,k);
    (*k)++;
    if(*k==n){
        struct ListNode* temp=head->next;
        free(head);
        return temp;
    }
    return head;
}
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int k=0;
    return helper(head,n,&k);
}