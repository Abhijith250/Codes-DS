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
tr = trie()
tr.insert("here")
tr.insert("hear")
tr.insert("he")
tr.insert("hello")
tr.insert("how ")
tr.insert("her")
print(tr.search("hes"))
     
