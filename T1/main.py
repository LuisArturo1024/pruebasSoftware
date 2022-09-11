import os
from datetime import datetime

def prepareLog():
    filename = os.path.join('logs', "log.txt")
    file = open(filename,'w')
    file.write("datetime;operacion_menu;entrada_a;entrada_ b;valor_obtenido;cod_error;desc_error\n")
    file.close()

def captureInputs():
    stack = []
    for filename in os.listdir('texto'):
        file = os.path.join('texto', filename)
        if os.path.isfile(file) and filename == 'text.txt':
            lines = open(file)
            for line in lines.readlines():
                stack.append(line.strip())
            return stack
        else:
            print('Agregue archivo de texto plano "text.txt" válido al directorio /texto')
            quit()
    
def writeLog(op_menu,inp_a='',inp_b='',err_menu2='',value='',err=0):
    error = str(err)
    file = os.path.join('logs', "log.txt")
    file = open(file,'a')
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
    file.write(dt+';'+str(op_menu)+';'+str(inp_a)+';'+str(inp_b)+';'+str(value)+';'+error+';'+err_menu2+'\n')
    file.close()

def elegirElemento(stack):
    string = input("\nElija un elemento de la pila entre 0 y {}\n".format(len(stack)-1))
    try:
        inp = int(string)
        if inp >= len(stack) or inp < 0:
            writeLog(1,inp_a=str(inp),err=1,err_menu2='out of bounds')
            elegirElemento(stack)
        print("\n---Texto del elemento seleccionado de la pila [largo: {}]---\n".format(str(len(stack[inp]))))
        print(stack[inp])
        writeLog(1,inp_a=str(inp),value=stack[inp])
        print('\n------------------------------------------------\n')
    except:
        print("\nADVERTENCIA: Introduzca un número de opción válido\n")
        writeLog(1,inp_a=str(string),err=1,err_menu2='invalid input')
        elegirElemento(stack)

def comparar(stack):
    string = input("\nElija el elemento 1 a comparar de la pila (entre 0 y {})\n".format(len(stack)-1))
    string2 = input("\nElija el elemento 2 a comparar de la pila (entre 0 y {})\n".format(len(stack)-1))
    try:
        inp = int(string)
        inp2 = int(string2)
        if inp >= len(stack) or inp < 0 or inp2 >= len(stack) or inp2 < 0:
            writeLog(4,inp_a=str(inp),inp_b=str(inp2),err=1,err_menu2='out of bounds')
            comparar(stack)
        print("\n---Texto del elemento 1 [largo: {}]---\n".format(str(len(stack[inp]))))
        print(stack[inp])
        print('\n------------------------------------------------\n')
        print("\n---Texto del elemento 2 [largo: {}]---\n".format(str(len(stack[inp2]))))
        print(stack[inp2])
        print('\n------------------------------------------------\n')
        diff = abs(len(stack[inp])-len(stack[inp2]))
        if diff == 0:
            print("Los elementos 1 y 2 tienen la misma cantidad de caracteres: {}".format(str(len(stack[inp]))))
        else:
            print("La diferencia en cantidad de caracteres del elemento 1 y 2 es: {}".format(str(diff)))
        writeLog(4,inp_a=str(inp),inp_b=str(inp2),value=diff)
        print('\n------------------------------------------------\n')
    except:
        print("\nADVERTENCIA: Introduzca un número de opción válido\n")
        writeLog(4,inp_a=str(string),err=1,err_menu2='invalid input')
        comparar(stack)

def masLargo(stack):
    lar = max(stack, key=len)
    print("\n---Texto del elemento más largo de la pila [largo: {}]---\n".format(str(len(lar))))
    print(lar)
    writeLog(2,value=lar)
    print('\n---------------------------------------------\n')

def masCorto(stack):
    shor = min(stack, key=len)
    print("---Texto del elemento más corto de la pila [largo: {}]---\n".format(str(len(shor))))
    print(shor)
    writeLog(3,value=shor)
    print('\n---------------------------------------------\n')

def mainActivity(stack):
    inp = 0
    if len(stack) == 0:
        print('Agregue archivo text.txt no vacío al directorio texto')
        quit()
    while inp != 5:
        try:
            string = input("1) Elegir texto de la pila\n2) Ver texto más largo\n3) Ver texto más corto\n4) Comparar 2 strings\n5) Salir del programa\n")
            inp = int(string)
            if inp <= 0 or inp >= 6:
                print("\nADVERTENCIA: Introduzca un número de opción válido\n")
                writeLog(0,inp_a=inp,err=1,err_menu2='out of bounds')
            if inp == 1:
                elegirElemento(stack)
            elif inp == 2:
                masLargo(stack)
            elif inp == 3:
                masCorto(stack)
            elif inp == 4:
                comparar(stack)
        except:
            print("\nIntroduzca un número de opción válido")
            writeLog(0,inp_a=string,err=1,err_menu2='invalid input')
    quit()

def main():
    stack = captureInputs()
    prepareLog()
    mainActivity(stack)

if __name__ == "__main__":
    main()