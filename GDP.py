import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file .csv
data = pd.read_csv("GDPlist.csv")
print(data.head())
# số dòng, số cột trong bộ dữ liệu
print(data.shape)
# Thang đo tương ứng của các thuộc tính lưu trữ
print(data.dtypes)
# tính các giá trị thống kê của bộ dữ liệu
print(data.describe())
print('giá trị trung bình:' + str(data['GDP (millions of US$)'].mean()))
print('giá trị trung vị:' + str(data['GDP (millions of US$)'].median()))

# biểu đồ kiểm tra tính đồng đều của dữ liệu
plt.hist(data['GDP (millions of US$)'])
plt.show() 

# Số quốc gia trong châu lục
quantity_countries = data.groupby(['Continent'])['Country'].size()
print("số quốc gia của mỗi châu lục:")
print(quantity_countries)

# Tổng GDP của mỗi châu lục
print('tổng GDP của mỗi châu lục:')
GDP_continent = data.groupby(['Continent']).sum()
print(GDP_continent)

# Top 10 quốc gia có GDP cao nhất
print("Top 10 quốc gia có GDP cao nhất:")
GDP_Max = data.sort_values('GDP (millions of US$)', ascending = False)
print(GDP_Max.head(10))
