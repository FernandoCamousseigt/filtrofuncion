import sys

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

###Funciones
def print_error():
    """Imprime mensaje de Error"""
    errorMessage = "Intenta de nuevo. Escribe el valor del umbral seguido de \"menor|mayor\".\nSi no se indica el segundo argumento, por defecto se filtrará por mayor."
    return errorMessage

def imprimir_diccionario(dictionary, asignacion):
    """Imprime resultados del diccionario filtrado"""
    print(f"Los productos {asignacion} al umbral son:")
    for i in dictionary:
        print(i)
def filtrar_diccionario(valorUmbral, mayor = True):
    """Procedimiento de creación de diccionario filtrado"""
    if mayor:
        diccionarioFiltrado = {k:v for k,v in precios.items() if v > valorUmbral}
        signo = "mayores"
        imprimir_diccionario(diccionarioFiltrado, signo)
    else:
        diccionarioFiltrado = {k:v for k,v in precios.items() if v < valorUmbral}
        signo = "menores"
        imprimir_diccionario(diccionarioFiltrado, signo)
###

#Validando los Argumentos del User
if len(sys.argv) < 2:
    print(f"Error. No escribiste argumentos.\n{print_error()}")
else:
    umbral = int(sys.argv[1])
    if len(sys.argv) == 2:
        filtrar_diccionario(umbral)
if len(sys.argv) > 2:
    menorOMayor = sys.argv[2].lower()
    if menorOMayor == "menor":
        filtrar_diccionario(umbral, False)
    elif menorOMayor == "mayor":
        filtrar_diccionario(umbral, True)
    else:
        print(f"Escribiste un argumento inválido.\n{print_error()}")
###









