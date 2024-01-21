#!/bin/python3

from numpy import log2 as log
import numpy as np 
import sys
sys.setrecursionlimit(10000)

class id3_class:
    def __init__(self, df, name): 
        self.df = df
        self.name = name
        self.eps = np.finfo(float).eps

    '''Total entropy H(T) '''
    def Total_entropy(self, df):
        entropy = 0
        class_label = df.keys()[-1]
        class_values = df[class_label].unique()
        for value in class_values:
            probability = df[class_label].value_counts()[value]/len(df[class_label])
            entropy += -probability*np.log2(probability)
        return entropy
    
    '''Conditional entropy per feater-value Sum H(T|a=v)'''
    def Conditional_entropy(self, df, attribute):
        sum_entropy = 0
        class_label = df.keys()[-1] 
        class_values = df[class_label].unique()  
        attribute_values = df[attribute].unique()  
        for value in attribute_values:
            entropy = 0
            for class_val in class_values:
                values_per_class = len(df[attribute][df[attribute]==value][df[class_label] ==class_val])
                no_values = len(df[attribute][df[attribute]==value])
                probability = values_per_class/(no_values+self.eps)
                entropy += -probability*log(probability+self.eps)
            sum_entropy += -(no_values/len(df))*entropy
        return abs(sum_entropy)

    '''Feature with highest gain Max(a)'''
    def Best_feature(self, df):
        IG = []
        for key in df.keys()[:-1]:
            IG.append(self.Total_entropy(df)-self.Conditional_entropy(df,key))
        return df.keys()[:-1][np.argmax(IG)]

    '''Create tree'''
    def Create_tree(self, df,tree=None): 
        class_label = df.keys()[-1]   
        node = self.Best_feature(df)
        attValue = np.unique(df[node])
        if tree is None:                    
            tree={}
            tree[node] = {}
        
        for value in attValue:    
            subtable = df[df[node] == value].reset_index(drop=True)
            clValue,counts = np.unique(subtable[class_label],return_counts=True)                        
            if len(counts)==1:
                tree[node][value] = clValue[0]                                                    
            else:        
                tree[node][value] = self.Create_tree(subtable)          
        return tree

    ''' Counting nummber of leaf nodes'''
    def LeafNodes(self, tree):
        nodes = 0 
        for key, value in tree.items():
            if isinstance(value, dict):
                nodes += self.LeafNodes(value)
            else:
                nodes += 1
        return nodes
    
    '''Display results'''
    def Show_report(self, tree):
        nodes = self.LeafNodes(tree)
        root = next(iter(tree))
        d = {1: [self.name, root, nodes]}
        print ("{:<15} {:<15} {:<8} ".format('Dataset','Root','Leafs'))
        for k, v in d.items():
            lang, perc, change = v
            print ("{:<15} {:<15} {:<8}".format(lang, perc, change))