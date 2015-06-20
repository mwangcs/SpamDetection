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
	#ignore those words that are not in the vocabulary
	if word in dict:
		email_vec[dict.index(word)] +=1

x = np.array(email_vec)
w_list = [1] * len(dict)
w = np.array(w_list)

predict = 1/(1+math.exp(-sum(x*w)))
print np.sign(2*predict-1)