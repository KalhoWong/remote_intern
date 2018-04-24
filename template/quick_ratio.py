# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:48:27 2018

@author: hjh83
"""

def run_formula(dv):
    quick_ratio = dv.add_formula('quick_ratio','(tot_cur_assets - inventories)/tot_cur_liab',
                               is_quarterly=True, add_data=False)
    return quick_ratio