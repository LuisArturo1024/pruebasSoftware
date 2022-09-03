import os

def captureInputs():
    stack = []
    for filename in os.listdir('textos'):
        file = os.path.join('textos', filename)
        if os.path.isfile(file):
            with open(file) as f:
                stack.append(''.join(f.readlines()))
    return stack

def elegirElemento(stack):
    print("\nElija un elemento de la pila entre 0 y {}".format(len(stack)-1))
    inp = int(input())
    try:
        while inp >= len(stack) or inp < 0:
            print("\nADVERTENCIA: Elija un elemento de la pila entre 0 y {}".format(len(stack)-1))
            inp = int(input())
        print("---Texto del elemento seleccionado de la pila---\n")
        print(stack[inp])
        print('\n------------------------------------------------\n')
    except:
        print("\nADVERTENCIA: Introduzca un número entero positivo válido\n")
        elegirElemento(stack)
        

def masLargo(stack):
    print("---Texto del elemento más largo de la pila---\n")
    print(max(stack, key=len))
    print('\n---------------------------------------------\n')

def masCorto(stack):
    print("---Texto del elemento más corto de la pila---\n")
    print(min(stack, key=len))
    print('\n---------------------------------------------\n')

def mainActivity(stack):
    inp = 0
    while inp != 4:
        try:
            inp = int(input("1) Elegir texto de la pila\n2) Ver texto más largo\n3) Ver texto más corto\n4) Salir del programa\n"))
            if inp <= 0 or inp >= 5:
                print("\nADVERTENCIA: Introduzca un número entero positivo válido\n")
            if inp == 1:
                elegirElemento(stack)
            elif inp == 2:
                masLargo(stack)
            elif inp == 3:
                masCorto(stack)
        except:
            print("\nIntroduzca un número entero positivo válido")
    quit()

def main():
    stack = captureInputs()
    mainActivity(stack)

if __name__ == "__main__":
    main()