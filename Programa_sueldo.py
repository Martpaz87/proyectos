#calcular sueldo promedio del empleado Juan.

def Sueldo_promedio(Sueldos_juan):

    meses = len(Sueldos_juan)
    suma = 0
    for n in Sueldos_juan:
        suma = suma + n
        
    promedio = suma/meses
    return promedio


Sueldos_juan = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]
promedio_calculado = Sueldo_promedio(Sueldos_juan)
    
<<<<<<< HEAD
print("El sueldo promedio anual del empleado Juan es:", promedio_calculado ) 

if promedio_calculado < 300 :
    print("El empleado/a cobra un sueldo bajo.")
if promedio_calculado > 300 and promedio_calculado < 900 :
    print("El sueldo percibido esta dentro e los parametros normales. ")
else :
    print("El sueldo percibido es mayor de lo normal. ")
=======
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

>>>>>>> 45d301fdbd5ad951c6e5e4fdb33a1fd79d823275

