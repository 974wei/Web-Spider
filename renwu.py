import pandas as pd
import numpy as np
import ast
import os

pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列
data = []
with open('C:\\Users\\ASUS\\Desktop\\flimtrust20220604random.txt') as f:
    for line in f:
        line = line.strip()#去掉每行后面的/n
        row = ast.literal_eval(line)#安全的字符串到 Python 对象的转换
        data.append(row)
df = pd.DataFrame(data,columns=['用户编号','产品编号','评分'])
indf = df.pivot(index='用户编号',columns='产品编号',values='评分')#pivot:将长格式数据转换为宽格式
cadf = indf.fillna(0)
u = indf.stack().mean() # stack 将二维表格转为 Series(一维)，mean()计算平均值

#用户偏置
user_mean = indf.mean(axis=1) # 每个产品的平均分,用含nan的indf计算
bu = user_mean - u

#产品偏置
item_mean = indf.mean(axis=0) # 每个产品的平均分,用含nan的indf计算
bi = item_mean - u

#残差 / 噪声项    数据过大，用向量计算减少运算时间
u_matrix = u #标量
bu_matrix = bu.values.reshape(-1,1) #(1509,1)的矩阵
bi_matrix = bi.values.reshape(1,-1) #(1,2071)的矩阵
residual = indf - (u_matrix + bu_matrix + bi_matrix)
residual = residual.fillna(0)

#用户统计量
var_u = indf.var(axis=1,ddof=0)#  方差
std_u = indf.std(axis=1,ddof=0)#  标准差

#产品统计量
var_i = indf.var(axis=0,ddof=0)
std_i = indf.std(axis=0,ddof=0)

#用户一致性偏差
zu = (indf - user_mean.values.reshape(-1,1)) / (std_u.values.reshape(-1,1) + residual)
zu = zu.fillna(0)

#产品一致性偏差
zi = (indf - item_mean.values.reshape(1,-1)) / (std_i.values.reshape(1,-1) + residual)
zi = zi.fillna(0)

#用户置信度
lambda_n = 10
nu = df.groupby('用户编号').size()
wu = nu/(nu + lambda_n)

#产品置信度
ni = df.groupby('产品编号').size()
wi = ni/(ni+lambda_n)

#修正后的偏差
zuu = zu.mul(wu,axis=0) # wu是Series，索引是用户编号，zu是DataFrame，索引是用户编号，列是产品编号，用mul修正
zii = zi.mul(wi,axis=1)

#联合异常分数
Sui = np.sqrt(zuu **2 + zii **2)

output_path = 'C:\\Users\\ASUS\\Desktop\\任务1.xlsx'
# 如果文件已存在，先删除（避免冲突）
if os.path.exists(output_path):
    os.remove(output_path)
    print(f"已删除旧文件: {output_path}")

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    cadf.to_excel(writer,sheet_name = '评分矩阵')

    # 保存统计量
    pd.DataFrame({'全局平均分': [u]}).to_excel(writer, sheet_name='全局平均分', index=False)
    bu.to_frame(name='用户偏置').to_excel(writer, sheet_name='用户偏置')
    bi.to_frame(name='产品偏置').to_excel(writer, sheet_name='产品偏置')
    residual.to_excel(writer, sheet_name='残差矩阵')

    # 保存方差和标准差
    var_u.to_frame(name='用户方差').to_excel(writer, sheet_name='用户方差')
    std_u.to_frame(name='用户标准差').to_excel(writer, sheet_name='用户标准差')
    var_i.to_frame(name='产品方差').to_excel(writer, sheet_name='产品方差')
    std_i.to_frame(name='产品标准差').to_excel(writer, sheet_name='产品标准差')

    # 保存一致性偏差
    zu.to_excel(writer,sheet_name='用户一致性偏差')
    zi.to_excel(writer,sheet_name='产品一致性偏差')

    # 保存置信度
    wu.to_frame(name='用户置信度').to_excel(writer,sheet_name='用户置信度')
    wi.to_frame(name='产品置信度').to_excel(writer,sheet_name='产品置信度')

    # 保存修正后的偏差
    zuu.to_excel(writer, sheet_name='修正后用户偏差')
    zii.to_excel(writer, sheet_name='修正后产品偏差')

    # 保存最终结果 - 联合异常分数
    Sui.to_excel(writer, sheet_name='联合异常分数')

# ✅ 打印移到 with 块外部
print(f"✅ 成功保存到 {output_path}")

# 验证文件
if os.path.exists(output_path):
    size = os.path.getsize(output_path)
    print(f"📁 文件大小: {size:,} 字节 ({size / 1024 / 1024:.2f} MB)")
