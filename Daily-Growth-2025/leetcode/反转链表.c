/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/*------------------------------------------------------*/
// 最初版本
// struct ListNode* successor=NULL;
// struct ListNode* reversebeforen(struct ListNode* head, int n) {
//     if (n==1){

//       successor=head->next;
//       return head;

//     }
//     struct ListNode* newnode=reversebeforen(head->next,n-1);
//     head->next->next=head;
//     head->next=successor;
//     return newnode;
// }
// struct ListNode* pre=NULL;
// struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    
//     struct ListNode* temp=head;
//     for(int i=1;i<left;i++){
//         pre=temp;
//         temp=temp->next;
//     }
//     struct ListNode* helper(struct ListNode* head, int left, int right,struct ListNode* pre,struct ListNode* start){
//         if(left==1){
//             return reversebeforen(head,right);
//         }
//         struct ListNode* p=helper(head->next,left-1,right-1,pre,start);
//         pre->next=p;
//         return start;
//     }
//     return helper(head,left,right,pre,head);
    
// }

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// 解答版本
/*-----------------------------------------------------------------------------------*/
struct ListNode* successor=NULL;
struct ListNode* reversebeforen(struct ListNode* head, int n) {
    if (n==1){

      successor=head->next;
      return head;

    }
    struct ListNode* newnode=reversebeforen(head->next,n-1);
    head->next->next=head;
    head->next=successor;
    return newnode;
}
struct ListNode* pre=NULL;
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    
    struct ListNode* temp=head;
    for(int i=1;i<left;i++){
        pre=temp;
        temp=temp->next;
    }
    struct ListNode* helper(struct ListNode* head, int left, int right,struct ListNode* pre,struct ListNode* start){
        if(left==1){
            return reversebeforen(head,right);
        }
        struct ListNode* p=helper(head->next,left-1,right-1,pre,start);
        pre->next=p;
        return start;
    }
    return helper(head,left,right,pre,head);
    
}
// 迭代版本
/*----------------------------------------------------------------------*/
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