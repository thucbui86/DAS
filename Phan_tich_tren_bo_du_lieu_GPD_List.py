import pandas as pd

# 1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv('GDPlist.csv')
print(df.head())
print(df.info())

# 2. Việt hóa tên các cột trong bảng dữ liệu: 
##   Country 🡪 Nuoc; Continent 🡪 Chauluc; GDP (millions of US$) 🡪 GDP (trieu $)
df.rename(columns = {'Country': 'nuoc', 'Continent': 'Chauluc', 'GDP (millions of US$)': 'GDP (trieu $)'}, inplace = True)
print(df.head())

# 3.Chèn thêm một cột “Thanhpho” vào sau cột “Nuoc”, 
# giá trị ban đầu là giá trị của cột “Nuoc”
df.insert(1, 'Thanhpho', pd.Series(df['nuoc'], index = df.index))
print(df.tail())

# 4. Trong cột Thanhpho, thay giá trị  Vietnam thành Hanoi; Làm tương tự với các nước còn lại.
df.loc[df['Thanhpho'] == 'Vietnam', 'Thanhpho'] = 'Hanoi'
print(df.tail())

# 5.Xóa các bản ghi có Chauluc là ‘Asia’
df.drop(df[df['Chauluc'] == 'Asia'].index, inplace = True)
print(df.head())

# 6. Xóa các bản ghi có GDP < 300000
df.drop(df[df['GDP (trieu $)'] < 300000].index, inplace= True)
print(df.head())