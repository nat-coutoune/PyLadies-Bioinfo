#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

def reversecomp(dna):
  '''
  Fx para fazer o reverso complementario de uma seq de DNA.
  '''
  rev = dna[::-1]
  complement = rev.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
  return complement

fasta = open("output_revc.txt","r")
seq = fasta.read()
print(reversecomp(seq))

'''
#Other solutions:
reverseComplement('AAAACCCGGT')
'ACCGGGTTTT'

from Bio import SeqIO
reverseComplement(*SeqIO.parse('data.fna', 'fasta'))

'''
