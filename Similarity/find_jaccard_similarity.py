import numpy as np
from sklearn.metrics import jaccard_similarity_score
A = [1,1,0,1,0,0,1,0]
B = [0,1,1,1,0,0,0,0]
C = [0,0,0,1,0,1,1,1]
N = [1,0,0,1,0,0,1,0]
print 'AN=',jaccard_similarity_score(A,N)
print 'BN=',jaccard_similarity_score(B,N)
print 'CN=',jaccard_similarity_score(C,N)


m1 = [1,0,1,0,0,0]
m2 = [1,1,1,0,1,0]
m3 = [1,1,0,0,0,0]
m4 = [0,0,0,1,1,0]
m5 = [0,1,0,1,1,1]
m6 = [0,0,0,0,1,1]

t1 = [0,0,0,1,0,1]
print 'test 1'

print 't1m1=',jaccard_similarity_score(t1,m1)
print 't1m2=',jaccard_similarity_score(t1,m2)
print 't1m3=',jaccard_similarity_score(t1,m3)
print 't1m4=',jaccard_similarity_score(t1,m4)
print 't1m5=',jaccard_similarity_score(t1,m5)
print 't1m6=',jaccard_similarity_score(t1,m6)


t2 = [0,1,1,0,0,0]
print 'test 2'

print 't2m1=',jaccard_similarity_score(t2,m1)
print 't2m2=',jaccard_similarity_score(t2,m2)
print 't2m3=',jaccard_similarity_score(t2,m3)
print 't2m4=',jaccard_similarity_score(t2,m4)
print 't2m5=',jaccard_similarity_score(t2,m5)
print 't2m6=',jaccard_similarity_score(t2,m6)
