# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:04:42 2020

@author: Aadhavan
"""

def secret(a, b):
	if b == 0:
		return a
	if a == 0:
		return secret(b, a) - 1
	return secret(a-1, b+a)
print(secret(3, 3))