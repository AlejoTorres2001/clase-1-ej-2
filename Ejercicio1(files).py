with open("E1datos.txt","r") as file:
    mediciones = file.readlines()
    previa = 0
    contador = 0
    for medidas in mediciones:
        medida_ind = int(medidas)
        if medidas == 0:
            print(f"{medida_ind} N/A - No hay medicion anterior")
        elif medida_ind > previa:
            print(f"{medida_ind} (aumento)")
            contador +=1
        elif medida_ind < previa:
            print(f"{medida_ind} (decrecimiento)")
        previa = medida_ind
print(f"El numero de mediciones mayores a su anterior es: {contador}")