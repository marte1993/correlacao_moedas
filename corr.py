# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:56:26 2022

@author: Rafael_Lopes
"""


import pandas as pd
import MetaTrader5 as metatrader
from datetime import datetime as dt 
from datetime import timedelta

# faz a ligação com a Clear
mt5Forex= metatrader

# datas de parametro
inicio=   dt.now()#dt(2022, 3, 3 )
fim= inicio - timedelta(days=90)
periodoTempo= metatrader.TIMEFRAME_D1


if not mt5Forex.initialize('./mt5_forex/terminal64.exe'):
    print('Falha ao incializar metatrader Forex.')
    quit() 

 
    
moedas= mt5Forex.symbols_get()
cotacoes= pd.DataFrame()


for i in moedas:
    cot= mt5Forex.copy_rates_range(i.name, mt5Forex.TIMEFRAME_D1, fim, inicio)
    cot= pd.DataFrame(cot)
    cotacoes[i.name]= cot['close']
   

correlacao= cotacoes.corr()
correlacao.to_excel('correlacao_moedas_1D.xlsx')






