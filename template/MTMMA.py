# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:44:56 2018

@author: hjh83
"""

def run_formula(dv, param=None):
    default_param = {'t1':10,'t2':10}
    if not param:
        param = default_param
    
    dv.add_formula('MTM1','close_adj - Delay(close_adj, %s)'%(param['t1']),
                        is_quarterly=False, add_data=True)    
    MTMMA = dv.add_formula('MTMMA1','Ts_Mean(MTM1, %s)'%(param['t2']),
                         is_quarterly=False)
    return MTMMA