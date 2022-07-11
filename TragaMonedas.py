import random

fila1 = ["", "", ""]
fila2 = ["", "", ""]
fila3 = ["", "", ""]

win_a = ["A", "A", "A"]
win_b = ["B", "B", "B"]
win_c = ["C", "C", "C"]

a = ["A", "B", "C"]
inventario = []
lista_premios = ["Peluche Totoro","Peluche Pacman","Peluche SUS","Peluche Pikachu"]
puntos = 500
respuesta_compra = ""

class Premios:
    def __init__(self,plush_totoro,plush_pacman,plush_sus,plush_pikachu):
        self.plush_totoro = plush_totoro
        self.plush_pacman = plush_pacman
        self.plush_sus = plush_sus
        self.plush_pikachu = plush_pikachu


precios = Premios(5000,2000,10000,1500)

print("Tragaperras:\nEmpiezas con 500 puntos, cada intento cuesta 100 puntos\n")
respuesta = input("Presione 1 para jugar \nPresione 2 para ver la lista de premios \nPresione 3 para ver sus puntos actuales\nPresione 0 para ver tu inventario:\n")

while puntos >= 100 and respuesta == "1" or respuesta == "2" or respuesta ==  "3" or respuesta == "0":

    if respuesta == "2":
        print("Lista de premios\nPlush_totoro --> $5000  Plush_pacman --> $2000\nPlush_sus --> $10000  Plush_pikachu --> $1500: ")

        respuesta_compra = input("Comprar:\n4 -- plush_totoro\n5 -- plush_pacman\n6 -- plush_sus\n7 -- plush_pikachu \n\n1 Para jugar de nuevo: ")
        respuesta  = "1"
    elif respuesta == "3":
        print(puntos)
        respuesta = input("\n1 Para jugar\n2 Para ver premios\n0 para ver inventario: ")
    elif respuesta =="0":
        print(inventario)
        respuesta = input("1 Para jugar\n2 Para ver premios\n3 Para ver puntos: ")
    elif respuesta_compra == "4" and puntos >= precios.plush_totoro:
        print("¡Compraste un Peluche Totoro!")
        inventario.append(lista_premios[0])
        puntos -= precios.plush_totoro
        respuesta_compra = ""

        respuesta = input("1 Para jugar \n2 Para ver premios. \n3 Para ver puntos actuales\n0 para ver inventario: ")
    elif respuesta_compra == "4" and puntos < precios.plush_totoro:
        print("Lo siento no tienes suficientes puntos para comprarlo")
        respuesta_compra = ""
        respuesta = input("1 Para jugar\n2 Para ver premios\n3 Para ver puntos actuales\n0 para ver inventario: ")


    elif respuesta_compra == "5" and puntos >= precios.plush_pacman:
        print("¡Compraste un peluche Pac man!")
        inventario.append(lista_premios[1])
        puntos -= precios.plush_pacman
        respuesta_compra = ""
        respuesta = input("1 Para jugar \n2 Para ver premios \n3 Para ver puntos actuales\n0 para ver inventario: ")
    elif respuesta_compra == "5" and puntos < precios.plush_pacman:
        print("Lo siento no tienes suficientes puntos para comprarlo")
        respuesta_compra = ""
        respuesta = input("1 Para jugar \n2 Para ver premios \n3 Para ver puntos actuales\n0 para ver inventario: ")
    elif respuesta_compra == "6" and puntos >= precios.plush_sus:
        respuesta_compra = ""
        print("¡Compraste un Peluche Amongus!")
        inventario.append(lista_premios[2])
        puntos -= precios.plush_sus
        respuesta = input("1 Para jugar. \n2 Para ver premios. \n3 Para ver puntos actuales\n0 para ver inventario: ")
    elif respuesta_compra == "6" and puntos < precios.plush_sus:
        respuesta_compra = ""
        print("Lo siento no tienes suficientes puntos para comprarlo")
        respuesta = input("1 Para jugar. \n2 Para ver premios. \n3 Para ver puntos actuales\n0 para ver inventario: ")
    elif respuesta_compra == "7" and puntos >= precios.plush_pikachu:
        respuesta_compra = ""
        print("¡Compraste un Peluche Pika!")
        inventario.append(lista_premios[3])
        puntos -= precios.plush_pikachu
        respuesta = input("1 Para jugar. \n2 Para ver premios. \n3 Para ver puntos actuales\n0 para ver inventario: ")
    elif respuesta_compra == "7" and puntos < precios.plush_pikachu:
        respuesta_compra = ""
        print("Lo siento no tienes suficientes puntos para comprarlo")

        respuesta = input("1 Para jugar. \n2 Para ver premios. \n3 Para ver puntos actuales\n0 para ver inventario: ")
    else:

        puntos -= 100
        fila1.insert(0, random.choice(a))
        fila1.insert(1, random.choice(a))
        fila1.insert(2, random.choice(a))
        fila1.pop(5)
        fila1.pop(4)
        fila1.pop(3)
        print(fila1)

        fila2.insert(0, random.choice(a))
        fila2.insert(1, random.choice(a))
        fila2.insert(2, random.choice(a))
        fila2.pop(5)
        fila2.pop(4)
        fila2.pop(3)
        print(fila2)

        fila3.insert(0, random.choice(a))
        fila3.insert(1, random.choice(a))
        fila3.insert(2, random.choice(a))
        fila3.pop(5)
        fila3.pop(4)
        fila3.pop(3)
        print(fila3)

        if fila1 == win_a or fila1 == win_b or fila1 == win_c or fila1[0] == "A" and fila2[0] == "A" and fila3[0] == "A"  or fila1[0] == "B" and fila2[0] == "B" and fila3[0] == "B"  or fila1[0] == "C" and fila2[0] == "C" and fila3[0] == "C":
         print(" \n¡Felicidades! ganaste 300 puntos\n")
         puntos += 300
         respuesta = input("1 Para jugar. \n2 Para ver  premios \n3 Para ver puntos actuales\n0 para ver inventario: \n")
        elif fila2 == win_a or fila2 == win_b or fila2 == win_c or fila1[1] == "A" and fila2[1] == "A" and fila3[1] == "A" or fila1[1] == "B" and fila2[1] == "B" and fila3[1] == "B" or fila1[1] == "C" and fila2[1] == "C" and fila3[1] == "C":
            print(" \n¡Felicidades! ganaste 300 puntos\n")

            respuesta = input("1 Para jugar. \n2 Para ver premios \n3 Para ver puntos actuales\n0 para ver inventario: \n")
            puntos += 300
        elif fila3 == win_a or fila3 == win_b or fila3 == win_c or fila1[2] == "A" and fila2[2] == "A" and fila3[2] == "A" or fila1[2] == "B" and fila2[2] == "B" and fila3[2] == "B" or fila1[2] == "C" and fila2[2] == "C" and fila3[2] == "C":
             print(" \n¡Felicidades! ganaste 300 puntos\n")
             puntos += 300

        else:

            respuesta = input( "\n1 Para jugar\n2 Para ver premios \n3 Para ver puntos actuales\n0 para ver inventario: \n")

if puntos < 100:
    print("¡Oh no! Te quedaste sin points UnU")
else:
    print("¡Ups!, Opcion incorrecta")













