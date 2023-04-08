texto = 'palavra'

letras_palavra = []
quantidade = len(palavra)
for n in range(quantidade):
    letras_palavra.append(texto[n])
print(letras_palavra)
vazia = ' '
novo_texto = vazia.join(letras_palavra)
w = novo_texto.replace(' ', '')
print(w)