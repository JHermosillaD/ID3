#!/bin/python3

from modules import __version__
from modules.console import interface_class
from modules.kfolds import kfold_class

def main():    
    # Load dataset
    console = interface_class()
    df, name = console.load_df()
    # Validate using dataset with k-folds
    kfold = kfold_class(df, name)
    kfold.kfold_validation(10)

if __name__ == "__main__":
    main()