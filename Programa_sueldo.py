#calcular sueldo promedio del empleado Juan.

def sueldo_promedio(sueldos_juan):

    meses = len(sueldos_juan)
    suma = 0
    for n in sueldos_juan:
        suma = suma + n
        
    promedio = suma/meses
    return promedio


sueldos_juan = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]
promedio_calculado = sueldo_promedio(sueldos_juan)
    
print("El sueldo promedio anual del empleado Juan es:", promedio_calculado ) 
#clasificar dicho sueldo segun corresponda en referencia a los valores dados.
if promedio_calculado <= 300 :
    print("El empleado/a cobra un sueldo bajo.")
if promedio_calculado >= 300 and promedio_calculado <= 900 :
    print("El sueldo percibido esta dentro e los parametros normales. ")
else :
    print("El sueldo percibido es mayor de lo normal. ")


