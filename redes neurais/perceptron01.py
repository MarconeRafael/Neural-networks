# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:12:30 2022

@author: A302
"""

entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        #print(entradas[i])
        #print(pesos[i])
        s += e[i] * p[i]
    return s
s = soma(entradas, pesos)
def stepfunction(soma):
    if (soma >= 1):
        return 1
    else:
        return 0
(r = stepfunction(s  )
