# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: SeongHyeok Im
"""

from random import shuffle

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

start_codon = str(codons[aa.index('M')][0])
stop_codons = codons[aa.index('|')]

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
    l = len(dna)
    res = []
    for i in range(0, l, 3):
        s = dna[i: i + 3]
        for j in range(len(codons)):
#            for codon in codons[j]:
#                if codon == s:
#                    res.append(aa[j])
#                    break;
            if s in codons[j]:  # [WOW] Python is really nice unlike C, yay!!
                res.append(aa[j])
    return collapse(res)

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    # list of [input, expected output]
    data_list = [
        # pass cases
        ["ATGCGA", "MR"],
        ["ATGCCCGCTTT", "MPA"],
        ["AAA", "K"],
        ["TTT", "F"],
        ["CCC", "P"],
        ["GGG", "G"],
        ["AAAA", "K"],
        ["AAAAA", "K"],
        ["AAAAAA", "KK"],
        ["CTAGAGTCT", "LES"],
        ["TTCCTCATCCCG", "FLIP"],
        ["GGTGGA", "GG"],
        ["TGAACCCGTAACGCACCTTGG", "|TRNAPW"],
        ["AGGGCCATTAAT", "RAIN"],
        ["CCGGAGCCTAGTATA", "PEPSI"],
    ]
    for data in data_list:
        if len(data) == 2:
            print "input: " + str(data[0]) + "," ,
            print "expected output: " + str(data[1]) + ",",
            o = coding_strand_to_AA(data[0])
            print "actual output: " + str(o)
            if o != data[1]:
                print "## Test Fail Here!"

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    res = "";
    for c in dna:
        if c == 'A':
            res = 'T' + res
        elif c == 'T':
            res = 'A' + res
        elif c == 'G':
            res = 'C' + res
        elif c == 'C':
            res = 'G' + res
    return res

def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    # list of [input, expected output]
    data_list = [
        ["ATGCCCGCTTT", "AAAGCGGGCAT"],
        ["AAAGCGGGCAT", "ATGCCCGCTTT"],
        ["CCGCGTTCA", "TGAACGCGG"],
        ["AAAA", "TTTT"],
        ["TTTT", "AAAA"],
        ["CCCC", "GGGG"],
        ["GGGG", "CCCC"],
        ["ATGGGAATGA", "TCATTCCCAT"],
        ["TCATTCCCAT", "ATGGGAATGA"],
        ["TTTAAAGGGCCC", "GGGCCCTTTAAA"],
        ["GGGCCCTTTAAA", "TTTAAAGGGCCC"],
        ["ATCGATCG", "CGATCGAT"],
        ["CGATCGAT", "ATCGATCG"],
    ]
    for data in data_list:
        if len(data) == 2:
            print "input: " + str(data[0]) + "," ,
            print "expected output: " + str(data[1]) + ",",CTAATGATGCCCCAT
            o = get_reverse_complement(data[0])
            print "actual output: " + str(o)
            if o != data[1]:
                print "## Test Fail Here!"

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.

        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    # [???] 'assumed to begin with a start codon': doesn't need to check input?
#    if len(dna) < 3:
#        return ""
#    if dna[0:3] != start_codon:
#        return ""

    l = len(dna)
    for i in range(3, l, 3):
        if dna[i: i + 3] in stop_codons:
            return dna[0: i]
    return dna

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    data_list = [
        ["ATGTGAA", "ATG"],
        ["ATGAGATAGG", "ATGAGA"],
        ["ATG", "ATG"],
        ["ATGTAG", "ATG"],
        ["ATGTAA", "ATG"],
        ["ATGTGA", "ATG"],
        ["ATGAAATTTGGGAAATTTGGGTAG", "ATGAAATTTGGGAAATTTGGG"],
        ["ATGAAATTTGGG", "ATGAAATTTGGG"],
        ["ATGAGAAGGAAATTTGATGGGGATGGAAGATT", "ATGAGAAGGAAATTTGATGGGGATGGAAGATT"],
        ["ATGAGAAGGAAATTTGATGGGGATGGAAGATAA", "ATGAGAAGGAAATTTGATGGGGATGGAAGA"],
        ["ATGAA", "ATGAA"],
        ["ATGATGATG", "ATGATGATG"],
    ]
    for data in data_list:
        if len(data) == 2:
            print "input: " + str(data[0]) + "," ,
            print "expected output: " + str(data[1]) + ",",
            o = rest_of_ORF(data[0])
            print "actual output: " + str(o)
            if o != data[1]:
                print "## Test Fail Here!"

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    res = []
    l = len(dna)
    next_pos = 0
    while True:
        arg = dna[next_pos:]
#        orf = rest_of_ORF(arg)
#        res.append(orf)
#        if arg == orf:  # if: no stop codon
#            break
#        next_pos = dna.index(orf, next_pos) + len(orf) + 3  # point next position
#        if next_pos >= l:   # if: meet the end of dna
#            break
        if arg[0:3] == start_codon:
            orf = rest_of_ORF(arg)
            res.append(orf)
            if arg == orf:  # if: no stop codon
                break
            next_pos = dna.index(orf, next_pos) + len(orf) + 3  # point next position
        else:   # if: not start codon, see next
            next_pos += 3
        if next_pos >= l:   # if: meet or go beyond the end of dna
            break
    return res

def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    data_list = [
        ["ATGCATGAATGTAGATAGATGTGCCC", ["ATGCATGAATGTAGA", "ATGTGCCC"]],
        ["ATGTAGATGTAG", ["ATG", "ATG"]],
        ["ATGATGATG", ["ATGATGATG"]],
        ["ATGGGGGATTAGATGATG", ["ATGGGGGAT", "ATGATG"]],
        ["ATGTGAATGTAA", ["ATG", "ATG"]],
        ["ATGTGAATGTAAATG", ["ATG", "ATG", "ATG"]],
        ["ATGCGTGGTGATTAGATGGATGGGGATTGA", ["ATGCGTGGTGAT", "ATGGATGGGGAT"]],
        ["ATGAAATTTCCCGGGAAATTTCCCGGG", ["ATGAAATTTCCCGGGAAATTTCCCGGG"]],
        ["ATGAAATTTTGAATGGGGCCC", ["ATGAAATTT", "ATGGGGCCC"]],
        ["ATGAAATTTTGAATGGGGCCCTAG", ["ATGAAATTT", "ATGGGGCCC"]],
    ]
    for data in data_list:
        if len(data) == 2:
            print "input: " + str(data[0]) + ",",
            print "expected output: " + str(data[1]) + ",",
            o = find_all_ORFs_oneframe(data[0])
            print "actual output: " + str(o)
            if o != data[1]:
                print "## Test Fail Here!"

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    res = []
    for i in range(0, 3):
        s = dna[i:]
#        print i, s,
#        l = len(s)
#        for j in range(0, l, 3):
#            if s[j: j + 3] == start_codon:
#                r = find_all_ORFs_oneframe(s[j:])
#                print r
#                if len(r) > 0:
#                    for item in r:
#                        res.append(item)
#                break   # careful for indentation here!!
        r = find_all_ORFs_oneframe(s)
        if len(r) > 0:
#            for item in r:
#                res.append(item)
            res += r    # [WOW] I love python!
    return res

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    data_list = [
        ["ATGCATGAATGTAG", ["ATGCATGAATGTAG", "ATGAATGTAG", "ATG"]],
        ["ATG", ["ATG"]],
        ["AATG", ["ATG"]],
        ["AAATG", ["ATG"]],
        ["ATGATG", ["ATGATG"]],
        ["ATATGGATTGA", ["ATGGAT"]],
        ["ATGAGATTAG", ["ATGAGATTAG"]],
        ["ATATGGATTAGTAGTAATGAAAGTATAG", ["ATGAAAGTA", "ATGGAT", ]],
# ATA TGG ATT AGT AGT AAT GAA AGT ATA G
# TAT GGA TTA GTA GTA ATG AAA GTA TAG
# ATG GAT TAG TAG TAA TGA AAG TAT AG
        ["ATGTCACGCAATGTAGGATGGATGGATTAGAC", ["ATGTCACGCAATGTAGGATGGATGGAT", "ATG", "ATGGATGGATTAGAC"]],
# ATG TCA CGC AAT GTA GGA TGG ATG GAT TAG AC --> ATG TCA CGC AAT GTA GGA TGG ATG GAT
# TGT CAC GCA ATG TAG GAT GGA TGG ATT AGA C
# GTC ACG CAA TGT AGG ATG GAT GGA TTA GAC
        ["ATGATGTAG", ["ATGATG"]],
        ["TCGATGC", ["ATGC"]],
        ["AAA", []],
# TCG ATG C
# CGA TGC
# GAT GC
    ]
    for data in data_list:
        if len(data) == 2:
            print "input: " + str(data[0]) + ",",
            print "expected output: " + str(data[1]) + ",",
            o = find_all_ORFs(data[0])
            print "actual output: " + str(o)
            if o != data[1]:
                print "## Test Fail Here!"

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    data_list = [
        ["ATGCGAATGTAGCATCAAA", ["ATGCGAATG", "ATGCTACATTCGCAT"]],
        ["ATG", ["ATG"]],
        ["CAT", ["ATG"]],
        ["CATCAT", ["ATGATG"]],
        ["CATGGGCAT", ["ATGGGCAT", "ATGCCCATG"]],
        ["CATGCAGTGCACGGATGGCAT", ["ATGCAGTGCACGGATGGCAT", "ATGGCAT", "ATGCCATCCGTGCACTGCATG"]],
# CATGCAGTGCACGGATGGCAT
# CAT GCA GTG CAC GGA TGG CAT
# ATG CAG TGC ACG GAT GGC AT
# TGC AGT GCA CGG ATG GCA T
# ATGCCATCCGTGCACTGCATG
# ATG CCA TCC GTG CAC TGC ATG
# TGC CAT CCG TGC ACT GCA TG
# GCC ATC CGT GCA CTG CAT G
        ["CATATGTAG", ["ATG", "ATG"]],
        ["ATGGGGCATCATTAG", ["ATGGGGCATCAT", "ATGATGCCCCAT"]],
# ATGGGGCATCATTAG
# ATG GGG CAT CAT TAG
# TGG GGC ATC ATT AG
# GGG GCA TCA TTA G
# CTAATGATGCCCCAT
# CTA ATG ATG CCC CAT
# TAA TGA TGC CCC AT
# AAT GAT GCC CCA T
    ]
    for data in data_list:
        if len(data) == 2:
            print "input: " + str(data[0]) + ",",
            print "expected output: " + str(data[1]) + ",",
            o = find_all_ORFs_both_strands(data[0])
            print "actual output: " + str(o)
            if o != data[1]:
                print "## Test Fail Here!"

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    l = find_all_ORFs_both_strands(dna)
    max_len = 0
    r = ""
    # [???] what if there are ORFs with same length?
    #       this function just get the first one.
    if len(l) == 0:
        return ""
    for o in l:
        if len(o) > max_len:
            r = o
            max_len = len(o)
    return r

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    data_list = [
        ["ATGCGAATGTAGCATCAAA", "ATGCTACATTCGCAT"],
        ["ATG", "ATG"],
        ["CAT", "ATG"],
        ["CATCAT", "ATGATG"],
        ["CATGGGCAT", "ATGCCCATG"],
        ["CATGCAGTGCACGGATGGCAT", "ATGCCATCCGTGCACTGCATG"],
# CATGCAGTGCACGGATGGCAT
# CAT GCA GTG CAC GGA TGG CAT
# ATG CAG TGC ACG GAT GGC AT
# TGC AGT GCA CGG ATG GCA T
# ATGCCATCCGTGCACTGCATG
# ATG CCA TCC GTG CAC TGC ATG
# TGC CAT CCG TGC ACT GCA TG
# GCC ATC CGT GCA CTG CAT G
        ["CATATGTAG", "ATG"],
        ["ATGGGGCATCATTAG", "ATGGGGCATCAT"],
# ATGGGGCATCATTAG
# ATG GGG CAT CAT TAG
# TGG GGC ATC ATT AG
# GGG GCA TCA TTA G
# CTAATGATGCCCCAT
# CTA ATG ATG CCC CAT
# TAA TGA TGC CCC AT
# AAT GAT GCC CCA T
    ]
    for data in data_list:
        if len(data) == 2:
            print "input: " + str(data[0]) + ",",
            print "expected output: " + str(data[1]) + ",",
            o = longest_ORF(data[0])
            print "actual output: " + str(o)
            if o != data[1]:
                print "## Test Fail Here!"

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    org = list(dna)
    max_len = 0
    r = ""
    for i in range(num_trials):
       l = org
       shuffle(l)
       orf = longest_ORF(collapse(l))
       if len(orf) > max_len:
           r = orf
           max_len = len(orf)
    return r

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
    r = []
    if len(l) > 0:
        for item in l:
            if len(item) > threshold:
                r.append(item)
    for i in range(len(r)):
        r[i] = coding_strand_to_AA(r[i])
    return r

#def gene_finder_unit_tests():
#    """ Unit tests for the gene_finder function """
#    data_list = [
#        ["ATGCGAATGTAGCATCAAA", 3, ["ATGCGAATG", "ATGCTACATTCGCAT"]],
#        ["ATGCGAATGTAGCATCAAA", 300, []],
#        ["ATG", 1, ["ATG"]],
#        ["CAT", 1, ["ATG"]],
#        ["CATCAT", 1, ["ATGATG"]],
#        ["CATGGGCAT", 1, ["ATGGGCAT", "ATGCCCATG"]],
#        ["CATGCAGTGCACGGATGGCAT", 1, ["ATGCAGTGCACGGATGGCAT", "ATGGCAT", "ATGCCATCCGTGCACTGCATG"]],
## CATGCAGTGCACGGATGGCAT
## CAT GCA GTG CAC GGA TGG CAT
## ATG CAG TGC ACG GAT GGC AT
## TGC AGT GCA CGG ATG GCA T
## ATGCCATCCGTGCACTGCATG
## ATG CCA TCC GTG CAC TGC ATG
## TGC CAT CCG TGC ACT GCA TG
## GCC ATC CGT GCA CTG CAT G
#        ["CATATGTAG", 1, ["ATG", "ATG"]],
#        ["ATGGGGCATCATTAG", 1, ["ATGGGGCATCAT", "ATGATGCCCCAT"]],
## ATGGGGCATCATTAG
## ATG GGG CAT CAT TAG
## TGG GGC ATC ATT AG
## GGG GCA TCA TTA G
## CTAATGATGCCCCAT
## CTA ATG ATG CCC CAT
## TAA TGA TGC CCC AT
## AAT GAT GCC CCA T
#    ]
#    for data in data_list:
#        if len(data) == 3:
#            print "input: " + str(data[0]) + " " + str(data[1]) + ",",
#            print "expected output: " + str(data[2]) + ",",
#            o = gene_finder(data[0], data[1])
#            print "actual output: " + str(o)
#            if o != data[2]:
#                print "## Test Fail Here!"

#if __name__ == "__main__":
    #print start_codon, stop_codons
    #coding_strand_to_AA_unit_tests()
    #get_reverse_complement_unit_tests()
    #rest_of_ORF_unit_tests()
    #find_all_ORFs_oneframe_unit_tests()
    #find_all_ORFs_unit_tests()
    #find_all_ORFs_both_strands_unit_tests()
    #longest_ORF_unit_tests()
    #print longest_ORF_noncoding("AGCTAGCAGGCGCGATAATCGCGAGAGATCTAGCTAGTC", 500)
    #gene_finder_unit_tests()
