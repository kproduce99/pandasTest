from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from sumifs.models import Goods, Tx, Sumifs

# Create your views here.
def sumifs(request):
    tx_df = pd.read_excel('p:/tx_df.xlsx', endcoding = 'ms949') # 엑셀 템플렛 불러오기 (tx_df )
    goods_df = pd.read_excel('p:/goods_df.xlsx', endcoding = 'ms949') # 엑셀 템플렛 불러오기 (goods_df )

    for index, row in tx_df.iterrows():
        Tx.objects.create(TrasactionID=row['TrasactionID'], GoodsID=row['GoodsID'], GoodsIDSeqNo=row['GoodsIDSeqNo'], Quantity=row['Quantity'])

    for index, row in goods_df.iterrows():
        Goods.objects.create(GoodsID=row['GoodsID'], GoodsIDSeqNo=row['GoodsIDSeqNo'], GoodsPrice=row['GoodsPrice'])

    all_df = pd.merge(left=tx_df, right=goods_df, how='left', on=['GoodsID','GoodsIDSeqNo'], sort=False)

    sumifs_df = all_df.groupby([all_df['GoodsID'], all_df['GoodsIDSeqNo']]).sum()
    sumifs_df = sumifs_df.reset_index() # 그룹바이를 통해 행이 뭉쳐져서 인덱스를 구성하게 되면 열을 기반으로 인덱스를 리셋해준다.

    for index, row in sumifs_df.iterrows():
        Sumifs.objects.create(GoodsID=row['GoodsID'], GoodsIDSeqNo=row['GoodsIDSeqNo'], Quantity=row['Quantity'], GoodsPrice=row['GoodsPrice'])

    Sumifs_list = Sumifs.objects.all()
    context = {"Sumifs_list" : Sumifs_list}

    return render(request, 'sumifs/sumifs.html', context)
