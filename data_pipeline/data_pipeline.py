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
import re
import MeCab
from collections import Counter

# テキストクリーニング
def clean_text(text : str) -> str:
    '''
    - text : データフレームのテキストが入る
    '''
    replaced_text = text
    replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[ + ± ＋ ]', ' ', replaced_text)     #  + ±の除去
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    #replaced_text = replaced_text + '削除したよ'
    return replaced_text

# データ検証用関数
def proces_val(data):
    print(data.isnull().sum())
    print(data.shape)

# 形態素解析
def mecab_text(text : str):
    '''
    - text : データフレームのテキストが入る
    - stops : ストップワードの文字列を指定する
    '''
    POS = ['名詞', '形容詞', '辞書登録']
    text = text.strip()
    
    t = MeCab.Tagger(r' -u /content/terminology.dic')
    all_words = []
    words = []
    word_list = []
    words = t.parse(text).split('\n')[:-2]
    for w in words:
        parts = w.split('\t')[1].split(',')
        pos = parts[0]
        base = parts[6]
        
        # 数字を入れるための設定
        if base == '*':
            base = w.split('\t')[0]
        
        if pos in POS:
            for stop in stops:
                if base==stop:
                    base = '' 
            if len(base) > 1:
                word_list.append(base)

    return sorted(set(word_list), key=word_list.index)

# 列をtext、行をDr


def count_words(col : str, df : pd.DataFrame):
    '''
    
    '''
    lis = []
    for li in df[col]:
        lis.extend([i for i in li.split(',') if len(i)>0])            
    return Counter(lis).most_common()

# データフレームをアソシエーション分析できる形にする

def data_reshape(data : pd.DataFrame) -> pd.DataFrame :
    Drs = data.index.to_list()
    words = data.columns.to_list()
    
    data_frames = []
    for dr in Drs:
        new_df = pd.DataFrame(index=range(len(words)), columns=['Dr', 'word', 'value'])
        new_df['Dr'] = dr
        new_df['word'] = words
        new_df['value'] = data.loc[dr, :].to_list()
        data_frames.append(new_df)
    
    results = pd.concat(data_frames)
    results = results[results['value'] > 0].sort_values('value', ascending=False).reset_index(drop=True)
    print(type(results))
    
    return results