def calcular_media_notas():
    notas = []
    for i in range (1, 5):
        nota = float(input(f'Digite a {i}ª nota Bimestral: '))
        notas.append(nota)

    media = sum(notas) / len(notas)
    print(f'A média das notas informada é {media:.2f}')


calcular_media_notas()

