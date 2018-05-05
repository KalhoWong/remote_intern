# -*- coding: utf-8 -*-
"""
Created on Sat May  5 09:38:23 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':5,'t2':10,'t3':20,'t4':60}
    if not param:
        param = default_param
    factor13=dv.add_formula('factor13','(Ts_Mean(turnover,%s)+Ts_Mean(turnover,%s)+Ts_Mean(turnover,%s)+Ts_Mean(turnover,%s))/4'%(param['t1'],param['t2'],param['t3'],param['t4']),
                            is_quarterly=False, add_data=True)
    return factor13