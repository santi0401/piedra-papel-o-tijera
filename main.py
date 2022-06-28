import random

while True:

    aleatorio = random.randrange(0,3)
    elijePc = ""
    print("1. piedra")
    print("2. papel")
    print("3.tijera")
    opcion = int(input("elije tu opcion: "))

    if opcion == 1:
        elijeUsuario = "papel"
    elif opcion == 2:
        elijeUsuario = "papel"
    elif opcion == 3:
        elijeUsuario = "tijera"
    print("Elejiste: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "piedra"
    elif aleatorio == 1:
        elijePc = "papel"
    elif aleatorio == 2:
        elijePc = "tijera"
    print("la maquina elijio: ", elijePc)
    print("...")
    if elijePc == "piedra" and elijeUsuario == "papel":
        print("ganaste, papel envuelve piedra")
    elif elijePc == "papel" and elijeUsuario == "tijera":
        print("ganaste, tijera corta papel")
    elif elijePc == "papel" and elijeUsuario == "piedra":
        print("ganaste, tijera corta papel")
    if elijePc == "papel" and elijeUsuario == "piedra":
        print("perdiste, papel envuelve piedra")
    elif elijePc == "tijera" and elijeUsuario == "papel":
        print("perdiste, tijera corta papel")
    elif elijePc == "piedra" and elijeUsuario == "tijera":
        print("perdiste, piedra rompe tijera")
    elif elijePc == elijeUsuario:
        print("empate")

    play_again = input("qieres jugar de nuevo (s/n): ")
    if play_again.lower() !="s":
        break
