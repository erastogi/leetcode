#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:30:47 2017

@author: eti
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self , root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root :
            return None
        if key < root.val and root.left is not None:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val and root.right is not None:
            root.right = self.deleteNode(root.right,key)
        elif key == root.val  :  
                if root.right is not None :  
                    rt = root.right
                    while(rt.left is not None) :
                        rt = rt.left
                    root.val = rt.val
                    root.right = self.deleteNode(root.right,rt.val)
                elif root.left is not None :  
                    rt = root.left
                    while(rt.right is not None) :
                        rt = rt.right
                    root.val = rt.val
                    root.left = self.deleteNode(root.left,rt.val)    
                else : #no child
                     return None
                        
        else :
             return(root)
        return root     