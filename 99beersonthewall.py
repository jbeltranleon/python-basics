#!/usr/bin/env python
# -*-coding:utf-8-*-
def sing(b,end):
    print(b or 'No more', 'bottle' + ('s' if b-1 else ''), end)

for i in range(99,0,-1):
    sing(i,'of beer on the wall,')
    sing(i, 'of beer,')
    print "Take one down, and pass it around,"
    sing(i-1,'of beer on the wall.\n')
    
verse = '''\
{some} bottles of beer on the wall
{some} bottles of beer
Take one down, pass it around
{less} bottles of beer on the wall
'''
 
for bottles in range(99,0,-1):
    print verse.format(some=bottles, less=bottles-1)