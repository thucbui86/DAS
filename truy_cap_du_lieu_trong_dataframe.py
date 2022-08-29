import pandas as pd

# Đọc dữ liệu vào DataFrame
df = pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.head())

# Truy cập dòng có chỉ số 3 của dữ liệu
print(df.iloc[3])

# Truy cập các dòng có chỉ số liên tục từ 3 tới 8 của dữ liệu
print(df.iloc[3:8])

# Truy cập các dòng rời rạc của dữ liệu
print(df.iloc[[3,5,7]])

# Truy cập cột thứ 4 của dữ liệu
# : được sử dụng để đại diện cho tất cả các dòng.
print(df.iloc[:,4])

# Truy cập các cột liên tục từ cột 3 tới cột 8 của dữ liệu
print(df.iloc[:,3:8])

# Truy cập tới phần tử tại dòng 3 cột 7 của dữ liệu
print(df.iloc[3,7])

# Truy cập tới các phần tử từ dòng 3 đến dòng 4, cột 5 đến cột 6 của dữ liệu
print(df.iloc[3:5,5:7])

# Truy cập dòng có chỉ số 3 của dữ liệu
print(df.loc[3])

# Truy cập cột thứ 4 của dữ liệu
print(df.loc[:,'UmName'])

# Truy cập cột thứ 4,5 của dữ liệu
print(df.loc[:,['UmName','Month']])

# Truy cập tới phần tử tại dòng 3 cột 7 của dữ liệu
print(df.loc[3,'Price'])

# Truy cập tới phần tử có Year >=2019
print(df.loc[df.Year >= 2019])

# Thay số 5 bằng số 10 trong toàn bộ dữ liệu
df.replace(5,10,inplace = True)
print(df.head())

# Thay mã sản phẩm từ giá trị 52 thành RR trong toàn bộ dữ liệu
# RR là chuỗi ký tự nên được để trong cặp dấu nháy đơn
df.replace(52,'RR',inplace = True)
print(df.head())

# Thay giá trị 10 trong cột Month thành giá trị 5
df['Month'].replace(10,5,inplace = True)
print(df.head())