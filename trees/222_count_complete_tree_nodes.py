#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:31:46 2017

@author: eti
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self , root) :
        n = 0 
        lt = root
        while lt.left is not None :
                lt = lt.left
                n = n + 1
        return n         
    def rheight(self,root):
        n = 0
        lt = root
        while lt.right is not None :
                lt = lt.right
                n = n + 1
        return n 
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root :
            return 0 
        else :
            lt = self.height(root)
            rt = self.rheight(root)
            if lt == rt :
                return 2**(lt+1) - 1
            else :
                return self.countNodes(root.left) + self.countNodes(root.right) + 1
                
    