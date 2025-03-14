# este archivo lo hemos creado para las pruebas:

# Prueba la función
from github import resta, suma

resultado = suma(5, 3)
if resultado == 8:
    print("La función funciona correctamente")
else:
    print("ERROR: La función no está funcionando bien")

resultadov2 = resta(8,2)
if resultadov2 == 10:
    print("No funciona bien")
else:
    print("funciona bien...")
