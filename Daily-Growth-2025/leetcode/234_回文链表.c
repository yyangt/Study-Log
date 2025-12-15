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
// 递归版
/*

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };

struct ListNode* l1;
bool helper(struct ListNode *l2){
    if(l2==NULL){
        return true;
    }
    bool ans=helper(l2->next);
    if(ans==false){
        return false;
    }
    bool p=(l2->val==l1->val);
    l1=l1->next;
    return p;
}
bool isPalindrome(struct ListNode* head) {
    l1=head;
    return helper(head);
}
*/