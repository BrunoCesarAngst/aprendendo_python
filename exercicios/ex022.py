n = str(input('Escreva seu nome completo: ')).strip()
print('Analizando seu nome... ')
print('Seu nome em maisculo: {}.'.format(n.upper()))
print('Seu nome em minúsculo: {}.'.format(n.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(n) - n.count(' ')))
# print('Seu nome tem {} letras.'.format(n.find(' ')))
separa = n.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))