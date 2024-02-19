import csv
import pandas as pd

def using_csv(filepath):
    with open(filepath, newline='') as csvf: #if newline not specified, newlines wont be intepreted correctly
        reader = csv.reader(csvf, delimiter=',', quotechar='"')
        for row in reader:
            print(row)

def using_pandas(filepath):
    df = pd.read_csv(filepath, names=["ID", "Device"]) #custom headers
    print(df["Device"]) #we can get data from a colum
    df.sort_values(["ID", "Device"], ascending=[True, False]) #can specify how we want data to be sorted
    print(df['Device'].unique()) #print all unique values
    print(df["Devices"].describe()) #print the descriptive statistics of the field 

