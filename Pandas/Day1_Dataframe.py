#pandas.DataFrame(data, index, columns, dtype, copy)
import pandas as pd
data=[["Alex",10],["Bob",12],["Clarke",13]]
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)