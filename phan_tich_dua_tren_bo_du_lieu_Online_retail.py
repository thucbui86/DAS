import pandas as pd
import numpy as np

# 1.Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv('OnlineRetail.csv')
print(df.head())
print(df.info())

# 2.Trích xuất dữ liệu các cột Description và Quantity lưu vào file OnlineRetail.csv
df.to_csv('demo_OnlineRetail.csv', columns=['Description', 'Quantity'])

# 3.Trích xuất dữ liệu 1000 dòng đầu tiên lưu vào file OnlineRetail.xlsx
# df = df.head(1000)
df.iloc[:1000, :].to_excel('demo_OnlineRetail.xlsx')

# 4. Trích xuất các bản ghi có số lượng từ 10 trở lên lưu vào file OnlineRetail.h5
# df = df.loc[df['Quantity'] >= 10]
# df.to_hdf('demo_OnlineRetail.h5', 'table')

# 5.Trích xuất dữ liệu các phần tử từ dòng 1000 đến dòng 2000, 
# các cột Quantity, InvoiceDate, UnitPrice lưu vào file OnlineRetail.json
df.loc[1000:2001,'Quantity':'UnitPrice'].to_json('demo_OnlineRetail.json')

# 6. Trích xuất các bản ghi có số hóa đơn ‘536365’ lưu vào file OnlineRetail.html
df.loc[df['InvoiceNo'] == '536365'].to_html('demo_OnlineRetail.html')
# print(df.loc[df['InvoiceNo'] == '536365'])