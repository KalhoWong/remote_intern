# -*- coding: utf-8 -*-
"""
Created on Sat May  5 09:36:21 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':30}
    if not param:
        param = default_param
    factor12=dv.add_formula('factor12','-(volume/Delay(close,%s))/(volume/close)'%(param['t1']),
                            is_quarterly=False, add_data=True)
    return factor12