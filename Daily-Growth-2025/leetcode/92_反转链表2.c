/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (left==right){
        return head;
    }
    struct ListNode* init=NULL;
    struct ListNode* cur=head;
    for (int i = 1; i < left; i++){
        init=cur;
        cur=cur->next;
    }
    
    struct ListNode* pre=NULL;
    struct ListNode* newnode=cur;
    struct ListNode* next=NULL;
    for (int i=left;i<=right;i++){
        
        next=cur->next;
        cur->next=pre;
        pre=cur;
        cur=next;
    }
    if(left==1){
        head=pre;
    }
    else{
        init->next=pre;
    }
    newnode->next=cur;
    return head;
    
}