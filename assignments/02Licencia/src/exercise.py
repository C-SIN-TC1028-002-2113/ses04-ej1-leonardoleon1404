def main():
    #escribe tu código abajo de esta línea
    edad1 = int(input("Ingresa tu edad: "))
    if edad1>=18:
        id = input("¿Tienes identificación oficial? (s/n): ")
        if  id == 's':
            print("Trámite de licencia concedido")
        elif id == 'n':
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif edad1<=0:
        print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")



if __name__ == '__main__':
    main()
