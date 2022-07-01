
#funcion de suma



def suma(n1, n2):
    return n1 + n2

#funcion de resta
def resta(n1, n2):
    return n1 - n2

#funcion de multiplicacion
def multiplicacion(n1, n2):
    return n1 * n2

#funcion de division
def division(n1, n2):
    return n1/n2

#funcion que cierra el programa
def close():
    return print ("Cerrando programa...\nVuelva pronto!")

#muestra las operaciones para elegir
def eleccion_operacion():
    return str(input("Qué operación vas a realizar(1,2,3,4)? \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division \n5.Salir \n"))


# verifica que se elija bien la operacion y establece que tarea seguir en base a los datos ingresados
def chequeo(eleccion):  
        try:
            num_valido = str(eleccion)
            if num_valido < "1" or num_valido > "4":
                raise ValueError
            return True    
        except (ValueError or TypeError):
            if num_valido == "5":
                return "5"
            else:    
                print("CARACTER O NUMERO INVALIDO")
                return False


            
#los input para ingresar los numeros/parametros a operar
def my_variables():
    global num1, num2
    num1 = float(input("Primer numero--> "))
    num2 = float(input("Segundo numero--> "))


#funcion que cierra el programa al elegir 5(Salir)
def no_calculadora():
    if choice == "5":
        close()

#Muestra como funcionan las operaciones 
def calculadora(n1, n2):
        if choice == "1":
            print (f"{num1} + {num2} = {suma(n1,n2)}")
        elif choice == "2":
            print (f"{num1} - {num2} = {resta(n1,n2)}")
        elif choice == "3":
            print (f"{num1} * {num2} = {multiplicacion(n1, n2)}")
        elif choice == "4":
            print (f"{num1} / {num2} = {division(n1, n2)}")


choice = eleccion_operacion()
chequeo(choice)
#procedimiento de acuerdo a los datos obtenidos
if chequeo(choice) == "5":
    no_calculadora()
elif chequeo(choice) == True:
    my_variables()
    calculadora(num1,num2)
else:
    print("Intentalo de nuevo")
    close()
