'''
Created on 18 Nov 2016

@author: Billy
'''

import sys
import gensim
import argparse
import numpy as np
# encoding=utf8
reload(sys)
sys.setdefaultencoding('utf8')

def compat_splitting(line):
    if sys.version > "3":
        return line.split()
    else: # if version is 2
        return line.decode('utf8').split()
    
def readVec(path):
    vectors = {}
    fin = open(args.modelPath, 'r')
    for i, line in enumerate(fin):
        try:
            tab = compat_splitting(line)
            vec = np.array(tab[1:], dtype=float)
            word = tab[0]
            if not word in vectors:
                vectors[word] = vec
        except ValueError:
            continue
        except UnicodeDecodeError:
            continue
    fin.close()
    return vectors

def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def differenece(a,b):
    '''return words appear on either one model'''
    return list(set(a).difference(set(b))), list(set(b).difference(set(a)))

# def print_word_vecs(wordVectors, outFileName):
#     sys.stderr.write('\nWriting down the vectors in '+outFileName+'\n')
#     outFile = open(outFileName, 'w')  
#     for word, values in wordVectors.iteritems():
#         outFile.write(word+' ')
#         for val in wordVectors[word]:
#             outFile.write('%.13f' %(val)+' ')
#             outFile.write('\n')      
#     outFile.close()
  
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default=None, help="filter dict")
    parser.add_argument("-m", "--model", type=str, default=None, help="word vec")
    parser.add_argument("-o", "--output", type=str, help="Output word vecs")
    args = parser.parse_args()
    d = {}
    
    model = gensim.models.Word2Vec.load_word2vec_format(args.model, binary=False)
    Join_RCM_model = gensim.models.Word2Vec.load_word2vec_format(args.input, binary=False)
    intersectionModel = intersect(Join_RCM_model.vocab, model.vocab)
    onlyJoin_RCM, onlyModel = differenece(Join_RCM_model.vocab, model.vocab)
    ndim = model.syn0.shape[1]
    Jdim = Join_RCM_model.syn0.shape[1]
    assert ndim==Jdim
    wordsLen = len(onlyModel) + len(onlyJoin_RCM) + len(intersectionModel)
    #print wordsLen, ndim
    
    unionModel = union(Join_RCM_model.vocab, model.vocab)
    assert len(unionModel) == wordsLen
    for item in onlyJoin_RCM: 
        print item,  ' '.join(map(str, Join_RCM_model[item].tolist()))
    for item in onlyModel:
        print item,  ' '.join(map(str, model[item].tolist()))
    for item in intersectionModel:
        print item,  ' '.join(map(str, Join_RCM_model[item].tolist()))
        
        
    # debug, assert len(union model) == wordsLen:
    # unionModel = union(Join_RCM_model.vocab, model.vocab)    
#     print len(model.vocab), len(Join_RCM_model.vocab)
#     print len(unionModel), len(intersectionModel)
    