#include<stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverse(struct ListNode* head){
    if(head->next==NULL||head==NULL){
        return head;
    }
    struct ListNode *p=reverse(head->next);
    head->next->next=head;
    head->next=NULL;
    return p;
}
bool isPalindrome(struct ListNode* head) {
    if(head==NULL){
        return 0;
    }
    if(head->next==NULL){
        return 1;
    }
    struct ListNode *cur=head;
    struct ListNode* tail=NULL;
    struct ListNode* copy=NULL;
    while(cur!=NULL){
        struct ListNode* newnode=(struct ListNode*)malloc(sizeof(struct ListNode));
        newnode->val=cur->val;
        newnode->next=NULL;
        if(copy==NULL){
            copy=newnode;
            tail=newnode;
        }
        else{
            tail->next=newnode;
            tail=newnode;
        }
        cur=cur->next;
    }
    struct ListNode* p=reverse(copy);
    while(head!=NULL){
        if(p->val!=head->val){
            return 0;
        }
        p=p->next;
        head=head->next;

    }
    return 1;
}