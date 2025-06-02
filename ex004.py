#Ler algo, mostrar o seu tipo primitivo e todas possibilidades possiveis
plvr = input('Digite uma palavra: ')

print('')
print(type(plvr))
print('É alfabetico:', plvr.isalpha())
print('É alfanumerico:', plvr.isalnum())
print('É numerico:', plvr.isnumeric())
print('Só possui espaço:', plvr.isspace())
print('Possui somente letras maiúscula:', plvr.isupper())
