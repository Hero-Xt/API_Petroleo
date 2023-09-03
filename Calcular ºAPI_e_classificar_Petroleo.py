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
def calculograuapi(densidade_agua, densidade_oleo, temperatura):
    d = densidade_oleo / densidade_agua
    api = (141.5 / d) - 131.5
    if temperatura != 60:
        api_corrigido = api + ((60 - temperatura) / 10)
        api = api_corrigido
        print(f'ºAPI: {api:.2f}')
        classificação(api)
    else:
        print(f'ºAPI: {api:.2f}')
        print("Petróleo: ", end="")
        classificação(api)
def conversao(temperatura):
    fahrenheit = (temperatura * 1.8) + 32
    temperatura = fahrenheit
    return temperatura

resposta = 'SIM'

while resposta == 'SIM':
    while True:
        print("-="*25)
        print('      Calcular ºAPI e classificar Petróleo!')
        print("-="*25)
        print('Calcular grau API [1]')
        print('Classificar Petróleo [2]')
        interacao_usuario = int(input())
        if interacao_usuario == 1 or interacao_usuario == 2:
            break
        else:
            print("-="*25)
            print('                      Erro!')
            print("-="*25)
    if interacao_usuario == 1:
        print("-="*25)
        densidade_agua = float(input('Densidade da água: '))
        densidade_oleo = float(input('Densidade da óleo: '))
        pergunta_temperatura = input('Temperatura em graus Celsius ?[sim/nao]').upper().strip()
        
        while (pergunta_temperatura != 'SIM') and (pergunta_temperatura != 'NAO') and (pergunta_temperatura != 'NÃO'):
            print("-="*25)
            print('                      Erro!')
            print("-="*25)
            pergunta_temperatura = input('Temperatura em graus Celsius ?[sim/nao]').upper().strip()
        if pergunta_temperatura == 'SIM':
            temperatura = int(input('Temperatura: '))
            temperatura = conversao(temperatura= temperatura)
        else:
            temperatura = int(input('Temperatura: '))
        print("-="*25)    
        calculograuapi(densidade_agua= densidade_agua, densidade_oleo= densidade_oleo, temperatura= temperatura)
        print("-="*25)
    if interacao_usuario == 2:
        print("-="*25)
        api = int(input('Digite o ºAPI do óleo: '))
        print("-="*25), print()
        classificação(api)
        print("-="*25), print()

    resposta = str(input('Continuar programa?[sim/nao] ')).upper().strip()
    while (resposta != 'NAO') and (resposta != 'NÃO') and (resposta != 'SIM'):
            print("-="*25)
            print('                      Erro!')
            print("-="*25)
            resposta = input('Continuar programa?[sim/nao] ').upper().strip()

print('Fim!')
