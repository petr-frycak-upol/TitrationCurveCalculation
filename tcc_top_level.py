from tcc import calculate_pH

def titration_curve(v_start: float, v_end: float, step: float) -> list:
    result = []
    V_NaOH_values = [v_start + i * step for i in range(int((v_end - v_start) / step) + 1)]
    initial_H_OH = [1E-1, 1E-13]
    after_eq_point = False
    for V_NaOH in V_NaOH_values:
        pH = calculate_pH(V_NaOH, initial_H_OH)
        if V_NaOH<0.1:
            initial_H_OH = [pH, 1E-14 / pH]
        else:
            if not after_eq_point: initial_H_OH = [1E-8, 1E-6]
            else: initial_H_OH = [pH, 1E-14 / pH]
            after_eq_point = True
        result.append((V_NaOH, pH))
    return result

v_start = 0.00
v_end = 0.2
step = 0.001

titration_data = titration_curve(v_start, v_end, step)

for volume, pH in titration_data:
    print(f"Volume NaOH: {volume:.3} l pH: {pH:.2}")