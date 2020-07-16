# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:54:26 2020

@author: alfre
"""

# acquisire file csv dal web

import pytz
# from pandas.io.data import DataReader
#from pandas_datareader import DataReader
from pandas_datareader import data as dreader
from collections import OrderedDict
data = OrderedDict()
start_date = '9/17/2011'
end_date = '6/24/2015'

# con il primo comando salviamo il dataframe, dopo averlo scaricato da internet nella cartella
dreader.DataReader('SPY',data_source='yahoo',start=start_date, end=end_date).to_csv("data"+'.csv')
# con il secondo inseriamo solo il DataReader nel dizionario con chiave SPY
data['SPY'] = dreader.DataReader('SPY',data_source='yahoo',start=start_date, end=end_date)         
print(data['SPY'].head())
type(data['SPY'])
