# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:16:48 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    factor10=dv.add_formula('factor10','-Rank(vwap+close)/Rank(vwap-close)',
                            is_quarterly=False, add_data=True)
    return factor10