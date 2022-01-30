def sacar_factorial(numero):
    """Calcula e imprime el factorial de un numero"""
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
    print(f"El factorial de {numero} es {resultado}")

def sacar_productoria(lista):
    """Calcula e imprime el resultado de la productoria de una lista de numeros"""
    resultado = 1
    for i in lista:
        resultado *= i
    print(f"La productoría de {lista} es {resultado}")

def calcular(**kwargs):
    """Ejecuta las funciones de calcular factorial o productoria segun los argumentos entregados por la ejecución del programa"""
    for k,v in kwargs.items():
        if "fact" in k:
            sacar_factorial(v)
        elif "prod" in k:
            sacar_productoria(v)

#EJECUCION DEL PROGRAMA
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

