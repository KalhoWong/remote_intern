# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:57:24 2018

@author: hjh83
"""

def run_formula(dv,param=None):
    default_param = {'t1':20}
    if not param:
        param = default_param
    
    dv.add_formula('DTM',"If(Return(open_adj,1)>0,Max(high_adj-open_adj, open_adj-Delay(open_adj,1)),0)",
                   is_quarterly=False, add_data=True)
    
    dv.add_formula('DBM',"If(Return(open_adj,1)<0,Max(open_adj-low_adj, Delay(open_adj,1)-open_adj),0)",
                   is_quarterly=False, add_data=True)
    
    dv.add_formula('STM1',"Ts_Sum(DTM,%s)"%(param['t1']),
                      is_quarterly=False, add_data=True)
    
    dv.add_formula('SBM1',"Ts_Sum(DBM,%s)"%(param['t1']),
                       is_quarterly=False, add_data=True)
    
    ADTM = dv.add_formula('ADTM_',"(STM1-SBM1)/(Max(STM1,SBM1))",
                          is_quarterly=False, add_data=False)
    return ADTM