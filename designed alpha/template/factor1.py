# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:09:02 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':6}
    if not param:
        param = default_param
    factor1=dv.add_formula('factor1','-Ts_Mean(Abs(close-Ts_Mean(close,%s)),%s)'%(param['t1'],param['t1']),
                              is_quarterly=True,add_data=True)
    return factor1