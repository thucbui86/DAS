# Đọc file dữ liệu 'FoodPrice_in_Turkey.csv'
import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.head())

# Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, giữ chỉ số ban đầu của các dòng
df=df.drop_duplicates(['ProductId'], keep='last')
print(df.head())

# Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, thiết lập lại chỉ số
df=df.drop_duplicates(['ProductId'], keep='last').reset_index(drop=True)
print(df.head())

# Tách file chứa thông tin sản phẩm
df_pro = df.loc[:,['ProductId','ProductName','UmId','UmName']]
print(df_pro.head())

# Tách file chứa thông tin giá với số dòng từ bản ghi 10 đến 20
df_pri10 = df.loc[10:20,['ProductId','Place','Month','Year','Price']]
print(df_pri10.head())

# 2. Ghép các cột từ các file có chung 1 thuộc tính
df1=pd.merge(df_pro, df_pri10, on='ProductId')
print(df1.head())

df2=pd.concat([df_pro,df_pri10], axis=1)
print(df2.head())

df2=pd.concat([df_pro,df_pri10,df_pri10], axis=1)
print(df2.head())



