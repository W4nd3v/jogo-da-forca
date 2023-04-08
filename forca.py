def forca(dica, palavra):
    cores = {'vermelho':'\033[31m',
             'amarelo':'\033[33m',
             'verde':'\033[32m',
             'fecha':'\033[m'}

    print('#' * 20)
    print('JOGO DA FORCA')
    print('#' * 20)
    print(f'DICA: {dica}')

    quantidade = len(palavra)
    verificador = 0
    lacuna = '___'
    palavra_mod = []
    vidas = 6
    erros = []
    while True:
        vencedor = []
        if vidas <= 0:
            print(f'{cores["vermelho"]}Você perdeu!{cores["fecha"]}')
            print(f'A palavra coreta era {palavra}')
            break

        if verificador == 0:
            aux = 1
            while aux <= quantidade:
                palavra_mod.append(lacuna)
                aux += 1
        if vidas >= 5:
            print(f'Vidas: ', end=" ")
            print(f'[{cores["verde"]}', end=" ")
            print(f' * ' * vidas, end=" ")
            print(f'{cores["fecha"]}]')
        elif vidas >= 2 and vidas <= 4:
            print(f'Vidas: ', end=" ")
            print(f'[{cores["amarelo"]}', end=" ")
            print(' * ' * vidas, end=" ")
            print(f'{cores["fecha"]}]')
        else:
            print(f'Vidas: ', end=" ")
            print(f'[{cores["vermelho"]}', end=" ")
            print(f' * ' * vidas, end=" ")
            print(f'{cores["fecha"]}]')
        print(f'Erros: {erros}')
        print('')
        for c in palavra_mod:
            if c == '___':
                vencedor.append(c)
            print(f'{c}', end=" ")
        print(" ")
        if verificador > 0:
            if len(vencedor) == 0:
                print(f'{cores["verde"]}Você venceu!{cores["fecha"]}')
                break

        palpite = input('Escolha uma letra: ').upper()
        print('')
        letras_palavra = []

        if palpite in palavra:
            for n in range(quantidade):
                if palpite == palavra[n]:
                    letras_palavra.append('ñ')
                    palavra_mod[n] = palpite
                else:
                    letras_palavra.append(palavra[n])

            vazia = ' '
            novo_texto = vazia.join(letras_palavra)
            w = novo_texto.replace(' ', '')
            palavra = w
        else:
            vidas -= 1
            erros.append(palpite)
        verificador += 1

palavra = str(input('Qual palavra secreta? ')).upper()
dica = str(input('Qual a dica? ').upper())
forca(dica, palavra)

''' 
pode responder qualquer hora
ranking
'''
