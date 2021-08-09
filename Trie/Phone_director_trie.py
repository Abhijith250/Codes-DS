# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:20:19 2021

@author: Abhi
"""


class trieNode:
    def __init__(self,char):
        self.char=char
        self.isend=False
        self.children={}
class trie(object):
    def __init__(self):
        self.root=trieNode("*")
    
    def insert(self,word):
        node=self.root
        for char in word:
            
            if char in node.children:
                node=node.children[char]
            else:
                new=trieNode(char)
                node.children[char]=new
                node=new
        node.isend=True
        
    def search(self,word):
        cur=self.root
        for i in word:
            if i in cur.children:
                cur=cur.children[i]
            else:
                return False
        return True
    def displayall(self,prefix,last):
        if last.isend==True:
            print(prefix)
        for i in range(97,127):
               if chr(i) in last.children:
                    print(prefix)
                    newnode=last.children[chr(i)]
                    self.displayall(prefix+chr(i),newnode)
    
      
     
        
        
        print(prefix)
        
    def display(self,strin):
        n=len(strin)
        node=self.root
        prefix=""
        for i in strin:
            prefix+=i
            last=i
            cur=node.children[last]
            if last not in node.children:
                print("not found")
                break
            self.displayall(prefix,cur)
            node=cur
           
tr = trie()
tr.insert("aere")
tr.insert("aear")
tr.insert("ae")
tr.insert("aello")
tr.insert("aow ")
tr.insert("aer")
print(tr.search("hes"))
tr.display("a")
     
