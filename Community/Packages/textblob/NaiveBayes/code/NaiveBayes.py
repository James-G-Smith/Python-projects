# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier

import pandas

trainpath="../data/train.csv"
testpath="../data/test.csv"

#Open training data and train model
with open(trainpath) as csvfile_a:
    cl = NaiveBayesClassifier(csvfile_a, format="csv")
    
def classifier(alpha):
    
    if str(alpha)=="nan":
        beta=""
        return beta
    else:
    
        beta=cl.classify(alpha)
        return beta

#read the test file in
df = pandas.read_csv(testpath, encoding='utf-8')

# Here is the original table
print(df)

#Enter name of new column and column you want to classify
df["N/P"] = df["Sentence"].apply(classifier)
print(df)

#This is here to test string on their own
print(cl.classify("James is the best"))

#test the accuracy of your train
with open('../data/train.csv', 'r') as train:
    print(cl.accuracy(train))