from tcc import calculate_pH

def titration_curve(v_start: float, v_end: float, step: float) -> list:
    result = []
    V_NaOH_values = [v_start + i * step for i in range(int((v_end - v_start) / step) + 1)]
    for V_NaOH in V_NaOH_values:
        pH = calculate_pH(V_NaOH)
        result.append((V_NaOH, pH))
    return result

v_start = 0.00
v_end = 0.2
step = 0.001

titration_data = titration_curve(v_start, v_end, step)

for volume, pH in titration_data:
    print(f"Volume NaOH: {volume:.3} l pH: {pH:.2}")