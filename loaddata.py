import pickle

dict_file = open('dict.txt', 'rb')
dict = pickle.load(dict_file)
dict_file.close()

ham_file = open('ham_vector.txt', 'rb')
ham = pickle.load(ham_file)
ham_file.close()

spam_file = open('spam_vector.txt', 'rb')
spam = pickle.load(spam_file)
spam_file.close()