altura = float(input("Qual a altura da parede em metros? "))
largura = float(input("Qual a largura da parede em metros? "))
area = altura * largura
tinta = area / 2
print("Sua parede tem {}m², serão necessários {}l de tinta para pintar a parede completamente".format(area, tinta))