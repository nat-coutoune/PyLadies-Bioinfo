#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# This problem is an example of string slicing :)

# input files
DNA = A
sub = A

# loop

for position in range(len(DNA)):
    if DNA[position].starswith(sub):
        print(position+1) 


