import pandas as pd
import matplotlib.pyplot as plt

excel_file = "shintyou_taijyuu.xlsx" 
df = pd.read_excel(excel_file)

plt.scatter(df['shintyou'], df['taijyuu'])  
plt.title("S-T_data")
plt.xlabel("shintyou") 
plt.ylabel("taijyuu")  
plt.grid(True)
plt.show()