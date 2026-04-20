import pandas as pd
import numpy as np
import ast
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
data = []
with open('C:\\Users\\ASUS\\Desktop\\moive1M20221009random.txt') as f:
    for line in f:
        line = line.strip()#去掉每行后面的/n
        row = ast.literal_eval(line)#安全的字符串到 Python 对象的转换
        data.append(row)
df = pd.DataFrame(data,columns=['用户编号','产品编号','评分'])
indf = df.pivot(index='用户编号',columns='产品编号',values='评分')#pivot:将长格式数据转换为宽格式
car_matrix = indf.fillna(0)
print(car_matrix.shape)
print(car_matrix)
car_matrix.to_csv('C:\\Users\\ASUS\\Desktop\\接收（moive）.csv',encoding='utf-8-sig')