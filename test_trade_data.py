import os
import pandas as pd
import numpy as np


def get_data(df, selected_value, selected_feature):
    # selected_value = 'o'  # 选择标的的名称比如  selected_value = 'rb' 则会获取rb0818 rb0918 ......
    # selected_feature = 'C'  # 选择哪个特征进行判断交易哪一期的期货 rb0819 或者 rb0918 .... 以方差作为选择方法
    size_row = df.iloc[:, 0].size - 1    # 获得一个数据的行数ps注意索引从零开始
    df_sub = pd.DataFrame()     # 创建一个 dataframe 的表格 pd.dataframe

    for i in range(0, size_row):
        if selected_value in df.iloc[i, 3]:
            df_sub = df_sub.append(df.iloc[i, ])  # 获得一个
    print(df_sub)

    # groupby ('ru_index').var()['以此参数的方差作为参考选择交易标的']
    biaodi_feature = df_sub.groupby('code').mean()[
        selected_feature]     # 找到方差最大的一个期货(最活跃的期货) C 为某个变量的方差vol acc_val 等等   B 为标的名称eg ru0918
    biaodi_var_max = biaodi_feature.idxmax()  # 扥到了一个期货名 eg 通过判断方差发现 rb0918最活跃

    select_trade = df.loc[df['code'] == biaodi_var_max]
    return select_trade


# 以一天的数据作为实验
path = "I:/Financial_Modeling/filedb-for-steven/filedb/kbar/2010_marge"
#  获得了相关的路径信息在这个文件夹下所有的文件列表
files = os.listdir(path)
i = 1
#  描述路径一第一个为例，将文件列表名称中的第一个导入到
print(path+'/'+'%s' % files[i])  # 成功的路径描述
data_i = pd.read_csv((path+'/'+'%s' % files[i]))

selected_data = get_data(data_i, 'rb', 'volume')
