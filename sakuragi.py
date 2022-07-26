import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
この関数はインデックスをカラムに変換する

第1引数にデータフレーム名 :obj
第2引数にリネーム後のカラム名 :str
data.reset_index(inplace= True)
data = data.rename(columns={'index': 'Insight'})

'''

def to_index(frame, colname):
    frame.reset_index(inplace = True)
    frame = frame.rename(columns = {'index' : colname})

    return frame

'''
この関数はカラムを指定して要素をカウントして可視化までする

第1引数にデータフレーム名 :obj
第2引数にカウントしたいカラム名 :str
第3引数に新しく作成するデータフレーム名 :obj
第4引数に棒グラフのカラー :str

'''

def count_hist(frame, colname, new_frame, color):
    new_frame = pd.DataFrame(frame[colname].value_counts())
    print(colname)
    new_frame[colname].plot.bar(
        y = '件数', figsize = (50, 20), color = color
    )
