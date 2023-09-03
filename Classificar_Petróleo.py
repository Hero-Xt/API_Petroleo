def classificação(api):
    print("Petróleo: ", end="")
    if api >= 0 and api < 15:
        print('Asfáltico')
    elif api >= 15 and api < 19:
        print('Extrapessado')
    elif api >= 19 and api < 27:
        print('Pesado')
    elif api >= 27 and api < 33:
        print('Médio')
    elif api >= 33 and api < 40:
        print('Leve')
    elif api >= 40:
        print("Extraleve")
    else:
        print("VALOR FORA DO INTERVALO DE CLASSIFICAÇÃO!")

print("-="*25)
api = int(input('Digite o ºAPI do óleo: '))
print("-="*25), print()
classificação(api)
print("-="*25), print()