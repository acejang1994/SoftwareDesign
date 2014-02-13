# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
import random

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    result = ''
    for i in range(0,len(dna)/3):               # divide by 3 to get the codon pairs
        part = dna[3*i:3*i+3]
        for k in range(0,len(codons)):          # going through codons
            for j in range(0,len(codons[k])):   # going through the lists in codon
                if part == codons[k][j]:        
                    result = result + aa[k]
    return result
   
#print coding_strand_to_AA('ATGCGA')
#print coding_strand_to_AA("ATGCCCGCTTT")

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    print 'INPUT_HERE' + 'ATGCGA'
 
    print 'EXPECTED OUTCOME'  + 'MR'
    print 'ACTUAL_OUTPUT_HERE' + coding_strand_to_AA('ATGCGA')
  
def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    result = ''
    back = ''
    for i in range(0, len(dna)):
        if dna[i] == 'A':               #matching the complement pairs
            result = result + 'T'
        if dna[i] == 'T':
            result = result + 'A'
        if dna[i] == 'G':
            result = result + 'C'
        if dna[i] == 'C':
            result = result + 'G'
                  
    for i in range(0, len(result)):
        back = back +  result[(len(result) - i-1)]      #putting it in reverse
    return back
        
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    
    print 'INPUT_HERE  ' + "ATGCCCGCTTT"
    print 'EXPECTED OUTCOME  '  + 'AAAGCGGGCAT'
    print 'ACTUAL_OUTPUT_HERE ' + get_reverse_complement("ATGCCCGCTTT")
    
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    result = ''
    for i in range(0, len(dna),3):
        part = dna[i:i+3]
        if part == 'TAA' or part == 'TAG' or part == 'TGA':     # break at break codons
            break
        else:
            result = result + part
    return result

#print rest_of_ORF('ATGAGATAGG')

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    print 'INPUT_HERE  ' + "ATGAGATAGG"
    print 'EXPECTED OUTCOME  '  + 'ATGAGA'
    print 'ACTUAL_OUTPUT_HERE  ' + rest_of_ORF("ATGAGATAGG")
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    frame = []
    while len(dna) > 0:                 #while there is something in dna
        if not (dna[:3] == 'ATG'):      
            dna = dna[3:]               # if the codon is not ATG then cut off the first codon
        else:
            x = rest_of_ORF(dna)        
            frame.append(x)
            dna = dna[len(x):]          # after appending rest_of_ORF cut off the dna
    return frame
   
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    print 'INPUT_HERE ' + "ATGCATGAATGTAGATAGATGTGCCC"
    print 'EXPECTED OUTCOME '  + "['ATGCATGAATGTAGA', 'ATGTGCCC']"
    print 'ACTUAL_OUTPUT_HERE ' + find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    frame = find_all_ORFs_oneframe(dna)
    dna = dna[1:]                           # change the reading frame
    frame += find_all_ORFs_oneframe(dna)
    dna = dna[1:]                           # change the reading frame
    frame += find_all_ORFs_oneframe(dna)
    return frame
    
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print 'INPUT_HERE ' + "ATGCGAATGTAGCATCAAA"
    print 'EXPECTED OUTCOME '  + "['ATGCGAATG', 'ATGCTACATTCGCAT']"
    print 'ACTUAL_OUTPUT_HERE ' + find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    frame = find_all_ORFs(dna)
    reverse = get_reverse_complement(dna)           
    frame += find_all_ORFs(reverse)

    return frame
    
def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    
    print 'INPUT_HERE ' + "ATGCGAATGTAGCATCAAA"
    print 'EXPECTED OUTCOME '  + "['ATGCGAATG', 'ATGCTACATTCGCAT']"
    print 'ACTUAL_OUTPUT_HERE ' + find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    
    
def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    frame = find_all_ORFs_both_strands(dna)         #find the frame
    ref = ''
    for i in frame:
        if len(i) > len(ref):               # find the max in the frame
            ref = i
    return ref

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    print 'INPUT_HERE ' + "ATGCGAATGTAGCATCAAA"
    print 'EXPECTED OUTCOME '  + 'ATGCTACATTCGCAT'
    print 'ACTUAL_OUTPUT_HERE ' + longest_ORF("ATGCGAATGTAGCATCAAA")

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    
    ldna = list(dna)
    longest = 0
    for i in range(0, num_trials):
          
        random.shuffle(ldna)
        dna = collapse(ldna)
        if len(longest_ORF(dna)) > longest:         #find the longest
            longest = longest_ORF(dna)              
    return longest

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    l = find_all_ORFs_both_strands(dna)         
    real = []
    aacid = []
    for i in l:
        if len(i) > threshold:          # if greater than threshold add to real
            real.append(i)
    
    for i in real:
        aacid.append(coding_strand_to_AA(i))    # add to codons of real to aacid
    
    return aacid
        
 
from load import load_seq

dna = load_seq("./data/X73525.fa")
x = longest_ORF_noncoding(dna, 1500)
print len(x)
print gene_finder(dna, len(x)/3)
