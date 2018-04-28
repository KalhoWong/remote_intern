# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:13:57 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':10}
    if not param:
        param = default_param
    factor6=dv.add_formula('factor6','(-1 * Correlation(Rank(close), Rank(volume), %s))'%(param['t1']),
                   is_quarterly=False,add_data=True)
    return factor6