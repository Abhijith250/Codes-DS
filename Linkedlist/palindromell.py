# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:11:20 2021

@author: Abhi
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeinput():
    head=None
    tail=None
    d=list(map(int,input().split(' ')))
    i=0
    while d[i]!=-1 and i<len(d):
        n=Node(d[i])
        if head is None:
            head=n
            tail=n
        else:
            tail.next=n
            tail=n
        i+=1
    return head
def reverse(head):
    cur=head
    prev=None
    while cur !=None:
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp
    return prev
def checkpali(head1,head2):
    while head1 is not None:
        if head1.data!=head2.data:
            return False
        head1=head1.next
        head2=head2.next
    return True
def printll(head):
    while head is not None:
        print(head.data)
        head=head.next
    
    


t=int(input())
while t>0:

    head=takeinput()
    printll(head)
    head2=reverse(head)
    printll(head2)
    print(checkpali(head,head2))
    t-=1
