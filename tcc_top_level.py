from tcc import calculate_pH
import pandas as pd

#A = [(0, 1.0), (0.05, 1.1), (0.10, 1.2)]
#df = pd.DataFrame(A)
#df.to_clipboard(header=False, index = False)

#print(calculate_pH(V_NaOH=0.05))


def titration_curve(v_start: float, v_end: float, step: float) -> list:
    result = []
    V_NaOH_values = [v_start + i * step for i in range(int((v_end - v_start) / step) + 1)]
    initial_H_OH = [0.1, 1e-13]
    after_eq_point = False
    for V_NaOH in V_NaOH_values:
        pH = calculate_pH(V_NaOH, initial_H_OH)
        if V_NaOH < 0.1:
            initial_H_OH = [pH, 1e-14 / pH]
        else:
            if not after_eq_point: initial_H_OH = [1e-8, 1e-6]
            else: initial_H_OH = [pH, 1e-14 / pH]
            after_eq_point = True
        result.append((V_NaOH, pH))
    return result

v_start = 0.00
v_end = 0.2
step = 0.001

titration_data = titration_curve(v_start, v_end, step)

df = pd.DataFrame(titration_data)
df.to_clipboard(header=False, index = False)