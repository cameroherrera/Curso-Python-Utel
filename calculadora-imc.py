# Calculadora demasa corporal
# Generamos variables a los datos requeridos
# Alberto Herrera Camero 2023.
while True:
    nom = input("Introduzca su nombre: ")
    if len(nom) > 1:
        print(nom)
        paterno = input(" Introduzca su apellido paterno: ")    
        if len(paterno) > 1:
            print(paterno)        
            materno = input(" Introduzca su apellido materno: ")
            if len(materno) > 1:
                print(materno)
                def esEdad(valor):
                    try:
                        return float(valor) if "." in valor else int(valor)
                    except:
                        return None
                edad = esEdad(input("Introduzca su edad: "))
                if edad is None:
                    print("El valor ingresado no es un número.")
                else:
                    print("Su edad es {}".format(edad), "Años")                
                    def esPeso(valor):
                        try:
                            return float(valor) if "." in valor else int(valor)
                        except:
                            return None
                    peso = esPeso(input("Introduzca su peso: "))
                    if peso is None:
                        print("El valor ingresado no es un número.")
                    else:
                        print("Su peso es {}".format(peso))                
                    def esEstatura(valor):
                        try:
                            return float(valor) if "." in valor else int(valor)
                        except:
                            return None
                    estatura = esEstatura(input("Introduzca su estatura: "))
                    if estatura is None:
                        print("El valor ingresado no es un número.")
                    else:
                        print("Su peso es {}".format(estatura))
                        IMC = peso / estatura **2
                        print("Su masa corporal IMC es: {}".format(IMC))
                        break                
            else:
                print("Debes escribir tu apellido materno")                    
                
        else:    
            print("Debes escribir tu apellido paterno")
        
    else:   
        print("Debes escribir tu nombre")
