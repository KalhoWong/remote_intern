# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 23:16:16 2018

@author: hjh83
"""

#--------------------------------------------------------
#import

import os
import numpy as np
import pandas as pd
import jaqs_fxdayu
jaqs_fxdayu.patch_all()
from jaqs.data import DataView
from jaqs_fxdayu.data.dataservice import LocalDataService

import warnings
warnings.filterwarnings("ignore")

#--------------------------------------------------------
#define

start = 20130101
end = 20180101
factor_list  = ['BBI','RVI','Elder','EPS','PE','PS','CTOP','AR','BR','ARBR','np_parent_comp_ttm','total_share','bps',
                'tot_cur_assets','tot_cur_liab','inventories',
                'oper_rev','tot_assets','net_profit']
check_factor = ','.join(factor_list)

dataview_folder = r'D:\\INTERN\\data2\\data'
ds = LocalDataService(fp = dataview_folder)

SH_id = ds.query_index_member("000001.SH", start, end)
SZ_id = ds.query_index_member("399106.SZ", start, end)
stock_symbol = list(set(SH_id)|set(SZ_id))

dv_props = {'start_date': start, 'end_date': end, 'symbol':','.join(stock_symbol),
         'fields': check_factor,
         'freq': 1,
         "prepare_fields": True}

dv = DataView()
dv.init_from_config(dv_props, data_api=ds)
dv.prepare_data()

dv.func_doc.funcs

#--------------------------------------------------------
"""
define factor caculation functions

input  :  dict
parameter of factor
-------
output :  pd.DataFrame
    factor_values , Index is trade_date, columns are symbols.

"""
#------------------------------------------------------------------------------    

def MTMMA(param=None):
    default_param = {'t1':6,'t2':20}
    if not param:
        param = default_param
    
    dv.add_formula('MTM1','close - Delay(close, %s)'%(param['t1']),
                        is_quarterly=False, add_data=True)    
    MTMMA = dv.add_formula('MTMMA','Ts_Mean(MTM1, %s)'%(param['t2']),
                         is_quarterly=False)
    
    return MTMMA


def quick_ratio():
    quick_ratio = dv.add_formula('quick_ratio','(tot_cur_assets - inventories)/tot_cur_liab',
                               is_quarterly=True)
    
    return quick_ratio

def TotalAssetTrate():
    TotalAssetTrate = dv.add_formula('total_asset_t_rate','oper_rev/tot_assets',
                                   is_quarterly=True)
    
    return TotalAssetTrate

def CCI5(param=None):
    default_param = {'t1':5}
    if not param:
        param = default_param
        
    CCI = dv.add_formula('CCI5','''Ta('CCI',0,open,high,low,close,volume,%s)'''%(param['t1']),
                         is_quarterly=False)
    return CCI

def NetProftGrowRate3Y():
    NPGR3 = dv.add_formula('netprofitgrowrate3Y','net_proft/Delay(net_profit,3)-1',
                           is_quarterly=True)
    
    return NPGR3

def ADTM(param=None):
    default_param = {'t1':23}
    if not param:
        param = default_param
    
    dv.add_formula('DTM',"If(Return(open,1)>0,Max(high-open, open-Delay(open,1)),0)",
                   is_quarterly=False, add_data=True)
    
    dv.add_formula('DBM',"If(Return(open,1)<0,Max(open-low, Delay(open,1)-open),0)",
                   is_quarterly=False, add_data=True)
    
    dv.add_formula('STM1',"Ts_Sum(DTM,%s)"%(param['t1']),
                      is_quarterly=False, add_data=True)
    
    dv.add_formula('SBM1',"Ts_Sum(DBM,%s)"%(param['t1']),
                       is_quarterly=False, add_data=True)
    
    ADTM = dv.add_formula('ADTM',"If(STM1==SBM1,0,If(STM1>SBM1,(STM1-SBM1)/STM1,(STM1-SBM1)/SBM1))",
                          is_quarterly=False)
    return ADTM

    
def alpha74():
    alpha74 = dv.add_formula('alpha74','Rank(Correlation(Ts_Sum(((low*0.35)+(vwap*0.65)), 20), Ts_Sum(Ts_Mean(volume,40), 20), 7))+Rank(Correlation(Rank(vwap), Rank(volume), 6))',
                             is_quarterly=False)
    return alpha74

def alpha124():
    alpha124 = dv.add_formula('alpha124', '(close-vwap)/Decay_linear(Rank(Ts_Max(close, 30)),2)',
                              is_quarterly=False)
    
    return alpha124


factor_list = ['MTMMA','quick_ratio','TotalAssetTrate','CCI5','NetProftGrowRate3Y','ADTM','alpha74','alpha124']

#--------------------------------------------------------- 
#test output
def test(factor,data):
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError('On factor {} ,output must be a pandas.DataFrame!'.format(factor))
    else:
        try:
            index_name = data.index.names[0]
            columns_name = data.index.names[0]
        except:
            if not (index_name in ['trade_date','report_date'] and columns_name == 'symbol'):
                raise NameError('''Error index name,index name must in ["trade_date","report_date"],columns name must be "symbol" ''')
                
        index_dtype = data.index.dtype_str
        columns_dtype = data.columns.dtype_str
        
        if columns_dtype not in ['object','str']:
            raise TypeError('error columns type')
            
        if index_dtype not in ['int32','int64','int']:
            raise TypeError('error index type')


test_factor = True

if test_factor:   
    for factor in factor_list:
        data = globals()[factor]()
        test(factor,data)









