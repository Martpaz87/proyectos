#calcular sueldo promedio del empleado Juan.


Sueldos_juan = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]
suma = 0
meses = len(Sueldos_juan)
def Sueldo_promedio(Sueldos_juan):
    
    for n in Sueldos_juan:
        suma = suma + n
        return suma
promedio = suma/meses
print("El sueldo promedio anual del empleado Juan es:" promedio) 

    

