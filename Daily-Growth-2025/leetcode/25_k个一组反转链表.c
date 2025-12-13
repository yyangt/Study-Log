struct ListNode* s=NULL;

struct ListNode *reversen(struct ListNode *head,int n){
    if(n==1){
      s=head->next;
      return head;
    }
    struct ListNode*newnode=reversen(head->next,n-1);
    head->next->next=head;
    head->next=s;
    return newnode;
}
struct ListNode* helper(struct ListNode* head, int k,int num){
    if(num<k||k==1){
        return head;
    }
    struct ListNode *p=reversen(head,k);
    struct ListNode *q=head;
    head->next=helper(s,k,num-k);
    return p;
}
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    int n=1;
    struct ListNode* t=head;
    while(t->next!=NULL){
      t=t->next;
      n++;
    }
    /*
    while (t) {
      n++;
      t = t->next;
    }
    */
    return helper(head,k,n);

}
