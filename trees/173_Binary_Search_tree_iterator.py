#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:32:21 2017

@author: eti
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        #global st
        self.st = list()
        self.node = root
        if self.node :
            self.st.append(root)
            while self.node.left :
                self.node = self.node.left
                self.st.append(self.node)
            
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.st :
           return 1
        else:
            return 0 
            
    def next(self):
        """
        :rtype: int
        """
        #global st
        
        x = self.st[-1]
        del self.st[-1]
        if x.right :
             self.node = x.right
             self.st.append(self.node)
             self.addnode(self.node)
        return x.val
        
    def addnode(self,node) :
        while self.node.left :
            self.node = self.node.left
            self.st.append(self.node)
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())