# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:16:09 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':7}
    if not param:
        param = default_param
    factor9 = dv.add_formula('factor9','-Rank(Correlation(Ts_Sum(((low*0.35)+(vwap*0.65)), 20), Ts_Sum(Ts_Mean(volume,45), 20), 5))-Rank(Correlation(Rank(vwap), Rank(volume), 5))',
                             is_quarterly=False, add_data=True)
    return factor9