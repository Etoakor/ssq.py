# coding:utf-8
from pyecharts import Line,Bar
import pandas as pd

df=pd.read_excel('2I2C.xlsx')  # 这个会直接默认读取到这个Excel的第一个表单


bar = Bar("2I2C", "001")
bar.add("1", df['省分'].values, df[1].values,is_more_utils=True)
bar.render()

'''
line = Line("折线图","2I2C")

line.add("1",df['省分'].values, df[1].values, is_label_show=True)
line.add("2",df['省分'].values, df[3].values, is_label_show=True)
line.render()
'''
