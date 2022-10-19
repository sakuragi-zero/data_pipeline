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
# import MeCab
from collections import Counter
import time

# Rejouiの心得
def Rejoui():
    import time
    # 色を定義
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[33m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    text = ["しなやかさとは、", "繊細なようで", "柔らかいからこそ、", "おれない強さを意味します。", 
            "ビジネスでも人生でも", "壁にぶつかったり", "何かを諦めなければならない局面において",
            "しなやかさがあれば新しい選択肢を生み出せます", "当たり前にとらわれない",
            "しなやかな組織づくりをデータの力で実現します"]
    text_2 = "社名に込めた想い"
    text_3 = "理：理性・論理・理想そして教理の『理』常に論理的に物事に接します。"
    text_4 = "情：感情と情熱の『情』人の気持ちを思いやり何事にも情熱を持って臨みます。"
    text_5 = "意：意思の『意』積極的な心を持ち続け強くはっきりした意思を示します"

    for i in text:
        time.sleep(3.5)
        print(i)
    print()
    time.sleep(1)
    print("株式会社 " +color.RED + "Re" +color.END +color.YELLOW + "jo" +color.END + color.BLUE + "ui" +color.END)
    print()
    print(color.BOLD + text_2 + color.END)
    print()
    time.sleep(2)

    for i in text_3:
        time.sleep(0.3)
        print(color.RED + i + color.END, end="")
    print("")
    time.sleep(0.5)

    for i in text_4:
        time.sleep(0.3)
        print(color.BLUE + i + color.END, end="")
    print("")
    time.sleep(0.5)

    for i in text_5:
        time.sleep(0.3)
        print(color.YELLOW + i + color.END, end="")
    print()

    time.sleep(2)
    print("Rejouiは、哲学者カントが提唱する『知情意』にヒントを得た『理・情・意』を社名に込めております")
    time.sleep(2)
    print("顧客に対する姿勢も倫理的に数理・データサイエンスを使いこなし")
    time.sleep(2)
    print("お客様の意思決定に際して同じ情熱・熱量で支援する、を社員一同、心に旗幟として掲げております")

# テキストクリーニング
def clean_text(text : str) -> str:
    '''
    - text : データフレームのテキストが入る
    '''
    replaced_text = text
    replaced_text = re.sub(r'[（）()]', '', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[ + ± ＋ ]', '', replaced_text)     #  + ±の除去
    replaced_text = re.sub(r'　', '', replaced_text)  # 全角空白の除去
    #replaced_text = replaced_text + '削除したよ'
    return replaced_text

# データ検証用関数
def proces_val(data):
    print(data.isnull().sum())
    print(data.shape)

# 形態素解析
# def mecab_text(text : str):
#     '''
#     - text : データフレームのテキストが入る
#     - stops : ストップワードの文字列を指定する
#     '''
#     POS = ['名詞', '形容詞', '辞書登録']
#     text = text.strip()
    
#     t = MeCab.Tagger(r' -u /content/terminology.dic')
#     all_words = []
#     words = []
#     word_list = []
#     words = t.parse(text).split('\n')[:-2]
#     for w in words:
#         parts = w.split('\t')[1].split(',')
#         pos = parts[0]
#         base = parts[6]
        
#         # 数字を入れるための設定
#         if base == '*':
#             base = w.split('\t')[0]
        
#         if pos in POS:
#             for stop in stops:
#                 if base==stop:
#                     base = '' 
#             if len(base) > 1:
#                 word_list.append(base)

#     return sorted(set(word_list), key=word_list.index)

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