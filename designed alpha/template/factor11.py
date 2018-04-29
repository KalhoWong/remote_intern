# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 09:07:11 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    factor11=dv.add_formula('factor11','(oper_profit)/float_mv',
                            is_quarterly=True, add_data=True)
    return factor11