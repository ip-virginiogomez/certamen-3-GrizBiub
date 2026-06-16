edad = int(input("Ingresa tu edad : "))
socio = input("¿Posee tarjeta socio? (s/n) : ")
monto = int(input("Ingrese el total de su monto : "))
descuento = monto * 0.15 +- monto

if edad >= 60 or socio == "s" and monto >= 10.000:
    print("")
    print("Usted califica para el descuento.")
    print("")
    print(f"Su total es : {descuento}")
    print("")
else:
    print("") # los prints sin nada, estan de bonitos nada más.
    print("No califica para el descuento.")
    print("")
    print(f"Monto total: {monto}")
    print("")