

# intentar hacer la asignacion de sueldos afuera de la función
# y despues llamar a esa funcion con esa lista de valores.



# aca deberia recibir como parameto una lista de valores y no cada valor individual
def Sueldo_promedio(m1, m2 , m3, m4, m5, m6, m7, m8, m9, m10, m11, m12):
    # esta suma deberia ser con un for sobre la lista de valores.
    suma = m1 + m2 + m3 + m4 + m5 + m6 +m7 + m8 + m9 + m10 + m11 + m12
    
    #esta lista se define afeura de la función. y se llama a 
    # la funcion usando la lista:
    # ej:
    # meses = [........]
    # Sueldo_promedio(meses)
    meses = [m1, m2 , m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]

    # esto esta perfecto.
    print("El sueldo promedio anual del empleado Juan es:", suma/len(meses))
    

#ver el comentario de como llamar a la funcion
Sueldo_promedio(300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700)





