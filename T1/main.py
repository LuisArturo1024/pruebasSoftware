import os
from datetime import datetime

def prepareLog():
    filename = os.path.join('logs', "log.txt")
    file = open(filename,'w')
    file.write("datetime,entrada a,entrada b,valor obtenido,error\n")
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
    
def writeLog(oprtn,element='',index=''):
    file = os.path.join('logs', "log.txt")
    file = open(file,'a')
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
    if oprtn == -1:
        file.write(dt+','+str(oprtn)+','+str(index)+','+str(element)+','+'1'+'\n')
    elif oprtn == -2:
        file.write(dt+','+str(1)+','+str(index)+','+str(element)+','+'1'+'\n')
    else:
        file.write(dt+','+str(oprtn)+','+str(index)+','+str(element)+','+'0'+'\n')
    file.close()

def elegirElemento(stack):

    string = input("\nElija un elemento de la pila entre 0 y {}\n".format(len(stack)-1))
    try:
        inp = int(string)
        if inp >= len(stack) or inp < 0:
            writeLog(-2,index=str(inp))
            elegirElemento(stack)
        print("\n---Texto del elemento seleccionado de la pila---\n")
        print(stack[inp])
        writeLog(1,element=stack[inp],index=inp)
        print('\n------------------------------------------------\n')
    except:
        print("\nADVERTENCIA: Introduzca un número entero positivo válido\n")
        writeLog(-2,index=str(string))
        elegirElemento(stack)

def masLargo(stack):
    print("\n---Texto del elemento más largo de la pila---\n")
    print(max(stack, key=len))
    writeLog(2,element=max(stack, key=len))
    print('\n---------------------------------------------\n')

def masCorto(stack):
    print("---Texto del elemento más corto de la pila---\n")
    print(min(stack, key=len))
    writeLog(3,element=min(stack, key=len))
    print('\n---------------------------------------------\n')

def mainActivity(stack):
    inp = 0
    if len(stack) == 0:
        print('Agregue archivo text.txt no vacío al directorio texto')
        quit()
    while inp != 4:
        try:
            string = input("1) Elegir texto de la pila\n2) Ver texto más largo\n3) Ver texto más corto\n4) Salir del programa\n")
            inp = int(string)
            if inp <= 0 or inp >= 5:
                print("\nADVERTENCIA: Introduzca un número entero positivo válido\n")
                writeLog(-1,element=inp)
            if inp == 1:
                elegirElemento(stack)
            elif inp == 2:
                masLargo(stack)
            elif inp == 3:
                masCorto(stack)
        except:
            print("\nIntroduzca un número entero positivo válido")
            writeLog(-1,element=string)
    quit()

def main():
    stack = captureInputs()
    prepareLog()
    mainActivity(stack)

if __name__ == "__main__":
    main()