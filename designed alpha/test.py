# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:17:30 2018

@author: hjh83
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 23:00:30 2018

@author: hjh83
"""

import pandas as pd


def get_dv(start = 20170101,end = 20180101): 
    import jaqs_fxdayu
    jaqs_fxdayu.patch_all()
    from jaqs.data import DataView
    from jaqs_fxdayu.data.dataservice import LocalDataService
    
    import warnings
    warnings.filterwarnings("ignore")
    
    #--------------------------------------------------------
    
    #define
    factor_list  = ['EPS','PE','PS','CTOP','MA10RegressCoeff12','AR','BR','ARBR','np_parent_comp_ttm','total_share','bps',
                'tot_cur_assets','tot_cur_liab','inventories','pre_pay','deferred_exp',
                'oper_rev','tot_assets','net_profit']
    check_factor = ','.join(factor_list)
    
    dataview_folder = r'D:\\INTERN\\data2\\data'
    ds = LocalDataService(fp = dataview_folder)
    
    ZZ800_id = ds.query_index_member("000906.SH", start, end)
    stock_symbol = list(set(ZZ800_id))
    
    dv_props = {'start_date': start, 'end_date': end, 'symbol':','.join(stock_symbol),
             'fields': check_factor,
             'freq': 1,
             "prepare_fields": True}
    
    dv = DataView()
    dv.init_from_config(dv_props, data_api=ds)
    dv.prepare_data()
    return dv


if 'dv' not in dir():
    dv = get_dv()
    
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
        print ('{} OK!'.format(factor))

from template import factor1,factor2,factor3,factor4,factor5,factor6,factor7,factor8,factor9,factor10,factor11,factor12,factor13

for f in ['factor1','factor2','factor3','factor4','factor5','factor6','factor7','factor8','factor9','factor10','factor11','factor12','factor13']:
    test(f, globals()[f].run_formula(dv))