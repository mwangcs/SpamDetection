import sys
import pickle
from stemming.porter2 import stem
import numpy as np
import math

testfile = open(sys.argv[1], 'rb')

dict_file = open('dict.txt', 'rb')
dict = pickle.load(dict_file)
dict_file.close()

#generate vector for test email
email_vec = [0] * len(dict)
for word in testfile.read().split():
	word = stem(unicode(word, errors='ignore'))
	#ignore OOV words
	if word in dict:
		email_vec[dict.index(word)] +=1

#makes prediction
x = np.array(email_vec)
x = np.append(x,1)
w_file = open('w_file.txt', 'rb')
w = pickle.load(w_file)

predict = 1/(1+math.exp(-sum(x*w)))

if predict > 0.5:
	print 1
else:
	print 0