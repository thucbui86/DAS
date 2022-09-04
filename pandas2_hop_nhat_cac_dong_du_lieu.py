# Đọc file dữ liệu 'FoodPrice_in_Turkey.csv'
import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.head())

# Tách file 1 chứa 5000 bản ghi đầu tiên
df1 = df.loc[0:4999,:]
print(df1.head())

# Tách file 2 chứa các bản ghi còn lại
df2 = df.loc[5000:7380,:]
print(df2.head())

# Tách file 3 chứa thông tin giá với số dòng từ bản ghi 1000 đến 2000
df3 = df.loc[1000:2000,['ProductId','Place','Month','Year','Price']]
print(df3.head())

#2. Ghép các dòng từ các file
df4=pd.concat([df1,df2], axis=0)
print(df4.head())

df5=pd.concat([df1,df2,df3], axis=0)
print(df5.head())
print(df5.head())

df6=df1.append(df2)
print(df6.head())

df7=df1.append(df3)
print(df7.head())