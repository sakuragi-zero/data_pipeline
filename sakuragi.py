'''
この関数はインデックスをカラムに変換する
第1引数にデータフレーム名
第2引数にリネーム後のカラム名
data.reset_index(inplace= True)
data = data.rename(columns={'index': 'Insight'})
'''

def to_index(frame, colname):
    frame.reset_index(inplace = True)
    frame = frame.rename(columns = {'index' : colname})

    return frame