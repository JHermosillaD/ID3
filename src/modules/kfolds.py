#!/bin/python3

from sklearn.model_selection import KFold
from timeit import default_timer as timer
from modules.id3 import id3_class
import pandas as pd

class kfold_class:
    def __init__(self, df, df_name): 
        self.df = df 
        self.df_name = df_name

    '''Estimate class given an instance'''
    def Predict(self, tree, instance):
        if not isinstance(tree, dict): 
            return tree 
        else:
            root_node = next(iter(tree)) 
            attribute_value = instance[root_node] 
            if attribute_value in tree[root_node]: 
                return self.Predict(tree[root_node][attribute_value], instance) 
            else:
                return None
            
    '''Calculate accuracy given a dataset'''
    def Accuracy(self, tree, df_test):
        class_label = df_test.keys()[-1]
        correct_preditct = 0
        wrong_preditct = 0
        for index, row in df_test.iterrows():
            predicted_class = self.Predict(tree, df_test.iloc[index]) 
            if predicted_class == df_test[class_label].iloc[index]:
                correct_preditct += 1 
            else:
                wrong_preditct += 1
        accuracy = correct_preditct / (correct_preditct + wrong_preditct) 
        return accuracy

    '''Average accuracy, leaf nodes and train duration'''
    def kfold_validation(self, n):  
        kf = KFold(n_splits=n, shuffle=True)
        results = []
        results2 = []
        for i, (t_ind, v_ind) in enumerate(kf.split(self.df)):
            train = self.df.iloc[t_ind]
            valid = self.df.iloc[v_ind] 
            start = timer()
            df_tree = id3_class(self.df, self.df_name).Create_tree(train)
            end = timer()
            accuracy = self.Accuracy(df_tree, valid.reset_index())
            nodes = id3_class(self.df, self.df_name).LeafNodes(df_tree)
            results2.append(nodes)
            results.append(accuracy)
        score = sum(results) / len(results)
        leafnodes = sum(results2) / len(results2)

        d = {1: [self.df_name, score, leafnodes, end-start]}
        print ("{:<15} {:<15} {:<15} {:<15} ".format('Dataset','Avg score','Avg leafs', 'Avg time'))
        for k, v in d.items():
            lang, perc, change, t = v
            print ("{:<15} {:<15} {:<15} {:<15}".format(lang, perc, change, t))