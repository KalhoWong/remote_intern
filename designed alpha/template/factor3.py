# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 04:11:29 2018

@author: hjh83
"""

def SMA(A,n,m):
    # 设置alpha的比例
    alpha = m/n
    #通过ewm计算递归函数
    return A.ewm(alpha=alpha, adjust=False).mean()

def run_formula(dv,param=None):
    default_param = {'t1':14}
    if not param:
        param = default_param
    factor3=dv.add_formula('factor3','-SMA(close-Delay(close,%s),%s,1)'%(param['t1'],param['t1']),
                           is_quarterly=False,add_data=True,register_funcs={"SMA":SMA})
    return factor3