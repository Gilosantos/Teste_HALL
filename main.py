'''

Programa para teste de sondas HAll

'''
print("*****************************\n")
print("     TESTE DE SONDA HALL     \n")
print("*****************************\n")
while True:
    print("\n")
    hall = int(input("Modelo da hall: "))           #   Ex: 100, 150, 200, 400 (A) 
    current = float(input("Corrente lida: "))       #   Insira o valor de corrente lido no amperímetro
    sinal = (current*4)/hall
    if hall >= 400:                                 #   Para fundos de escala mais altos, fazer espiras na sonda hall (A carga usada alcança apenas 12A)
        voltas = int(input("Número de voltas: "))   #   insira o n° de espiras para fundos de escala mais altos
        sinal = sinal * voltas
    print("Sinal:", sinal)                         #   Compare este valor com o que foi lido no multímetro (tensão AC)
    
    


