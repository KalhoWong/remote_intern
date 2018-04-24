# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:58:27 2018

@author: hjh83
"""

def run_formula(dv):
    alpha74 = dv.add_formula('alpha74','Rank(Correlation(Ts_Sum(((low_adj*0.35)+(vwap_adj*0.65)), 20), Ts_Sum(Ts_Mean(volume,40), 20), 7))+Rank(Correlation(Rank(vwap_adj), Rank(volume), 6))',
                             is_quarterly=False, add_data=False)
    return alpha74