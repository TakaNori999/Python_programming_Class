import pandas as pd

file = "test_data.xlsx"  
df = pd.read_excel(file)
#df = df.iloc[:, 1:]

correlation_matrix = df.corr().round(2)
print(correlation_matrix)
