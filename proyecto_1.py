#Empleado Juan. Calcular sueldo promedio.
"""
def Sueldo_promedio(m1, m2 , m3, m4, m5, m6, m7, m8, m9, m10, m11, m12):
    suma = m1 + m2 + m3 + m4 + m5 + m6 +m7 + m8 + m9 + m10 + m11 + m12
    meses = [m1, m2 , m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
    print("El sueldo promedio anual del empleado Juan es:", suma/len(meses))
    
Sueldo_promedio(300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700)
"""
sueldos = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]
suma_sueldos = sueldos [0] + sueldos [1] + sueldos [2] + sueldos [3] + sueldos [4] + sueldos [5] + sueldos [6] + sueldos [7] + sueldos [8] + sueldos [9] + sueldos [10] + sueldos [11]
meses = len(sueldos)

promedio_sueldo = suma_sueldos/meses
print("El promedio de sueldo anual de Juan es: ", promedio_sueldo) 