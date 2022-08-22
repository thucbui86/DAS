import pandas as pd
import matplotlib.pyplot as plt

foodprice = pd.read_csv('FoodPrice_in_Turkey.csv')
print(foodprice.head())

# số dòng và cột của bộ dữ liệu
print(foodprice.shape)

# kiểm tra thông tin bộ dữ liệu
print(foodprice.info())

# giá trung bình của từng loại thực phẩm
print('Giá trị trung bình của từng loại sản phẩm:')
giatriTB = foodprice.groupby(['ProductName'])['Price'].mean()
print(giatriTB)
