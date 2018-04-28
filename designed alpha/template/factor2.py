# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:10:37 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':14,'t2':6}
    if not param:
        param = default_param
    factor2=dv.add_formula('factor2','-Correlation(Rank(((close-Ts_Min(low,%s))/(Ts_Max(high,%s)-Ts_Min(low,%s)))), Rank(volume),%s)'%(param['t1'],param['t1'],param['t1'],param['t2']),
                              is_quarterly=True,add_data=True)
    return factor2