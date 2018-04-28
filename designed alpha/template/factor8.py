# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:15:30 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':7}
    if not param:
        param = default_param
    factor8=dv.add_formula('factor8','If(Ts_Mean(close,7)<close,-1*Delta(close,2),0)',
                           is_quarterly=False, add_data=True)
    return factor8