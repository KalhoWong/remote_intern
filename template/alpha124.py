# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:59:33 2018

@author: hjh83
"""

def run_formula(dv):
    alpha124 = dv.add_formula('alpha124', '(close_adj-vwap_adj)/Decay_linear(Rank(Ts_Max(close_adj, 30)),2)',
                              is_quarterly=False, add_data=False)
    return alpha124