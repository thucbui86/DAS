import pandas as pd

data = pd.read_csv("OnlineRetail.csv")
# print(data.head())
# print(data.info())
# lấy ra tên các quốc gia
countries = data.Country.unique()
print("số lượng các quốc gia:" + str(countries.size))  
# Tạo cột tính thành tiền của các mặt hàng
data['total'] = data['Quantity'] * data['UnitPrice']
# Giá trị đơn hàng của mỗi đơn hàng
total_invoices = data['total'].sum()
print ("số lượng hóa đơn bán ra: "+ str (total_invoices.size))
print ("Tổng doanh thu: " + str(total_invoices.sum()))
# Tốp 10 sản phẩm bán ra lớn nhất
quantity_product = data.groupby(['StockCode',
'Description'])['Quantity'].sum().sort_values(ascending= False)
print(quantity_product.head(10))

# Top 10 mặt hàng có doanh thu lớn nhất
total_product = data.groupby(['StockCode',
'Description'])['total'].sum().sort_values(ascending= False)
print(total_product.head(10))