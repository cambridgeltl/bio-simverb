from scipy.stats import spearmanr
from scipy.stats import pearsonr


# compute correlation between intrinsic and extrinsic score
'''
e.g for a set of vector: 
#its intrinsic scores (e.g. bio-simverb):
#win1 0.59
#win2 0.48
#win4 0.44
#win5 0.02 

#its extrinsic scores (e.g. bc2gm):
#win1 69.14
#win2 69.56
#win4 69.88
#win5 70.11

'''
result_in=[0.59,0.48,0.44, 0.02] ## intrinsic score
result_ex=[69.14, 69.56, 69.88, 70.11] # extrinsic score

print "correlation between intrinsic-extrinsic score:", spearmanr(result_in, result_ex)[0]
