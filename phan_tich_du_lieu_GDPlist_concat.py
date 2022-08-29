import pandas as pd
import numpy as np

# 1.Đọc bộ dữ liệu, cho biết số dòng, 
# số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv('GDPlist.csv')
print(df.head())
print(df.info())

# 2. Tính giá trị lớn nhất và nhỏ nhất của GDP.
df.rename(columns = {'Country': 'nuoc', 'Continent': 'Chauluc', 'GDP (millions of US$)': 'GDP'}, inplace = True)
print(df.head())
print('Giá trị lớn nhất của GDP:', df.loc[:,'GDP'].max())
print('Giá trị nhỏ nhất của GDP:', df.loc[:,'GDP'].min())

# 3. Hãy cho biết xu hướng phân bố dữ liệu của GDP.
print('Giá trị trung bình của GDP', df.loc[:,'GDP'].mean())
print('Giá trị trung vị của GDP:', df.loc[:,'GDP'].median)
print('Giá trị xuất hiện nhiều nhất của GDP:', df.loc[:,'GDP'].mode)

    # xuat ra GDP cua nuoc afghanistan
tget = df[df["nuoc"]=='Afghanistan']
print(tget)

# 4.Hãy cho biết châu lục nào xuất hiện nhiều nhất?
target = df.groupby(["Chauluc"])["Chauluc"].value_counts()
print(target)

# 5. Với mỗi châu lục hãy tính tổng GDP; 
# trung bình cộng GDP. 
# Hợp nhất 2 bảng này thành một bảng duy nhất gồm 3 thông tin: 
# Tên châu lục; Tổng GDP; TBC GDP.
pivot_chauluc = pd.pivot_table(data= df, index= ['Chauluc'], values= 'GDP', aggfunc = ['sum', 'mean'])
print(pivot_chauluc)