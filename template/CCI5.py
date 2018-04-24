# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:53:49 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':5}
    if not param:
        param = default_param
        
    CCI = dv.add_formula('CCI5_','''Ta('CCI',0,open_adj,high_adj,low_adj,close_adj,volume,%s)'''%(param['t1']),
                         is_quarterly=False, add_data=False)
    return CCI