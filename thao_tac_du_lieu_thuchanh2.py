import pandas as pd
df=pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
print(df)

# Để đơn giản ta thực hiện lọc tập dữ liệu ban đầu theo các thuộc tính sau
df = df[['date_collected','shop_location','response_time']]
print(df)

# Tách cột shop_location thành 2 cột District và City
df['District']=df['shop_location'].str.split(',').str[0]
df['City']=df['shop_location'].str.split(',').str[1]
print(df)

# Tách cột response_time thành 3 cột Hour, Minute, Second
df['Hour']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.hour
df['Minute']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.minute
df['Second']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.second
print(df)