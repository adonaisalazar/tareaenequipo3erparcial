"""Un teatro ortorga descuentos segun la edad del cliente. Determina la cantidad de dinmero que el teatro deja de percibiur por cada una de las categorias.
Tomar encuenta que los niños menores de 5 años no pueden entrar al teatro y que existe un precio único en los asientos. Los descuentos se hacen tomando en 
cuenta el siguiente cuadro:"""
"""                  Edad            Descuento"""
"""Categoria 1      5 - 14             35%"""
"""Categoria 2     15 - 19             25%"""
"""Categoria 3     20 - 45             10%"""
"""Categoria 4     46 - 65             25%"""
"""Categoria 5   66 en adelante        35%"""

asiento = float(input("ingrese el costo del asiento: "))
edad = int(input("ingrese su edad: "))

if edad < 5:
    print("No se permiten personas menores a 5 años")

if edad >= 5 and edad <= 14:
    print("Categoria 1")
    pd = asiento * 0.35
    pt = asiento - pd
    print("El precio es de", pt)

if edad >= 15 and edad <= 19:
    print("Categoria 2")
    pd = asiento * 0.25
    pt = asiento - pd
    print("El precio es de", pt)

if edad >= 20 and edad <= 45:
    print("Categoria 3")
    pd = asiento * 0.10
    pt = asiento - pd
    print("El precio es de", pt)

if edad >= 46 and edad <= 65:
    print("Categoria 4")
    pd = asiento * 0.25
    pt = asiento - pd
    print("El precio es de", pt)

if edad >= 66:
    print("Categoria 5")
    pd = asiento * 0.35
    pt = asiento - pd
    print("El precio es de", pt)
