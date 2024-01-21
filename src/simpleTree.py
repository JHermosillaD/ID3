#!/bin/python3

from modules import __version__
from modules.console import interface_class
from modules.id3 import id3_class
from modules.plottree import plotTree_class

def main():    
    # Load dataset
    console = interface_class()
    df, name = console.load_df()
    # Generate decision tree 
    id3 = id3_class(df, name)
    tree = id3.Create_tree(df)
    id3.Show_report(tree)
    # Display and save tree
    plt_tree = plotTree_class(tree)
    plt_tree.plot_tree(csv_file=True)

if __name__ == "__main__":
    main() 