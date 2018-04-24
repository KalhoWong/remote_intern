# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:55:13 2018

@author: hjh83
"""

def run_formula(dv):
    NPGR3 = dv.add_formula('netprofitgrowrate3Y','net_profit/Delay(net_profit,3)-1',
                           is_quarterly=True, add_data=False)
    return NPGR3