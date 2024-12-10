from scipy.optimize import fsolve
import math

c0_HCl = 0.1
V0_HCl = 0.1
c_NaOH = 0.1
Kw = 1e-14

def equations(unknowns, *precalculated_args):
    H, OH = unknowns
    Cl, Na = precalculated_args
    eq1 = Kw - H * OH
    eq2 = Na + H - Cl - OH
    return [eq1, eq2]

def precalculate(c0_HCl: float, V0_HCl: float, c_NaOH: float, V_NaOH: float) -> (float, float):
    Cl = c0_HCl * V0_HCl / (V0_HCl + V_NaOH)
    Na = c_NaOH * V_NaOH / (V0_HCl + V_NaOH)
    return Cl, Na

def calculate_pH(V_NaOH: float) -> float:
    initial_H_OH = [1E-7, 1E-7]
    solution = fsolve(equations, initial_H_OH, args=precalculate(c0_HCl, V0_HCl, c_NaOH, V_NaOH))
    H, OH = solution

    return H
    #return -math.log10(H)