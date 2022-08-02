import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 型ヒントライブラリー
from typing import Any
from typing import Union
from typing import List, Dict
from typing import Optional
from dataclasses import dataclass
from typing_extensions import TypedDict
# from typing import TypedDict

import datetime

'''
この関数はインデックスをカラムに変換する

第1引数にデータフレーム名 :obj
第2引数にリネーム後のカラム名 :str

'''

def to_index(frame : pd.DataFrame, colname : str) -> pd.DataFrame:
    frame.reset_index(inplace = True)
    frame = frame.rename(columns = {'index' : colname})

    return frame

'''
この関数はカラムを指定して要素をカウントして統計量を出し可視化までする
返り値はデータフレーム型
変数に格納して使用した場合はデータフレームが表示されない

第1引数にデータフレーム名 :df
第2引数にカウントしたいカラム名 :str
第3引数に棒グラフのカラー :str

'''

def count_and_bar(frame : pd.DataFrame, colname : str, color : str) -> pd.DataFrame:

    new_frame = pd.DataFrame(frame[colname].value_counts())
    print(new_frame.describe())
    print(colname)
    new_frame[colname].plot.bar(ylabel = '件数', figsize = (50, 20), color = color
    )

    return new_frame

'''
この関数は行の文字の最初からtargetまでの文字を取得して新しいカラムを作る時に使う
第1引数apply()で使うのでデータフレームの1行ずつが入る
第2引数は抜き出したいテキストを正規表現で範囲指定する
.astype(str).apply()で使う
'''
def get_text(text, target):
  idx = text.find(target)
  r = text[:idx]

  return r

'''
datetimeモジュールを使用して適正な時系列indexに変える
第1引数apply()で使うのでデータフレームの1行ずつが入る
.astype(str).apply()で使う
'''

def correct_date(text):
    date_col =datetime.datetime.strptime(text, '%d-%b-%y').strftime('%Y-%m-%d')

    return date_col

'''
この関数はcrosstabから作成したデータフレームから行の範囲を指定して集計する
data : df
a : int
'''

def get_count(data, a):
  for i in range(a + 1):
    s = i* 10
    e = s + 9
    s = str(s)
    e = str(e)
    # 範囲を決める
    a = data.loc[s : e]
    # 集計する
    print('レンジ' + s + '〜' + e)
    print(a)
    print(a.sum(axis = 0))
    print('++++++++++++++++++++++++++++++++++++')

