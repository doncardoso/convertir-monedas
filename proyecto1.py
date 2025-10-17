print("Bienvenico a conversor de monedas\n")

def convertir_moneda(moneda, valor, destino):

    if moneda == 1:

        def dolarTo():
            if destino == "1":
                print(f'${valor} dolares son ${valor * 3750} pesos colombianos')
            elif destino == "2":
                print(f'${valor} dolares son ¥{valor * 6.37} yuanes')
            elif destino == "3":
                print(f'${valor} dolares son £{valor * 0.76} libras esterlinas')
            else :
                print("no se reconoce a que moneda convertir")
        dolarTo()



    elif moneda == 2:

        def euroTo():
            if destino == "1":
                print(f'€{valor} euros son ${valor * 4000} pesos colombianos')
            elif destino == "2":
                print(f'€{valor} euros son ¥{valor * 6.93} yuanes')
            elif destino == "3":
                print(f'€{valor} euros son ¥{valor * 0.83} libras esterlinas')
            else :
                print("no se reconoce a que moneda convertir")
        euroTo()
    else:
        print("no se reconoce a que moneda convertir")




#datos
moneda= int(input("Ingresa tu moneda: \n 1.Dolar \n 2.Euro \n"))

valor = float(input("Ingresa tu valor: \n "))

destino = input(" a que ,moneda convertir? \n 1. Pesos colombianos \n 2. Yuanes \n 3. Libras esterlinas  \n ")


#llamar
convertir_moneda(moneda, valor, destino)









