# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:14:43 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':7}
    if not param:
        param = default_param
    factor7=dv.add_formula('factor7','-1*Rank(Correlation(Rank(close),Rank(volume),%s))'%(param['t1']),
                           is_quarterly=False, add_data=True)
    return factor7