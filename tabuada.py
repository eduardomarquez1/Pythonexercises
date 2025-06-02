tabuada = 0
numero = int(input("Digite um número: "))

for i in range(10):
    tabuada += 1
    print("{}X{} = {}".format(numero, tabuada, numero * tabuada))
