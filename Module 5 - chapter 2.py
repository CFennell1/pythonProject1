
import os
wd = os.getcwd()
os.listdir(wd)




########################
# # Import pickle package
# import pickle
#
# # Open pickle file and load data: d
# with open('data.pkl', "rb") as file:
#     d = pickle.load(file)
#
# # Print d
# print(d)
#
# # Print datatype of d
# print(type(d))

##############################
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = "battledeath.xls"

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)