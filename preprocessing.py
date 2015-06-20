from nltk import PorterStemmer
from stemming.porter2 import stem
from sets import Set
import os
import sys
import pickle

#stem()
#stemmer.stem()

dictionary = Set()

ham_folder = os.listdir("enron1/ham")
spam_folder = os.listdir("enron1/spam")

for ham_email in ham_folder:
    if ham_email.endswith('.txt'): 
    	f = open('enron1/ham/' + ham_email)
    	for word in f.read().split():
    		#stemming
    		word = unicode(word, errors='ignore')
    		dictionary.add(stem(word))

for spam_email in spam_folder:
    if spam_email.endswith('.txt'): 
    	print spam_email
    	f = open('enron1/spam/' + spam_email)
    	for word in f.read().split():
    		#stemming
    		word = unicode(word, errors='ignore')
    		dictionary.add(stem(word))

dictionary = list(dictionary)
dictionary = sorted(dictionary)

dict_file = open('dict.txt', 'wb')
pickle.dump(dictionary, dict_file)

dict_file.close()

ham = []
#create bag-of words for ham emails
for ham_email in ham_folder:
    if ham_email.endswith('.txt'): 
    	print ham_email
    	email_vec = [0] * len(dictionary)
    	f = open('enron1/ham/' + ham_email)
    	for word in f.read().split():
    		word = unicode(word, errors='ignore')
    		email_vec[dictionary.index(stem(word))] +=1
    	ham.append(email_vec)

ham_file = open('ham_vec.txt', 'wb')
pickle.dump(ham, ham_file)

ham_file.close()

spam = []
#create bag-of words for spam emails
for spam_email in spam_folder:
    if spam_email.endswith('.txt'): 
    	print spam_email
    	email_vec = [0] * len(dictionary)
    	f = open('enron1/spam/' + spam_email)
    	for word in f.read().split():
    		word = unicode(word, errors='ignore')
    		email_vec[dictionary.index(stem(word))] +=1
    	spam.append(email_vec)

spam_file = open('spam_vec.txt', 'wb')
pickle.dump(spam, spam_file)
spam_file.close()
