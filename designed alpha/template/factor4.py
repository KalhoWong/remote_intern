# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:12:21 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    factor4=dv.add_formula('factor4','(EPS)/(close)',
                              is_quarterly=False,add_data=True)
    return factor4