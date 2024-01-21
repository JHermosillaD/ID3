#!/bin/python3

from datetime import datetime
import pydot
import uuid
import matplotlib.pyplot as plt
import os
import json

class plotTree_class:
    def __init__(self, tree): 
        self.tree = tree 
        self.cwd = os.getcwd()
        self.data_path = f'{self.cwd}/../data/'

    def generate_unique_node(self):
        return str(uuid.uuid1())
    
    def create_node(self, graph, label, shape='oval', color='white'):
        node = pydot.Node(self.generate_unique_node(), label=label, shape=shape, style = "filled", fillcolor = color)
        graph.add_node(node)
        return node
    
    def create_edge(self, graph, node_parent, node_child, label):
        link = pydot.Edge(node_parent, node_child, label=label)
        graph.add_edge(link)
        return link
    
    def walk_tree(self, graph, dictionary, prev_node=None):
         for parent, child in dictionary.items():
            # root
            if not prev_node: 
                root = self.create_node(graph, parent)
                self.walk_tree(graph, child, root)
                continue            
            # node
            if isinstance(child, dict):
                for p, c in child.items():
                    n = self.create_node(graph, p)
                    self.create_edge(graph, prev_node, n, str(parent))
                    self.walk_tree(graph, c, n)
            # leaf
            else: 
                leaf = self.create_node(graph, str(child), shape='box', color='gold')
                self.create_edge(graph, prev_node, leaf, str(parent))

    def plot_tree(self, csv_file=False):
        now = datetime.now()
        if(csv_file == True):
            print("\nSaving Tree...")
            with open(self.data_path + "output/" + now.strftime("%I%p") + ".json", "w") as fp:
                json.dump(self.tree, fp)  
            print("Done!")
            
        graph = pydot.Dot(graph_type='graph')
        self.walk_tree(graph, self.tree)
        path_temp = self.data_path+"temp/" + now.strftime("%I%p") + ".png"
        graph.write_png(path_temp)
        img_temp = plt.imread(path_temp)
        plt.imshow(img_temp)
        plt.axis('off')
        plt.show()
        os.remove(path_temp) 
