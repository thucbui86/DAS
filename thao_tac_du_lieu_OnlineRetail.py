import numpy as np
import pandas as pd


# 1.Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv("OnlineRetail.csv")
# print(df.head())
print(df.info())

# 2. Tạo cột mới có tên quý –  ‘Previous’ 
# nhận giá trị 1 nếu ngày lập hóa đơn nằm trong các tháng 1,2,3; 
# nhận giá trị 2 nếu ngày lập hóa đơn nằm trong các tháng 4,5,6; 
# nhận giá trị 3 nếu ngày lập hóa đơn nằm trong các tháng 7,8,9;  
# nhận giá trị 4 nếu ngày lập hóa đơn nằm trong các tháng 10,11,12

df[["day", "mm", "year"]] = df["InvoiceDate"].str.split("/", expand=True)
print(df.info())
conditions = [(df['mm'] == '1') | (df['mm'] == '2') | (df['mm'] == '3'), 
              (df['mm'] == '4') | (df['mm'] == '5') | (df['mm'] == '6'), 
              (df['mm'] == '7') | (df['mm'] == '8') | (df['mm'] == '9'), 
              (df['mm'] == '10') | (df['mm'] == '11') | (df['mm'] == '12')]
choices = ['1', '2', '3', '4']
df['Previous'] = np.select(conditions, choices, default= None)
print(df['Previous'])

# 3.Tạo một cột mới có tên ‘Amount’ có giá trị bằng Quantity * UnitPrice
df['Amount'] = df['Quantity'] * df['UnitPrice']
print(df['Amount'])

# 4.Tạo cột mới ‘Discount’ nhận giá trị 10% nếu Country là ‘United Kingdom’ và thuộc quý 4,
# 5% nếu là ‘France’ ngược lại là 0%.
df['Discount'] = np.nan
condition2 = [(df['Country'] == 'United Kingdom') & (df['Previous'] == '4'),
              (df['Country'] == 'France'),
              (df['Country'] != 'France') & (df['Country'] != 'France')
              ]
choice2 = [0.1, 0.05, 0]
df['Discount'] = np.select(condition2, choice2, default= None)
print(df['Discount'])

# 5.Tạo cột mới ‘Total’ nhận giá trị bằng: Amount – Discount.
df['Total'] = df['Amount'] - df['Discount']
print(df['Total'])