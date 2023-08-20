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
def calculograuapi(dagua, doleo, t):
    d = doleo / dagua
    api = (141.5 / d) - 131.5
    if t != 60:
        api_corrigido = api + ((60 - t) / 10)
        api = api_corrigido
        print(f'ºAPI: {api:.2f}')
        classificação(api)
    else:
        print(f'ºAPI: {api:.2f}')
        print("Petróleo: ", end="")
        classificação(api)
def conversao(t):
    f = (t * 1.8) + 32
    t = f
    return t

res = 'SIM'
while res == 'SIM':
    while True:
        print("-="*25)
        print('      Calcular ºAPI e classificar Petróleo!')
        print("-="*25)
        print('Calcular grau API [1]')
        print('Classificar Petróleo [2]')
        r = int(input())
        if r == 1 or r == 2:
            break
        else:
            print("-="*25)
            print('                      Erro!')
            print("-="*25)
    if r == 1:
        print("-="*25)
        dagua = float(input('Densidade da água: '))
        doleo = float(input('Densidade da óleo: '))
        temp = input('Temperatura em graus Celsius ?[sim/nao]').upper().strip()
        while (temp != 'SIM') and (temp != 'NAO') and (temp != 'NÃO'):
            print("-="*25)
            print('                      Erro!')
            print("-="*25)
            temp = input('Temperatura em graus Celsius ?[sim/nao]').upper().strip()
        if temp == 'SIM':
            t = int(input('Temperatura: '))
            t = conversao(t)
        else:
            t = int(input('Temperatura: '))
        print("-="*25)    
        calculograuapi(dagua, doleo, t)
        print("-="*25)
    if r == 2:
        print("-="*25)
        api = int(input('Digite o ºAPI do óleo: '))
        print("-="*25), print()
        classificação(api)
        print("-="*25), print()

    res = str(input('Continuar programa?[sim/nao] ')).upper().strip()
    while (res != 'NAO') and (res != 'NÃO') and (res != 'SIM'):
            print("-="*25)
            print('                      Erro!')
            print("-="*25)
            res = input('Continuar programa?[sim/nao] ').upper().strip()

print('Fim!')
