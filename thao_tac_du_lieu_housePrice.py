from itertools import groupby
from statistics import mean
import pandas as pd
import numpy as np

# 1.Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_excel("house_price_dống-da.xlsx")
print(df.head())
print(df.info())

# 2.Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
df1 = df[(df["type_of_land"] ==  "Bán nhà riêng") & ((df["street_name"] == "Phố Trung Liệt") | (df["street_name"] == "Phố Khâm Thiên"))]
print(df1.head())

# 3.Lọc các thông tin Địa chỉ, Giá, Hướng nhà,
# Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.
df2 = df[(df['land_certificate'] == 'Sổ đỏ') & (df['bedroom'] >= 3)]
df3 = df2[['address', 'price', 'house_direction', 'balcony_direction']]
print(df3.head())

#4. Với mỗi loại nhà đất, 
# tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
target1 = df.groupby(df['type_of_land']).agg({'price': ['mean', 'min', 'max']})
print(target1)

# 5. Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.
target2 = df.groupby(df['ward_name']).agg({'bedroom': np.mean, 'toilet': np.mean, 'floor': np.mean })
print(target2)
