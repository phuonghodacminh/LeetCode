/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1==nullptr) return l2;
        else if(l2==nullptr) return l1;
        else{
            int count=0;
            ListNode* head=new ListNode((l1->val+l2->val+count)%10);
            count=(l1->val+l2->val+count)/10;
            ListNode* temp=head;
            l1=l1->next;
            l2=l2->next;
            while(l1!=nullptr&&l2!=nullptr){
                ListNode* newNode=new ListNode((l1->val+l2->val+count)%10);
                count=(l1->val+l2->val+count)/10;
                l1=l1->next;
                l2=l2->next;
                temp->next=newNode;
                temp=temp->next;
            }
            if(l1==nullptr){
                while(l2!=nullptr){
                    ListNode* newNode=new ListNode((l2->val+count)%10);
                    count=(l2->val+count)/10;
                    l2=l2->next;
                    temp->next=newNode;
                    temp=temp->next;
                }
            }
            else if(l2==nullptr){
                while(l1!=nullptr){
                    ListNode* newNode=new ListNode((l1->val+count)%10);
                    count=(l1->val+count)/10;
                    l1=l1->next;
                    temp->next=newNode;
                    temp=temp->next;
                }
            }
            if(count!=0){
                ListNode* newNode=new ListNode(count);
                temp->next=newNode;
                temp=temp->next;
            }
            return head;
        }
    }
};