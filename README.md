# Spam Email Detector
Approach
------
Stem using function stem from python package stemming, module porter2.
Construct dictionary as set of all Unicode-converted, stemmed ham and spam email words.
Convert documents to vectors using (stemmed) dictionary-word in-document frequencies. Augments vectors	with 1 for bias.
Train the model using logistic regression by gradient descent with regularization.

Evaluation
------
92.8% recall and 93.2% precison on unseen test data
