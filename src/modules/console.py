#!/bin/python3

from simple_term_menu import TerminalMenu
import pandas as pd
import os

class interface_class: 
    def __init__(self):
        self.cwd = os.getcwd()
        self.data_path = f'{self.cwd}/../data/datasets/'
        self.options = ["Iris-setosa","Car evaluation","Tic-tac-toe","Chess","Play Tennis"]
        self.baner = """
██╗██████╗ ██████╗ 
██║██╔══██╗╚════██╗
██║██║  ██║ █████╔╝
██║██║  ██║ ╚═══██╗
██║██████╔╝██████╔╝
╚═╝╚═════╝ ╚═════╝ \n
"""

    '''Generate dataframe'''
    def load_df(self):
        terminal_menu = TerminalMenu(self.options,title=self.baner+"Select dataset:\n",clear_screen=True)
        menu_entry_index = terminal_menu.show()
        if self.options[menu_entry_index] == 'Iris-setosa':
            df = pd.read_csv(self.data_path+'D1_iris/iris.csv')
        elif self.options[menu_entry_index] == 'Car evaluation':
            df = pd.read_csv(self.data_path+'D2_car_evaluation/car.csv')
        elif self.options[menu_entry_index] == 'Tic-tac-toe':
            df = pd.read_csv(self.data_path+'D3_tic_tac_toe/tic-tac-toe.data')
        elif self.options[menu_entry_index] == 'Chess':
            df = pd.read_csv(self.data_path+'D4_chess_KRKPA7/kr-vs-kp.csv')
        elif self.options[menu_entry_index] == 'Play Tennis':
            df = pd.read_csv(self.data_path+'D5_PlayTennis/PlayTennis.csv')
        df_name = self.options[menu_entry_index]
        print(self.baner)

        return df, df_name