# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:50:41 2018

@author: hjh83
"""

def run_formula(dv):
    TotalAssetTrate = dv.add_formula('total_asset_t_rate','oper_rev/tot_assets',
                                   is_quarterly=True, add_data=False)
    return TotalAssetTrate