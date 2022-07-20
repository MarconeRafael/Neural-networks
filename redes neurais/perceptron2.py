# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:49:09 2022

@author: A302''
"""
import numpy as np
entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):
    return e.dot(p)
#DOT PRODUT --> PRODUTO ESCALAR (SOMAS AS MULTIPLICAÇÕES)
s = soma(entradas, pesos)
def stepfunction(soma):
    if (soma >= 1):
        return 1
    else:
        return 0
r = stepfunction(s)
