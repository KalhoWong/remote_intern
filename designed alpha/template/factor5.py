# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:13:03 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    factor5=dv.add_formula('factor5','((((-1*Ts_Min(low, 7)) + Delay(Ts_Min(low, 7), 7)) * Rank(((Ts_Sum(Return(close,1),220)-Ts_Sum(Return(close,1),20))/220)))*Ts_Rank(volume,5))',
                   is_quarterly=False,add_data=True)
    return factor5