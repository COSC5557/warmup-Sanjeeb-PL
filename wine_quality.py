import pandas as pd
# import the OS module
import os, sys, platform

# import the dataset for red wine from excel file
#filepath = 'winequality-red.csv'
dataset = pd.read_csv('winequality-red.csv', sep = ';')
