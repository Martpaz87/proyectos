#calcular sueldo promedio del empleado Juan.


Sueldos_juan = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]
suma = 0
meses = len(Sueldos_juan)
def Sueldo_promedio(Sueldos_juan):
    
    for n in Sueldos_juan:
        suma = suma + n
        return suma

promedio = suma/meses

print("El sueldo promedio anual del empleado Juan es:", promedio) 




# solucion correcta:


def Sueldo_promedio(Sueldos_juan):
    #meses se usa dentro de la funcion
    meses = len(Sueldos_juan)
    #suma solo se usa dentro de la funcion
    suma = 0    
    for n in Sueldos_juan:
        suma = suma + n
        #este return no va porque no es una funcion. ya el for
        # guardo en suma el resultado. no es necesario. cuando se ejecuta la 
        # siguiente linea suma va a tener la suma adentro.
        #return suma

    #aca faltaba un tab o espacio para que quede dentro de la funcion
    promedio = suma/meses
    return promedio
#aca falta identacion para que quede adetnro de la funcion
#promedio = suma/meses

Sueldos_juan = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]
promedio_calculado = Sueldos_juan(meses)

print("El sueldo promedio anual del empleado Juan es:", promedio_calculado) 


