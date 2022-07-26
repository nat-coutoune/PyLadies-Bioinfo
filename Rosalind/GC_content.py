#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# Link do video: https://www.youtube.com/watch?v=mw4FSbDro0A

def readFile(filePath):
    '''Reading a file and returning a list of lines'''
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
    '''Return the GC content in a DNA/RNA sequence'''
    return round(
        ((seq.count("C") + seq.count("G")) / len(seq) * 100), 6)

# --- Read data from a (fasta) file -------------------------------------------
# Storing the file content in a list
FASTAfile = readFile('rosalind_gc.txt')
# Dictionary for Labels +data
FASTAdict = {}
# String for folding the current label
FASTAlabel = ""


# --- Clean/Prepare  tha data (format for the gc_function fx) ----------------
# Converting the fasta file/list into a dictionary
for line in FASTAfile:
    if '>' in line:
        FASTAlabel = line
        FASTAdict[FASTAlabel] = ""
    else:
        FASTAdict[FASTAlabel] += line 

#print(FASTAfile)
#print(FASTAlabel)
#print(FASTAdict)

# --- Format the data (store the data in a convenient way)-------------------
# Using the dictionary comprehension to generate a new dictionary with GC content
RESULTdict ={key: gc_content(value) for (key,value) in FASTAdict.items()}
print(RESULTdict)

# --- Collect the results (Rosalind submission)
MaxGCkay = max(RESULTdict, key = RESULTdict.get)

# Printing the solsalind formatted result:
print(f'{MaxGCkay[1:]}\n{RESULTdict[MaxGCkay]}')


  