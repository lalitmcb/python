import pandas as pd

#install xlrd module to support excel.
#In python 3 use: pip3 install xlrd
#read the excel file by giving name and sheet
excel_df = pd.read_excel('titanic.xls',sheetname=0)
print(excel_df.head())

#Writing the csv file out
#By default index also goes in csv. It can be ignored
#sep is optional. By default it's comma
excel_df.to_csv('titanic.csv',index=False,sep=',')

#Reading the csv file is similar
#Let's read the same csv file that we generated
csv_df = pd.read_csv('titanic.csv')
print(csv_df.head())

