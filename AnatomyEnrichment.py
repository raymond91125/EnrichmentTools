 # /usr/bin/env python
 # -*- coding: utf-8 -*-
"""
Author: Raymond Lee
Date: January 29, 2016
A script to implement a hypergeometric test for WBbt anatomy enrichment
based on gene expression pattern annotations.
Needs:
A gene/tissue dictionary
A list of gene names to query
"""

import os
import sys, getopt
os.environ['MPLCONFIGDIR']='/tmp'
sys.path.append('../tissue_enrichment_tool_hypergeometric_test') \
# location of the test library

import matplotlib
matplotlib.use('Agg') 

import pandas as pd
from scipy import stats

from hypergeometricTests \
import implement_hypergmt_enrichment_tool as hgt

# for arg in sys.argv:
#     print arg

q_threshold=0.1
# q_threshold= 0.018
# in the case of anatomical expression patterns, \
# there are ~5000 genes total in the dictionary whereas a tissue has \
# minimally 100 genes. Thus, if the input contains a singleton gene, \
# the p can be as low as 0.02 for tissues that does not express that \
# gene at all. It makes no sense to say that the tissue is enriched.


path= "./"
os.chdir(path)
if len(sys.argv) == 2:
    gene_file = sys.argv[1]
#    q_threashold = sys.argv[2]
else:
    exit("Must specify a gene list. Bye")
genes1= pd.read_csv(gene_file) #this file should be only wormbase ID's!
print "using file ", gene_file

#extract the first column of the file as a list of strings for analysis
gene_list1= genes1[genes1.columns[0]].values

#read in the dictionary
tissue_df= pd.read_csv("/home/raymond/local/src/git/tissue_enrichment_tool_hypergeometric_test/input/dictionary_anatomy.csv")

hgt(gene_list=gene_list1, tissue_df=tissue_df)

