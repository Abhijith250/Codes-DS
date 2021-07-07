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
def deleteNode(head,p):
    if p==1:
        if head.next is not None:
            head.next=head.next.next
            return head
    return deleteNode(head.next, p-1)

def printll(head):
    while head is not None:
        print(head.data)
        head=head.next
    
    


t=int(input())
while t>0:
    print("hi")
    head=takeinput()
    p=int(input())
    printll(head)
    deleteNode(head,p)
    printll(head)
    t-=1
