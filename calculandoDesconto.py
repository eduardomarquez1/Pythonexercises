preco = float(input("Qual o preço do produto: R$"))
desconto = (preco * 5) / 100
print("Você recebeu 5% de desconto nesse produto \n Agora ele custa R${}".format(preco - desconto))