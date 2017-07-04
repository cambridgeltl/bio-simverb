from scipy.stats import spearmanr
from scipy.stats import pearsonr
import itertools
import numpy as np
import sys, os, codecs
import collections

def read_file(filename):
    lexicon =  collections.OrderedDict()
    lex2 =  collections.OrderedDict()
    extrinTask1 = "average"
    extrinTask2 = "Hallmark-CNN"
    #with codecs.open(filename, encoding='utf-8') as i:
    with open(filename) as i:
        for i, line in enumerate(i):
            line = line.strip().split("\t")
            word = line[0].strip()
            result = [float(t) for t in line[1:]]
            #print word, word == extrinTask1, word == extrinTask2
            if word == extrinTask2 or word == extrinTask1:
                lex2[word] = result
            else:
                lexicon[word] = result
    return lexicon, lex2


if __name__=='__main__':
    path = "data.txt"
    dataSize = 10
    lex1, lex2= read_file(path)
    # for k, v in lex1.items():
    # 	print k, v 
    # for k, v in lex2.items():
    # 	print k, v 

 #    a = np.array([-2, 1, 5, 3, 8, 5, 6])
    # b = [1, 2, 5]
    # print list(a[b])
    print "lex1.values()", len(lex1.values()), len(lex2.values())
    for i in range(5,dataSize):
        index_list=list(itertools.combinations(range(dataSize), i))
        for index in index_list:
            #print index
            a = [int(i) for i in index]
            intrinsic = [np.array(val)[a] for val in lex1.values()]
            extrinsic = [np.array(val2)[a] for val2 in lex2.values()]
            #print len(intrinsic)
            #print len(extrinsic)
            in_corr = [(float("{0:.2f}".format(spearmanr(in_score, extrinsic[0])[0])),\
                        float("{0:.2f}".format(spearmanr(in_score, extrinsic[1])[0])))for in_score in intrinsic]
            if in_corr[0][0] >=0.5 and in_corr[0][1] >=0.5 and in_corr[1][0] >=0.5 and in_corr[1][1] >=0.5:
            	#if in_corr[0][0] <= in_corr[0][1] and in_corr[1][0] <= in_corr[1][1]:
                print in_corr
                print [i+1 for i in index]
                print "\n"


