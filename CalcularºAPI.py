def calculograuapi(densidade_agua, densidade_oleo, temperatura):
    d = densidade_oleo / densidade_agua
    api = (141.5 / d) - 131.5
    if temperatura != 60:
        api_corrigido = api + ((60 - temperatura) / 10)
        api = api_corrigido
        print(f'ºAPI: {api:.2f}')
    else:
        print(f'ºAPI: {api:.2f}')
        print("Petróleo: ", end="")

def conversao(temperatura):
    fahrenheit = (temperatura * 1.8) + 32
    temperatura = fahrenheit
    return temperatura

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