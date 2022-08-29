import pandas as pd
import numpy as np

# 1.Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv('OnlineRetail.csv')
print(df.head())
print(df.info())

# 2.Xây dựng bảng Pivot table, 
# với mỗi Số hóa đơn tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia. 
df_pivot_hoadon = pd.pivot_table(data= df, index= ['InvoiceNo'],columns= ['Country'], values= 'Quantity', aggfunc='mean' )
print(df_pivot_hoadon)

# 3. Xây dựng bảng Pivot table, 
# với mỗi Khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo Kho.
df_pivot_khachhang = pd.pivot_table(data= df, index=['CustomerID'], columns=['StockCode'], values='Quantity', aggfunc=['max', 'min'])
print(df_pivot_khachhang)

# 4. Xây dựng bảng Pivot table, 
# với mỗi Mã kho tính tổng số lượng các mặt hàng và trung bình cộng giá.
df_pivot_MaKho = pd.pivot_table(data= df, index = ['StockCode'], values= ['Quantity', 'UnitPrice'], aggfunc={'Quantity': 'sum', 'UnitPrice': 'mean'} )
print(df_pivot_MaKho)

# 5. Xây dựng bảng Pivot table cho biết tổng số lượng hàng bán được của mỗi ngày
df_pivot_date = pd.pivot_table(data= df, index=['InvoiceDate'], values='Quantity', aggfunc=['sum'])
print(df_pivot_date)