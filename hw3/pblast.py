# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 03:05:08 2014

@author: SeongHyeok Im
"""

from load import load_salmonella_genome

salmonella_genome = load_salmonella_genome()

def search_genome_simple(genomes, query_AA_seq):
    """ Returns names of proteins in the genome that contain the specified
        amino acid sequence as a subsequence.

        genome: full genome of particular strain,
                currently, I use genome from load_salmonella_genome() in load.py
        query_AA_seq: query amino acid sequence
    """
    if len(genomes) == 0:
        return []
    r = []
    for genome in genomes:
        if query_AA_seq in genome[2]:
            r.append(genome[1])
    return r

def get_levenshtein_distance(s1, s2):
    """ Compute levenshtein distance between given two strings
    """
    if s1 == s2:
        return 0
    # Implement here!
    return 0

def search_genome_levenshtein(genomes, query_AA_seq, matching_threshold):
    """
    """
    # Implement here!

if __name__ == "__main__":
    #print salmonella_genome
    #print search_genome_simple(salmonella_genome, "MRVTIVLVAPARAENIGAAARAMKTMGFTDLRI")
    ## --> ['CAD03431.1']
