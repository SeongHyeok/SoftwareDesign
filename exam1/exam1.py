# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 15:23:45 2014

@author: sim
"""

############################################################################
# Prob 1
############################################################################

def sum_squares_even(n):
    s = 0
    for i in range(2, n + 1, 2):
        s += i ** 2
    return s

def test_prob1():
    print sum_squares_even(10)
    print sum_squares_even(5)
    print sum_squares_even(0)
    print sum_squares_even(1)
    print sum_squares_even(2)

############################################################################
# Prob 2
############################################################################

def pair_list_to_dictionary(l):
    d = dict()
    for i in range(0, len(l), 2):
        if i == len(l) - 1:
            break
        d[l[i]] = l[i + 1]
    return d

def test_prob2():
    print pair_list_to_dictionary([1, 'a', 5])
    print pair_list_to_dictionary(['hello', 'a', 'test', 'b'])
    print pair_list_to_dictionary([1, 2, 3, 4, 5, 6, 7])
    print pair_list_to_dictionary([])
    print pair_list_to_dictionary([1])

############################################################################
# Prob 3
############################################################################

def split_dictionary(d):
    d1 = dict()
    d2 = dict()
    l = []
    for key in d.keys():
        if key[0].isupper():
            d1[key] = d[key]
        else:
            d2[key] = d[key]
    l.append(d1)
    l.append(d2)
    return l

def test_prob3():
    print split_dictionary({'a':2, 'B':'hello', 'c':'t'})
    print split_dictionary({'A':1, 'B':2, 'C':3})
    print split_dictionary({'a':1, 'b':2, 'c':3})
    print split_dictionary({})

############################################################################
# Prob 4
############################################################################

def in_language(s):
    na = nb = 0
    for c in s:
        if c == 'a':
            na += 1
        elif c == 'b':
            nb += 1
            break
        else:
            return False
    for c in s[na + nb:]:
        if c != 'b':
            return False
        nb += 1
    return na == nb

def test_prob4():
    print in_language('aaab')
    print in_language('aaaccc')
    print in_language('')
    print in_language('aaaabbbb')
    print in_language('ab')
    print in_language('aabb')
    print in_language('abab')
    print in_language('c')
    print in_language('caabb')
    print in_language('aacbb')
    print in_language('aabbc')

############################################################################
# Prob 5
############################################################################

class DNASequence:
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides

    def get_reverse_complement(self):
        rev_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        res = ''
        for c in self.nucleotides:
            res = rev_dict[c] + res
        return DNASequence(res)

    def get_proportion_ACGT(self):
        d = {'A':0, 'C':0, 'G':0, 'T':0}
        if len(self.nucleotides) > 0:   # necessary for empty nucleotides!
            for key in d.keys():
                d[key] = self.nucleotides.count(key) / float(len(self.nucleotides))
        return d

def test_prob5():
    d = DNASequence("AAATTTGGGCCC")
    print d.nucleotides
    print d.get_reverse_complement().nucleotides
    print d.get_proportion_ACGT()

    d = DNASequence("AAA")
    print d.get_proportion_ACGT()

    d = DNASequence("CGT")
    print d.get_proportion_ACGT()

    d = DNASequence("") # empty string
    print "[%s]" % (d.nucleotides)
    print "[%s]" % (d.get_reverse_complement().nucleotides)
    print d.get_proportion_ACGT()

if __name__ == "__main__":
    test_prob1()
    #test_prob2()
    #test_prob3()
    #test_prob4()
    #test_prob5()